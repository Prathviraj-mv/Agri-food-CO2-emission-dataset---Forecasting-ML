from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = ROOT_DIR / "Dataset" / "Agrofood_co2_emission.csv"

RESULTS_DIR = ROOT_DIR / "Results"

MODELS_DIR = ROOT_DIR / "Saved_Models"