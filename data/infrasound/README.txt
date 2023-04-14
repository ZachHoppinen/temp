TITLE

Dataset for Snow Attenuation of Infrasound Signals and Wind Noise

SUMMARY AND PURPOSE

This dataset is provided as a supplement to the manuscript "Snow Attenuation of Infrasound Signals and Wind Noise."

Infrasound monitoring of nuclear explosions, snow avalanches, and earthquakes may be seasonally 
impacted by snow burial of infrasound stations. A number of factors may impact infrasound
in snowpacks including: increased attenuation of the earthquake signals, reductions in wind noise,
and changes in the sound speed through the snowpack. To assess these factors we installed a
vertical array of sensors in the Sawtooth mountains of Idaho that was naturally buried by snow
throughout the 2021-2022 winter. Using 38 earthquake signals that were detected by the array
we calculate the frequency-dependent attenuation coefficient of infrasound by snowpacks and the
speed of the sound wave. The attenuation coefficients were undetectable between 0-8 Hz, but then
rose to 0.1 dB/cm at around 12 Hz, and above 12 Hz maintained a relatively constant 0.1 db/cm
attenuation. The speed of sound in the snow was measured at 160 ± 51 m/s, significantly sub-
sonic. Finally, there was a significant reduction in the amount of background noise measured for
snow-buried compared to free-air sensors with 24 dB of reduction observed for high-wind speeds
with only 20 cm of snow burial. This study provides a clearer understanding of how snow burial
will bias the ability of infrasound sensors to assess the power and timing of infrasound signals used
to monitor for natural and man-made hazards.

Digital waveforms for the entire winter of recording are provided as parquet files in the a3m-upper
and be4-lower directories. The format for the files are: YYYY-MM-DD-c{channel}.parq. The date
and time in the file are UTC.

Related code for this dataset is located at: https://github.com/ZachKeskinen/infrasound.

CREATOR(S)

Zachary Keskinen, Boise State University
zachkeskinen@gmail.com
https://orcid.org/0000-0003-0916-7774

Jeffrey Johnson, Boise State University
jeffreybjohnson@boisestate.edu
https://orcid.org/0000-0003-4179-8592

DATE(S)

Dataset release date:  January ??, 2023

Time Period Covered by Data: December 2nd, 2021 to June 26th, 2022

DATA ATTRIBUTES

ARRAY DATA
----------

The array data is all broadband three channel sound data from infraBSU version2 sensors
recorded at 200 Hz. Provided data have been converted to pascals.

The array data is split between two directories - a3m-upper and be4-lower. Within
each directory the data is split into each day of recording and into the three seperate
channels. be4-lower is the lower set of 3 sensors in the vertical infrasound profile.
a3m-upper is the top sensor of the vertical profile, the free-air sensor at 2.0 m
and an unused channel. The vertical geometry of the sensors is:

be4-lower:
channel 1 - 0.33 m
channel 2 - 0.66 m
channel 3 - 1.0 m

a3m-upper:
channel 1 - 1.33 m
channel 2 - unused
channel 3 - 2.0 m - free-air - horizontally seperate from vertical profile

All sensors were horizontally located at the banner snotel (44.30 N  -115.23 E).

The time index is in UTC.

GEOGRAPHIC INFORMATION

Banner Summit Snotel (44.30 N  -115.23 E)

FILE FORMATS

*.parq

LANGUAGE

English

FUNDER CITATION

This work was funded by U.S. Army CRREL, "Advancement of snow monitoring for water resources, vehicle mobility, and hazard mitigation:
using optical, microwave, acoustic, and seismic techniques", # W913E520C0017, and by NASA Terrestrial Hydrology Program, "Spatiotemporal Patterns in Snow Remote Sensing", #NNX17AL61G.

RIGHTS OR LICENSING INFORMATION

Users are free to share, copy, distribute and use the dataset; to create or produce works from the dataset; to adapt, modify, transform and build upon the dataset as long as the user attributes any public use of the dataset, or works produced from the dataset, referencing the author(s) and DOI link. For any use or redistribution of the dataset, or works produced from it, the user must make clear to others the license of the dataset and keep intact any notices on the original dataset.
