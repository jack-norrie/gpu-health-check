import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from src.config import DATA_DIR


def plot_gpu_fans(
    hw64_log_path,
    gpu_fan_cols: list[str] | None = None,
):
    results_path = Path("results") / hw64_log_path.with_suffix(".PNG").relative_to(
        Path("data")
    )
    if not results_path.parent.exists():
        results_path.parent.mkdir(parents=True)

    data = pd.read_csv(
        hw64_log_path,
        encoding="cp1252",
        on_bad_lines="skip",
        low_memory=False,
    )

    if gpu_fan_cols is None:
        gpu_fan_cols = [
            col
            for col in data.columns
            if "gpu" in col.lower() and "fan" in col.lower() and "rpm" in col.lower()
        ]
    data = data[["Time"] + gpu_fan_cols]

    # Convert all GPU fan columns to numeric
    for col in gpu_fan_cols:
        data[col] = data[col].str.extract(r"(\d+\.?\d*)").astype(float)

        # Create a figure with a subplot for each fan
        fig, axes = plt.subplots(
            nrows=len(gpu_fan_cols),
            ncols=1,
            figsize=(8, 5 * len(gpu_fan_cols)),
            sharex=True,
            sharey=True,
            squeeze=False,
        )

        # Plot each fan in its own subplot
        for i, col in enumerate(gpu_fan_cols):
            data.plot(x="Time", y=col, ax=axes[i, 0])
            axes[i, 0].set_ylabel("Fan Speed (RPM)")
            axes[i, 0].set_title(f"{col}")
            axes[i, 0].tick_params(axis="x", rotation=45)
            plt.setp(axes[i, 0].get_xticklabels(), ha="right")

        plt.suptitle("GPU Fan Speeds", y=1.02)

    plt.tight_layout()

    plt.savefig(results_path, dpi=300)
