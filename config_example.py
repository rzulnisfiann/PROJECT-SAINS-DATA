
from pathlib import Path

# Ganti lokasi berikut sesuai lokasi Google Drive di laptop masing-masing
DATA_DIR = Path(r"H:\My Drive\PROJECT SAINS DATA\DATA")
OUTPUT_DIR = DATA_DIR.parent / "OUTPUT"
# Subfolder dataset
COMPOUND_DIR = DATA_DIR / "Compound_Jamur"
MAOB_DIR = DATA_DIR / "MAO-B"
ALPHA_SYNUCLEIN_DIR = DATA_DIR / "α-Synuclein"
