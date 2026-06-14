"""Root entry point for the modular wind farm forecasting pipeline."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from wind_farm_forecast.pipeline import main

if __name__ == "__main__":
    main()
