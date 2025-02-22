from src.viz.fans import plot_gpu_fans
from src.viz.temperatures import plot_gpu_temperatures
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from src.config import DATA_DIR

if __name__ == "__main__":
    hwinfo64_log_paths = list(DATA_DIR.glob("*.CSV"))

    hwinfo64_fan_log_paths = [
        p for p in hwinfo64_log_paths if "fan_stability" in p.stem
    ]
    plot_gpu_fans(hwinfo64_fan_log_paths[0])

    hwinfo64_temp_log_paths = [
        p for p in hwinfo64_log_paths if "fan_stability" not in p.stem
    ]
    for hw64_log_path in hwinfo64_temp_log_paths:
        plot_gpu_temperatures(hw64_log_path, gpu_temp_cols=None)
