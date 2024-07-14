import os

from fairseq import checkpoint_utils


def get_index_path_from_model(sid):
    return "F:/audios/added_IVF1157_Flat_nprobe_1_kaede_akino_v2.index"


def load_hubert(config, hubert_path: str):
    models, _, _ = checkpoint_utils.load_model_ensemble_and_task(
        [hubert_path],
        suffix="",
    )
    hubert_model = models[0]
    hubert_model = hubert_model.to(config.device)
    hubert_model = hubert_model.half() if config.is_half else hubert_model.float()
    return hubert_model.eval()
