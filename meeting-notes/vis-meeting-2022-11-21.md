- When: Nov. 21, 2022, 2:30pm ET, 11:30am PT
- Who: Berk, Chris, Brianna, and Hui

# Meeting notes


### Updates on recent progress

- Chris finished updating the CAM NetCDF reader to import the information needed for calculating air pressure. Also made other improvements. Will test in Paraview.
- Hui obtained information about EAMv2's new physics grid and created connectivity files with help from Mark Taylor. See pre-meeting notes below.
- Kitware has been working with PNNL's Contracts office on the subcontract.

### Misc. comments

- Sean's first tutorial on cloud microphysics was informative. 
  [Link to recording](https://pnnl-my.sharepoint.com/personal/sean_santos_pnnl_gov/_layouts/15/stream.aspx?id=%2Fpersonal%2Fsean%5Fsantos%5Fpnnl%5Fgov%2FDocuments%2FRecordings%2FPAESCAL%20Microphysics%20Meeting%2D20221115%5F120632%2DMeeting%20Recording%2Emp4&ga=1) (- or go to Teams app, find on the calendar the meeting at 3pm ET on 11/15/2022 (the title was "introductory microphysics tutorial"), then double click on that event. Hopefully a link to the recording will show up near the top of the window.)

### Conclusions and to-do iterms

- The reader needs to be updated to support both the node-based and cell-based grids.
- Each connectivity file should include descriptions of both grids _as well as_ meta data. Hui can work on that; needs Berk/Chris to provide a list of 
  
    - variables to be included in a connectivity file and their preferred names, and
    - information to be included as meta data.


# Pre-meeting notes


### Grid update from EAMv1 to v2

In EAMv1, the same cubed sphere grid was used for both the fluid dynamics solver (i.e., the "dynamical core" or "dycore") and the physics parameterizations (i.e., the subgrid models for cloud microphysics, turbulence, etc.).

In EAMv2, the dycore grid stays unchanged, but the subgrid models are calculated at a different set of locations, as explained in [this paper by Hannah et al. (2021)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020MS002419).

Taking the NE30 mesh for example.

- There are 30x30x6 = 5400 **elements** over the whole globe. Figure 1 in [the paper by Hannah et al. (2021)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020MS002419) depicts a single element.
- Each element has 4x4 Gauss-Lobatto-Legendre (GLL) points (**nodes**), see green dots in Figure 1 of [Hannah et al. (2021)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020MS002419). Each node along the edges of the elements is shared by 2 or 3 elements, so the total number of unique nodes is `(30x30x6)x(3x3)+2 = 48602`.
- For calculating the subgrid models, each element is dividide into 2x2 **cells**, giving a total of `(30x30x6)x(2x2) = 21600` cells. The dashed red lines Figure 1 of [Hannah et al. (2021)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020MS002419) are the boundaries of the cells. These cells form the so-called "physics grid". Some colleagues are viewing this grid as a finite-volume grid, i.e., the values of physical quantities provided in each cell are the cell-averages. 




### Sample output file containing data on physics grid

See file `aerosol_F2010.eam.h0.2014-12.nc` in [this directory](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/), 

### Connectivity file for the cell-based mesh

New connectivity files were created by Hui following instructions from Mark Taylor.

- Script [`make_SE_connectivity_files_using_Tempest_on_Compy.sh`](https://github.com/PAESCAL-SciDAC5/task-notes-visualization/blob/main/e3sm-how-to/make_SE_connectivity_files_using_Tempest_on_Compy.sh)
- Connectivity files (see [this directory](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/)):
  - In SCRIP format with original variable names from Tempest: `TEMPEST_ne30pg2.scrip.nc`
  - In SCRIP format with revised variable names: `TEMPEST_ne30pg2.scrip.renamed.nc`
  - In Exodus format: `TEMEPST_NE30pg2.g`


