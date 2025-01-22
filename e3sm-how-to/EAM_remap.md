# Remapping EAM output between horizonal meshes

EAM's fluid dynamics solver and large-scale advection algorithm use, for the horizontal discretization, the cubed sphere mesh which is considered to be an unstructured mesh.

For visualization and analysis, it is often useful to remap the data to a latitude-longitude mesh. This can be done using the `ncremap` command of the [netCDF Operators (NCO)](http://nco.sourceforge.net).

## Using NCO at DOE LCFs

After logging into an LCF system or E3SM-dedicated computer (e.g., Compy at PNNL), try 

```
module load nco
```

At NERSC, starting in AY25, NCO (and CDO, NCL, ncview) can be accessed after using

```
module load climate-utils
```

After that, type `ncremap` or any other NCO command, and the basic usage will be shown in your terminal.


## The `ncremap` command

### Remap an entire file

```
ncremap -m ${map_file} -i ${input_file} -o ${output_file}
```

Here `${map_file}` is the name of a file containing the pre-computed weights for doing the remapping. See the "_Remapping files_" section below. 

Example:

```
ncremap -m ../map_files/map_ne30np4_to_cmip6_180x360_aave.20181001.nc -i PD_1800_ad4fd8_ANN_climo_SE.nc -o PD_1800_ad4fd8_ANN_climo_latlon_180x360.nc
```

- The map file `map_ne30np4_to_cmip6_180x360_aave.20181001.nc` can be downloaded from [here](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/map_files/)
- The climo file `PD_1800_ad4fd8_ANN_climo_SE.nc` containing data on the cubed sphere mesh can be downloaded from [here](https://compy-dtn.pnl.gov/wanh895/ParaView_EAM/cubed_sphere/model_output_samples/)


Afterwards, you can check the dimension sizes of the remapped fields using

```
ncdump -h PD_1800_ad4fd8_ANN_climo_latlon_180x360.nc
```
(To use the `ncdump` command at LCFs, you might need to first `module load netcdf`.)


### Remap a subset of variables from a file

```
ncremap -v ${variable_list} -m ${map_file} -i ${input_file} -o ${output_file}
```

Here `${variable_list}` is a list of variables to be remapped. 

Example:

```
ncremap -v T,Q,FSNT -m map.nc -i in.nc -i out.nc
```





## Remapping files

Where to find them:

* In the internet, check, for example [https://web.lcrc.anl.gov/public/e3sm/mapping/maps/](https://web.lcrc.anl.gov/public/e3sm/mapping/maps/) 
* On Compy at PNNL, check the directory `/qfs/people/zender/data/maps/`
* On Cori at NERSC, look under `/global/homes/z/zender/data/maps/`

Which files to use:

* For E3SMv1 output, look for file names like `map_ne*np4_to_*.nc`. For example,
`/qfs/people/zender/data/maps/map_ne30np4_to_cmip6_180x360_aave.20181001.nc` is for converting data from the ne30np4 cubed sphere grid to 1-degree lon-lat grid

* For E3SMv2, look for file names like `map_ne*pg2_to_*.nc`, as the v2 atmosphere model uses the `pg2` variant of the cubed sphere mesh for the parameterizations (sub-grid models).


