



# Pre-meeting notes

EAMv2's cubed sphere meshes used by the physics parameterization are different from the v1 model's meshes. 
At the NE30 horizontal resolution, the output are now defined at 21600 cell centers instead of
48602 nodes.

Here is a sample output file from EAMv2: 
see [this directory](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/), 
file `aerosol_F2010.eam.h0.2014-12.nc`

Hui created new connectivity files following instructions from Mark Taylor.

- Script [`make_SE_connectivity_files_using_Tempest_on_Compy.sh`](https://github.com/PAESCAL-SciDAC5/task-notes-visualization/blob/main/e3sm-how-to/make_SE_connectivity_files_using_Tempest_on_Compy.sh)
- Connectivity files (see [this directory](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/)):
  - In SCRIP format with original variable names from Tempest: `TEMPEST_ne30pg2.scrip.nc`
  - In SCRIP format with revised variable names: `TEMPEST_ne30pg2.scrip.renamed.nc`
  - In Exodus format: `TEMEPST_NE30pg2.g`
