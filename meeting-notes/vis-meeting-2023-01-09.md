- When: Jan 10, 2023, 2:30pm ET, 11:30am PT
- Who: Berk, Abhishek, Brianna, and Hui


# Meeting notes

We discussed updating ParaView's CAM reader to support the EAMv2's "physics grid".

Recap: Hui shared 
- a sample data file named `aerosol_F2010.eam.h0.2014-12.nc` (download from [here](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/));
- grid description files in Exodus and SCRIPS formats (see the same [directory](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/)). 
- The grid description files were generated with [this script](https://github.com/PAESCAL-SciDAC5/task-notes-visualization/blob/main/e3sm-how-to/make_SE_connectivity_files_using_Tempest_on_Compy.sh) using the TempestRemap tool

Discussions
- ParaView can open the Exodus file and show the mesh. There are 60x60 quadrilaterals on each face of the cubed sphere, suggesting these quadrilaterals correspond to the `ncol` dimension in the datafile.
- Berk and Abhishek will take this as a starting point to write a new reader. Will use Python and NetCDF binding instead of C++.


# Updates from later that week
- Hui plotted three 3D variables (`CLDTOT`, `TREFHT`, `PHIS`) using NCL. The plots and NCL scripts are uploaded to the same [directory](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/) as above.
- Berk wrote Python code to generate a VTK file, producing plots that Match Hui's.
- Abhishek started to work on the new reader based on Berk's work.
