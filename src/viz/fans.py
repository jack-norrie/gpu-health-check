import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


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

    plt.figure(figsize=(12, 6))  # Width: 12 inches, Height: 6 inches

    data.plot(x="Time", y=gpu_fan_cols)

    plt.legend()
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Fan Speed (RPM)")
    plt.title("GPU Fan Speeds")

    plt.tight_layout()

    plt.savefig(results_path, dpi=300)


if __name__ == "__main__":
    hwinfo64_log_path = Path("data/3090/fan_stability.CSV")
    plot_gpu_fans(hwinfo64_log_path)

