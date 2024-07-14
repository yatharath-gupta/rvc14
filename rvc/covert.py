from pathlib import Path

from dotenv import load_dotenv
from scipy.io import wavfile

from rvc.modules.vc.modules import VC


def main():
      vc = VC()
      vc.get_vc("F:/audios/Szrv3.pth")
      tgt_sr, audio_opt, times, _ = vc.vc_inference(
            1, input_audio_path=Path("F:/audios/a3.wav"), f0_up_key=12, index_rate= 1
      )
      wavfile.write("F:/audiosoutput1.wav", tgt_sr , audio_opt)


if __name__ == "__main__":
      load_dotenv(".env")
      main()