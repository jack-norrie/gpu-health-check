import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_gpu_temperatures(
    hw64_log_path,
    gpu_temp_cols: list[str] | None = None,
    max_memory_temp=105,
    max_core_temp=84,
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

    thermal_throttle_temp = float(
        (data["GPU Thermal Limit [°C]"].str.extract(r"(\d+\.?\d*)").astype(float))
        .min()
        .iloc[0]
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
        y=thermal_throttle_temp,
        color="orange",
        linestyle="--",
        label=f"Thermal Throttling Temp ({thermal_throttle_temp}°C)",
    )
    plt.axhline(
        y=max_core_temp,
        color="coral",
        linestyle="--",
        label=f"Max Core Temp ({max_core_temp}°C)",
    )
    plt.axhline(
        y=max_memory_temp,
        color="red",
        linestyle="--",
        label=f"Max Memory Temp ({max_memory_temp}°C)",
    )
    plt.legend()
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Temperatues (°C)")
    plt.title("GPU Temperatues")

    plt.tight_layout()

    plt.savefig(results_path, dpi=300)


if __name__ == "__main__":
    for hwinfo64_log_path in Path("data/1080 Ti").glob("*.CSV"):
        if "fan_stability" not in hwinfo64_log_path.stem:
            plot_gpu_temperatures(
                hwinfo64_log_path,
                gpu_temp_cols=None,
                max_core_temp=91,
                max_memory_temp=105,
            )
