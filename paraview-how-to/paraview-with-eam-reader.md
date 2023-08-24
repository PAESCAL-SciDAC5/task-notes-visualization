

## Install a clean paraview in a new Python environment

```
conda create --name eamviz python=3.10.0 ipython 
conda activate eamviz
conda install -c conda-forge paraview=5.11.1 netcdf4 libcxx=16.0.3
```

## Start the just-installed version of Paraview

```
which paraview
```
and then execute that command (probably with an additional ` &` at the end).

## Import plugins for EAM

Download the following plugins:

https://gitlab.kitware.com/ayenpure/eam-scripts/-/blob/master/eam_reader.py

https://gitlab.kitware.com/ayenpure/eam-scripts/-/blob/master/eam_filters.py

Import the plugins:

- In the ParaView window, go to `Tools > Manage Plugins` and this should open a plugin manager.
- Select `Load New...` and select one python file at a time.

To avoid having to load these plugins every time you quit and start paraview, 
check the auto load check box for these plugins.

## Open EAM output

- Start `ParaView`
- Use the `Open` button or `File->Open`, select EAM output file.
- In the pop-up windown, choose `EAM Data Reader` as the reader. If you don't see this option, then import the EAM plugins following instructions above.
- Go to the `Properties` menu, start typing `connectivity` in the search box. Click on the `...` button, locate and select `TEMPEST_ne30pg2.scrip.renamed.nc`. (If you don't have the file, yet, download it from [NERSC](https://portal.nersc.gov/project/m4359/huiwan/vis/202308/)
- Click `Apply` in the `Properties` panel.
