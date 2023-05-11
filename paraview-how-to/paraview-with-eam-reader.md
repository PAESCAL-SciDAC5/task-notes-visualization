

## Install a clean paraview in a new Python environment

```
conda create --name eamviz python=3.10.0 ipython 
conda activate eamviz
conda install -c conda-forge paraview netcdf4
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
