import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from src.config import THROTLING_TEMP, MAX_CORE_TEMP, MAX_MEMORY_TEMP


def plot_gpu_temperatures(
    hw64_log_path,
    gpu_temp_cols: list[str] | None = None,
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

    if gpu_temp_cols is None:
        gpu_temp_cols = [
            col
            for col in data.columns
            if "gpu" in col.lower() and "temp" in col.lower()
        ]
    data = data[["Time"] + gpu_temp_cols]

    # Convert all GPU temperature columns to numeric
    for col in gpu_temp_cols:
        data[col] = data[col].str.extract(r"(\d+\.?\d*)").astype(float)

    fig, axes = plt.subplots(
        nrows=len(gpu_temp_cols),
        ncols=1,
        figsize=(8, 5 * len(gpu_temp_cols)),
        sharex=True,
        sharey=True,
        squeeze=False,
    )  # Width: 12 inches, Height: 6 inches
    fig.suptitle("GPU Temperatues")

    for i, col in enumerate(gpu_temp_cols):
        axes[i, 0].set_title(col)
        data.plot(x="Time", y=col, ax=axes[i, 0])

        axes[i, 0].axhline(
            y=THROTLING_TEMP,
            color="orange",
            linestyle="--",
            label=f"Thermal Throttling Temp ({THROTLING_TEMP}°C)",
        )
        axes[i, 0].axhline(
            y=MAX_CORE_TEMP,
            color="coral",
            linestyle="--",
            label=f"Max Core Temp ({MAX_CORE_TEMP}°C)",
        )
        axes[i, 0].axhline(
            y=MAX_MEMORY_TEMP,
            color="red",
            linestyle="--",
            label=f"Max Memory Temp ({MAX_MEMORY_TEMP}°C)",
        )

        axes[i, 0].tick_params(axis="x", rotation=45)
        axes[i, 0].set_ylabel("Temperatues (°C)")
        axes[i, 0].legend()
    plt.tight_layout()

    plt.savefig(results_path, dpi=300)
