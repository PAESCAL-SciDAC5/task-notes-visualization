* When: 2022-08-29
* Who: Hui and Berk
* Topic: mini ParaView GUI for EAM

# Pre-meeting notes from Hui


I would love to use ParaView for interactive, exploratory analysis of EAM output, and I imagine ParaView will become increasingly more helpful as the model's resolution increases. 

The challenges I encountered a few years back were:

* ParaView's many capabilities, buttons and menus can be daunting for new users.
* To use the CAM reader to load a CAM or EAM output file, we need to click several buttons in a specific sequence, which is cumbersome and error-prone.
* For 3D views, the CAM reader doesn't seem to know we want to revert the vertical coordinate (lev or ilev) by default, and there is no global map or coastline displaced, so it can be a bit hard to orient ourselves.

Based on this experience, I suggest that we create an EAM-specific UI. Below I've posted a first draft of a layout we could consider. Test data can be found at

* Connectivity file: [download from here](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/connectivity_files/)
* EAM output file (NetCDF): [download from here](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/model_output_samples/)

-----

![ParaView_mini_for_EAM_20220825.png](vis-meeting-2022-08-29_files/ParaView_mini_for_EAM_20220825.png)


------

# Meeting notes
