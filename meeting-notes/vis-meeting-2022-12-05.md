- When: Dec 5, 2022, 2:30pm ET, 11:30am PT
- Who: Berk, Chris, Brianna, and Hui

# Meeting notes

We discussed connectivity files.

- Since EAM has started using the so-called PG2 grid for physics parameterizations, and the model output are typically written on the PG2 grid, we need to update ParaView's reader to support this new grid.
- ParaView can load the PG2 grid using the [Exodus version of the grid description file](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/TEMPEST_ne30pg2.g).
- Sample output file from EAMv2 can be downloaded from [here](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/aerosol_F2010.eam.h0.2014-12.nc) 

Berk will play with the two files to see what updates are needed in the reader.

# Other updates

- Chris will move to NERSC. Berk will involve a new colleague to take over Chris's role.
- We will cancel the remaining weekly meetings in December. A new meeting series will be created for the next year.
