When: 2022-10-17, 11:30am PT, 2:30pm ET
Who: Hui, Berk, Chris, Brianna
Topic: Using ParaView on EAM output

# Meeting notes

## Using `lev` as vertical coordinate to visualize 3D variables

- Chris has fixed the problem in the CAM Reader. 
- Need to flip the coordinate because `lev = 0` is the top of model atmosphere and `lev = 1000` is the Earth's surface.
- Chris will add the option to show the vertical coordinate in `ln(lev)`.
- Chris will prepare a `conda` environment to allow Hui to install and play with ParaView on her Mac laptop with the new fixes and updates.

## Using `Z3` or `PMID` as vertical coordinate to visualize 3D variables.

- Background: EAM uses a pressure-based terrain-following vertical coordinate for spatial discretization.
The 1D variable `lev` is the air pressure at level midpoints _assuming the surface pressure is 1000 hPa_.
For physics-based analysis of the EAM output, it will be useful to use the _actual_ air pressure
or the geoptentential height (variable `Z3` in EAM's output) as the vertical coordinate.

- The data file Hui shared has the `Z3` variable. Chris will work on using it as the vertical coordinate.
- Hui can provide a new file with the 3D pressure field.

## Project management misc

- We plan to continue using GitHub and Markdown to take meeting notes. 
- Google Docs will be used for interactive editing for reports etc.
- Hui has turned on the "Discussions" tab for this repo (task-notes-visualization). We will use that for technical discussions.
- The task-notes-visualization repo has been public and we plan to keep it public.
- Chris will transfer his _trame_ scripts from his own repo to this repo.
- Hui agreed to give a project overview to RAPIDS2.
- Berk will arrange a high-level tutorial to introduce CMake/CTest/CDash etc. to the PAESCAL team.
- Hui and Berk will arrange meetings to understand and address specific project tasks' testing needs (e.g., the CLUBB-FV task)
