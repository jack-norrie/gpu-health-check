# gpu-health-check

<!--toc:start-->
- [gpu-health-check](#gpu-health-check)
  - [Description](#description)
  - [Procedure](#procedure)
    - [Physical Inspection](#physical-inspection)
    - [GPU Installation](#gpu-installation)
    - [Fan Health](#fan-health)
    - [Stability and Performance](#stability-and-performance)
      - [Memory](#memory)
      - [Core Stability](#core-stability)
      - [Performance](#performance)
      - [Holistic](#holistic)
  - [Usage](#usage)
<!--toc:end-->

## Description

The following is a checklist of tests, highly inspired by this [video](https://www.youtube.com/watch?v=oRMPp-8IGQw), which can be run in order to assess the health of a recently bought second hand GPU. These tests are relatively quick to perform and should let you assess the quality of the GPU before any return policy windows expire.

>[!WARNING]
> This guide is provided for informational purposes only. Given the significant investment GPUs represent, users should exercise their own judgment when making purchasing decisions. While these tests have worked for me personally when evaluating second-hand GPUs, I cannot guarantee their effectiveness in all situations and accept no responsibility for any purchasing decisions made based on this guide.

## Procedure

### Physical Inspection

The following are some things to look out for during a first physical inspection:

- A broken warranty seal - This means the previous owner has likely opened the card up at some point. Another telltale sign of this is if the thermal pads look "chunky", i.e., they have likely installed their own. This is not immediately a bad thing, but it does increase the likelihood that something is wrong with the card - why did they have to open it up? Did they break anything when they opened it up? etc.
- Liquid coming out of the fans - This implies the lubricant seal has broken. This is a very bad sign in terms of the health of the fans and is likely going to cause a mess when they turn on.
- Look to see if the heatsink is clogged with dust/obstructions. This can be an indication of how the card was looked after by the previous owner.
- Look to see if the card is rusting - This implies the card has been in a humid environment and it is likely this will have an adverse effect on the card's lifespan.

### GPU Installation

Immediately before installing your new GPU you should run [DDU](https://www.guru3d.com/download/display-driver-uninstaller-download/) on your system to remove any drivers that may exist on your system for your old GPU. After doing this you should shut your system down and install your new GPU. Finally, when you first log onto your system after having installed the GPU, be sure to install the latest version of your GPU drivers. Now is also a good time to open up a program like GPU-Z to check that your system is detected the expected card and that it's sensors are feeding.

![gpuz](docs/gpuz.PNG)

### Fan Health

Fans are typically the first point of failure and as such it is the first thing we will check. The main thing we want to check is that the fan is able to maintain a set RPM for a prolonged period of time without any spikes, as this would be a sign the fan was dying. The test procedure for this is as follows:

- Use [HWiNFO64](https://www.hwinfo.com/download/) to log fan speeds.
- Use MSI afterburner to set a specific fan speed.
- Set the speed to 50% for 30 minutes and then 100% for another 30 minutes.

>[!TIP]
> Make sure your fans are synced if that is an option.

>[!WARNING]
> Often you will see a mismatch between the fans the software detects and the number of physical fans you see. Most commonly this occurs when there are 3 physical fans but only 2 fans detected. This is usually because multiple fans are connected to the same fan header via a hub.

Now with the logged fan data, you can use plotting software of your choice to analyze the data. You are looking for a relatively consistent curve for your set speeds, i.e., no spikes. For example, the plot below shows a stable fan curve for the above experiment.

![fan_stability](docs/fan_stability.PNG)

### Stability and Performance

For all of the following tests run HWiNFO64, as was described in the previous section to log your system's sensor data. These tests will be putting your system throughout fairly demanding workloads and as such this is a good opportunity to evaluate the thermal performance of the card, i.e. whether the card is thermal throttling or reaching unsafe temperatures. Specifically the two temperatures we will be most interested in are the:

- GPU core temperature - This should stay under the rated temperature on your GPU manufacturer's website.
  - For example a 3090 should stay under [93](https://www.nvidia.com/en-gb/geforce/graphics-cards/30-series/rtx-3090-3090ti/) degrees.
- Your card will also have a throttling temperature, which is lower than the core temperature limit. When your card hits this temperature, it will throttle its power consumption to protect itself (i.e., stop itself from hitting its thermal limit). Ideally, you should be operating below the throttling temperature, otherwise your card could theoretically perform better if it had additional thermal headroom and wasn't throttling.

- GPU hot spot - This is usually representative of the temperature at the memory junction and as such should be less than the maximum rated temperature for the VRAM, this can usually be found via the associated micron spec sheet.
  - For example, GDDR6X is rated up to [95](https://www.micron.com/products/memory/graphics-memory/gddr6x).

>[!NOTE]
> High temperatures primarily affect your GPU in two ways:
>
> 1. Performance throttling: Modern GPUs will automatically reduce their clock speeds when approaching their thermal limits to protect themselves. This results in reduced performance.
> 2. Efficiency reduction: GPUs operate more efficiently at lower temperatures, consuming less power and potentially lasting longer.
> Therefore, maintaining temperatures well below the maximum rated limits provides better performance and longevity.

>[!WARNING]
> While modern GPUs have multiple thermal protection mechanisms, any of the following conditions indicate a serious problem requiring immediate shutdown:
>
> - Temperatures exceeding manufacturer-specified maximum limits
> - Temperatures continuing to rise despite thermal throttling
> - Unusual temperature spikes or thermal behavior
>
>These conditions could indicate failed thermal protection systems and pose potential safety risks including fire hazards.

#### Memory

- Quick test - [GPUMemTest](https://www.programming4beginners.com/gpumemtest) to quickly check the card's memory. ![gpumemtest](docs/gpumemtest.PNG)
- Extensive test - The [OCCT](https://www.ocbase.com/) VRAM test. ![occt_vram](docs/occt_vram.PNG)

#### Core Stability

Run the [OCCT](https://www.ocbase.com/) 3D standard test with error detection.
![occt_standard3d](docs/occt_standard3d.PNG)

>[!NOTE]
> It is normal to hear coil whine while performing this test; this is not a concern.

#### Performance

The previous tests are assessing hardware faults based on the existence of computational errors. Assuming the hardware is not faulty, we are now interested in how it is performing relative to how it should.

A good test for this is the [Superposition](https://benchmark.unigine.com/superposition) benchmark, which will give you a score that you can compare to others running similar hardware to yourself.

![superposition](docs/superposition.PNG)

>[!warning]
> Many users who post their scores online are doing so for competative reasons, trying to see how far they can push their bespoke cooling setup, undervolts, overclocks etc. For the purpose of seeing if you are getting the hardware you expect, it would be wise to compare your performance to the median for similar hardware - skip past the top entries.

#### Holistic

The previous tests are all quite insular in nature, testing a modular part of the graphics card. As a final holistic test you should run the graphics card through some intense application that uses all facets of the graphics card. A demanding 3D game is a great option for such a test. As a human you will have a much better chance spotting artifacting over an hour long gaming session than a test suite that is trying to detect such phenomenon, that is often card specific.  

>[!TIP]
> Use RivaStatistics to get in depth system printouts during your games, it comes bundled with MSI afterburner. Just tick the show on screen checkbox and tick anything you want to see

## Usage

If you would like to replicate the plots made throughout this repo, you can run the plotting code via the docker app associated with this repo. Simply create a `/data` directory in the root of this repo with your HWiNFO64 logs. Then perform any additional configuration you desire in `src/config.py`. Then run the commands below to make a results directory if it does not already exist, build a docker image, and finally run this docker image.

```bash
mkdir -p results && \
docker build -t gpu-health-check . && \
docker run -v $(pwd)/results:/app/results gpu-health-check
```
