from pathlib import Path
from MMSA import MMSA_run, get_config_regression

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "MOSI" / "Processed" / "unaligned_50.pkl"

config = get_config_regression('lmf', 'mosi')

config['featurePath'] = str(DATA_PATH)

MMSA_run(
    model_name='lmf',
    dataset_name='mosi',
    config=config,
    seeds=[1111],
    gpu_ids=[0],
    num_workers=0
)