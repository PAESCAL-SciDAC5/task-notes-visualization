# EAMv1 output on the dynamics grid

- Data files: [see this folder on Compy](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/model_output_samples/)
- Connectivity files: [see this folder on Compy](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/connectivity_files/)

# EAMv2 output on the physics grid 

- Connectivity files: files starting with `TEMPEST` in [this folder on Compy](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/).
- Small sample data file containing only 1 time step: `aerosol_F2010.eam.h0.2014-12.nc` in [this folder on Compy](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/EAMv2/).
- NetCDF output files with multiple timesteps and some “ilev” variables:
  - Via browser: https://portal.nersc.gov/cfs/m4359/huiwan/vis/EAMv2_dust_sample_data/
  - On NERSC’s Community File System: `/global/cfs/cdirs/m4359/www/huiwan/vis/EAMv2_dust_sample_data/`

# EAMv2 output file with variables on both grids

- Via browser: https://portal.nersc.gov/cfs/m4359/huiwan/vis/EAMv2_bi_grid_sample_data/
- On NERSC’s Community File System: `/global/cfs/cdirs/m4359/www/huiwan/vis/EAMv2_bi_grid_sample_data/`

# EAMv2 output on the physics grid in a longitude-latitude box

- Via browser: https://portal.nersc.gov/cfs/m4359/huiwan/vis/EAMv2_lonlat_box_output_sample_data/
- On NERSC’s Community File System: `/global/cfs/cdirs/m4359/www/huiwan/vis/EAMv2_lonlat_box_output_sample_data/`

Explanation: 

The output file contains output in the lon-lat box of 0-360 longitude, 5N - 55N latitude. For this lon-lat box, 

- There is a special dimension `ncol_0e_to_360e_5n_to_55n = 18276` (in contrast to global output which would have the dimension `ncol = 21600`.
- Each variable written out in the box has the string `_0e_to_360e_5n_to_55n` appended to their name. For example, `cnd01_dst_a3_CHEM_0e_to_360e_5n_to_55n` is the variable `cnd01_dst_a3_CHEM` in the lon-lat box.
