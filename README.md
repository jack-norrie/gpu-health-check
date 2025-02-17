# gpu-health-check

## Description
The following is a checklist of tests, highly inspired by this [video](https://www.youtube.com/watch?v=oRMPp-8IGQw), which can be run in order to assess the health of a recently bought second hand GPU. These tests are relatively quick to perform and should let you assess the quality of the GPU before any return policy windows expire.

>[!warning]
> This guide is provided for informational purposes only. Given the significant investment GPUs represent, users should exercise their own judgment when making purchasing decisions. While these tests have worked for me personally when evaluating second-hand GPUs, I cannot guarantee their effectiveness in all situations and accept no responsibility for any purchasing decisions made based on this guide.

## Physical Inspection
The following are some things to look out for during a first physical inspection:
* A broken warranty seal - This means the previous owner has likely opened the card up at some point. Another telltale sign of this is if the thermal pads look "chunky", i.e., they have likely installed their own. This is not immediately a bad thing, but it does increase the likelihood that something is wrong with the card - why did they have to open it up? Did they break anything when they opened it up? etc.
* Liquid coming out of the fans - This implies the lubricant seal has broken. This is a very bad sign in terms of the health of the fans and is likely going to cause a mess when they turn on.
* Look to see if the heatsink is clogged with dust/obstructions. This can be an indication of how the card was looked after by the previous owner.
* Look to see if the card is rusting - This implies the card has been in a humid environment and it is likely this will have an adverse effect on the card's lifespan.

## Instalation
Immidiately before installing your new GPU you should run DDU on your system to remove any drivers that may exist on your system for your old GPU. After doing this you should shut your system down and install your new GPU.


When installing a new GPU run DDU


## Fan test
Fans are the typical first point of failure.
Use MSI afterburner to set a specific fan speed.
Use HWInfo64 to log fan speeds
Run at 50% for 30 minutes and 100% for 30 minutes.
Make sure your fans are synced if that is an option and do not worry about a mismatch in the number of logged fans and the number of physical fans, sometimes some fans are considerd one fan logically
When you analyse the resulting data it should be relatively stable, flucuations are fine, but large spikes are not.

## Stability and Performance 
For all of these test use HWInfo64 to log temperature. 
Check the Nvidia website to see maximum allowed temperatures, the site will quote the maximum allowed core temperature.
For the maximum allowed hotspot temperature look up the memory type of the card and see what its maximum allowed value is. For example, GDDR6X memory should be kept under 105 degrees according to the micron spec sheet.

### Memory
Use gpumeMtest to quickly check the card's memory
Use OCCTs VRAM test for 1 hour

### Core Stability
Run OCCTs 3D standard test - it is normal to hear coil whine while performing this test, this is not a concern.

### Performance
The previous tests are mainly looking for actual faults with the hardware. Assuming the hardware is not faulty, we are now interested in how it is performing relative to how it should.
For this we can use Superposition, which will give a result that you can compare with to others online with similar systems.
Beware though, some are competative about this and will be using highly optimised setups, e.g. water cooling etc. with the best CPUs
You will want to compare it to the median performance for someone with your CPU and GPU combination.

### Holistic View
All the previous tests are quite abstract. A final test would be to play a video game, as this will show artefacts, that a test might struggle to see, but would be very obvious to a human.
Usr RivaStatistics to get in depth system printouts during your games, it comes bundled with msi afterburner.
Just tick the show on screen checkbox and tick anything you want to see

