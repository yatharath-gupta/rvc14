import json
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from scipy.io import wavfile
import tempfile
from pathlib import Path

from rvc.modules.vc.modules import VC

app = FastAPI()

class VCParams(BaseModel):
    f0_up_key: int
    index_rate: float

@app.post("/process_audio")
async def process_audio(
    params: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        # Parse the JSON string manually
        params_dict = json.loads(params)
        # Validate the parsed dictionary using Pydantic
        vc_params = VCParams(**params_dict)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON in params")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Create a temporary directory to store input and output files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save the uploaded file
        input_path = Path(temp_dir) / "input.wav"
        with input_path.open("wb") as buffer:
            buffer.write(await file.read())

        # Set up the output path

        # Initialize VC
        vc = VC()
        vc.get_vc("F:/audios/Szrv3.pth")

        # Process the audio
        tgt_sr, audio_opt, times, _ = vc.vc_inference(
            1,
            input_audio_path=input_path,
            f0_up_key=vc_params.f0_up_key,
            index_rate=vc_params.index_rate
        )

        # Save the output
        wavfile.write("F:/outputies/stuffies1", tgt_sr, audio_opt)

        # Return the output file
        return FileResponse("F:/outputies/stuffies1", media_type="audio/wav", filename="output.wav")

if __name__ == "__main__":
    load_dotenv(".env")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)