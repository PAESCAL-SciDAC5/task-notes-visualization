
- When: Feb 27, 2023, 3:00pm ET, noon PT 
- Who: Berk, Abhishek, Brianna, and Hui

# Meeting notes

We discussed the current status of the new ParaView Reader for EAM and the next steps.


## Current status

Abhishek has created a ParaView reader named `EAM_reader` in Python. With the new reader, ParaView can show 2D fields (e.g., CLDTOT) on EAM's "physics grid".

The EAM output variables to be loaded are hardcoded for now. This will be changed soon. See below.

## Next steps

- Dimensions in EAM output files: only deal with `time`, `ncol`, `lev` and `ilev` for now.
- Reader output:
  - Should organize fields in EAM output into 3 objects: 2D variables, 3D midpoint variables (vertical dimension: `lev`), 3D interface variables (vertical dimension: `ilev`)
  - `hyai`, `hybi`, `hyam`, `hybm` should be imported as auxiliary data that can be used to compute additional quantities.
- Vertical coordinate: in addition to using layer indices (1, 2, 3, 4, ...), we would like to have
  - Z3 as the vertical coordinate for variables with `lev` dimension. Z3 should be available as in the NetCDF file.
  - Air pressure as the vertical coordinate, see [GitHub discussion](https://github.com/PAESCAL-SciDAC5/task-notes-visualization/discussions/4), with options of linear or log-linear tranformation.
  - Note that values of Z3 increases as we go up from the ground, but air pressure is zero at the top of the atmosphere and increase as we go downward towards the ground.
- Image rendering: show the original grid; no smoothing.
- Map projection: set default to show the entire globe in lat-lon grid (instead of part of a sphere).



