* When: 2022-11-08, 11:30am PT, 2:30pm ET
* Who: Berk Geveci, Brianna Major, Chris Harris, Hui Wan
* Topic: mini ParaView GUI for EAM

# Chris's update

Made a lot of progress on the _trame_-based UI for EAM:
- Finished the Conda Paraview package for Mac OS with Intel cores. See README.md in the trame-eam repo.
- Restructured scripts.
- Render views now automatically use the preferred aspect ratio. The axis labels and the unit of the z-axis are turned on by default.
- The UI now supports both the layer index and the `lev` variable as options for the z-axis. The choice can be made for each individual view. 
- A toggle between linear and logarithmic scales is now available for the z-axis.
- Calculation of air pressure is in progress. Need to revise the CAM Reader so that it exposes 1D and 0D variables needed by the calculation.

# To-do

- Chris will continue to work on the calculaiton of air pressure and then using pressure as the third option for the z-axis.
- Hui will contact Mark Taylor to get a connectivity file for EAMv2's ne30pg2 mesh.

# Misc management updates

- Berk has identified a Kitware colleague for the CMake tutorial. Will connect Hui with him.
- PNNL is working on pushing the subcontract paperwork through our internal pipeline.
