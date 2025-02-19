import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_gpu_temperatures(
    hw64_log_path,
    gpu_temp_cols: list[str] | None = None,
    max_core_temp=84,
    max_memory_temp=105,
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

    plt.figure(figsize=(12, 6))  # Width: 12 inches, Height: 6 inches

    data.plot(x="Time", y=gpu_temp_cols)
    plt.axhline(
        y=84,
        color="orange",
        linestyle="--",
        label=f"Max Core Temp ({max_core_temp}°C)",
    )
    plt.axhline(
        y=105,
        color="red",
        linestyle="--",
        label=f"Max Memory Temp ({max_memory_temp}°C)",
    )

    plt.legend()
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig(results_path, dpi=300)


if __name__ == "__main__":
    hwinfo64_log_path = Path("data/3090/gaming_session.CSV")
    plot_gpu_temperatures(
        hwinfo64_log_path, gpu_temp_cols=None, max_core_temp=84, max_memory_temp=105
    )
