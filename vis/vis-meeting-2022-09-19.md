* When: 2022-09-19, 11:30am PT, 2:30pm ET
* Who: 
* Topic: Using ParaView on EAM output

## Pre-meeting notes

### Hui's notes from 9/13/2022

* I uploaded a new sample output file `PD_1800_ad4fd8_ANN_climo_SE.nc` to [the directory](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/model_output_samples/). This file has more typical meteorological fields (like winds, temperature, clouds, aerosol-related quantities). Also, the values are annual averages, which can help us orient ourseleves.
* I downloaded ParaView 5.11.0-RC1 to my MacBook Pro (OS is 10.15.7, Catalina) and used it on the new sample data. See the two screenshots below.

### Loading the data file in ParaView

* After selecting `PD_1800_ad4fd8_ANN_climo_SE.nc` in the Open File dialogue, ParaView will pop up a window asking which reader to use. Choose "NetCDF CAM Reader".
* Very important: before hitting the "Apply" botton in ParaView, we need to go to the "Properties" panel, find the box with the text "Connectivity File Name" to its left, click on the botton with `...` to the right of the box to choose the connectivity file.
* After specifying the connectivity file, click on the "Apply" botton.

### Selecting fields to display

* In the "Properties" panel, under "Coloring", there is a box with the text "Solid Color". The list of fields/variables in the loaded data file is hidden in that botton.
* To change from, say, the group of variables defined at layer midpoints to the group of variables defined only at the Earth's surface, go to the "Properties" panel and use the button to the right of "Vertical Dimension".
* After making your choice using that button, remember to hit the "Apply" button in the "Properties" panel! Otherwise, the field list won't update.


 
