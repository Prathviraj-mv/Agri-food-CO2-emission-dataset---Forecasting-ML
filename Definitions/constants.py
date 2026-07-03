from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = ROOT_DIR / "Dataset" / "HIGGS_500k.csv"

RESULTS_DIR = ROOT_DIR / "Results"

MODELS_DIR = ROOT_DIR / "ML_Model"

OUTPUT_DIR_p = ROOT_DIR / "Plots" / "preprocessingHeatmap"
OUTPUT_DIR_rf = ROOT_DIR / "Plots" / "plots"
OUTPUT_DIR_lr = ROOT_DIR / "Plots" / "plots"
OUTPUT_DIR_ = ROOT_DIR / "Plots" / "plots"

