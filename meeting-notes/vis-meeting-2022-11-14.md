



# Pre-meeting notes


Grid update from EAMv1 to v2:

In EAMv1, the same cubed sphere grid was used for both the fluid dynamics solver (i.e., the "dynamical core" or "dycore") and the physics parameterizations (i.e., the subgrid models).

In EAMv2, the dycore stays unchanged, but the subgrid models are calculated at a different set of locations. Taking the NE30 mesh for example.
- We have 30x30x6 = 5400 elements.
- Each element has 4x4 Gauss-Lobatto-Legendre (GLL) points (nodes). The nodes along the edges of the elements are shared by 2 or 3 elements, so the total number of nodes is `(30x30x6)x(3x3)+2 = 48602`.
- For calculating the subgrid models, each element is dividide into 2x2 cells, giving a total of `(30x30x6)x(2x2) = 21600` cells. These cells form the so-called "physics grid". Many colleagues are viewing this grid as a "finite-volume" grid, i.e., the solution values provided for each cell are the cell-averages. 

Figure 1 in [this paper](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020MS002419) is a useful illustration. The dashed red lines are the boundaries of the new, "finite-volume" cells, while the green dots are the GLL nodes used by the dycore (and the subgrid models in v1).


Sample output file from EAMv2: 
see [this directory](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/), 
file `aerosol_F2010.eam.h0.2014-12.nc`

Hui created new connectivity files following instructions from Mark Taylor.

- Script [`make_SE_connectivity_files_using_Tempest_on_Compy.sh`](https://github.com/PAESCAL-SciDAC5/task-notes-visualization/blob/main/e3sm-how-to/make_SE_connectivity_files_using_Tempest_on_Compy.sh)
- Connectivity files (see [this directory](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/)):
  - In SCRIP format with original variable names from Tempest: `TEMPEST_ne30pg2.scrip.nc`
  - In SCRIP format with revised variable names: `TEMPEST_ne30pg2.scrip.renamed.nc`
  - In Exodus format: `TEMEPST_NE30pg2.g`

It is likely that the original reader in ParaView needs to be extended in order to support this grid.
