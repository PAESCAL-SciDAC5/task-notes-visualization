When: Jan 10, 2023, 2:30pm ET, 11:30am PT
Who: Berk, Abhishek, Brianna, and Hui

# Meeting notes

## New ParaView reader

- Abhishek made good progress in developing a new, Python-based reader so that ParaView can recognize E3SM's output on the "atmospheric physics grid" which became the default output mesh since E3SMv2’s public release in fall 2021.

- In the next steps, we will give priority to supporting the physics grid and adding the features Chris Harris worked on (e.g., reading 1D variables related to the vertical coordinate; calculating air pressure using surface pressure and vertical coordinate parameters; using air pressure or geopotential height as vertical coordinate when rendering 3D fields).

- The new reader and features will be released through Conda install initially; Kitware will then work on adding them to ParaView binaries.

- For our project’s first report to DOE in March/April, we will aim at presenting a plot from ParaView showing E3SMv2 output on the physics grid.

- Later down the road, we will let the new reader also support the “old” cubed sphere mesh used in E3SMv1 and CAM-SE, as that “old” mesh (also referred to as the np4 grid consisting of the GLL nodes) is still used by the dynamical core.

## Chat about AI/ML

- Many researchers in the atmosphere modeling community have started working on using AI/ML techniques to build surrogate models and replace some subgrid physics parameterizations in a global atmospheric model. The resulting PDE-ML hybrid systems often encounter problems of numerical instability, i.e., the simulations would blow up after just a few months of integration despite the need to simulate multiple decades. Our project has a task that investigates the causes of such numerical instability from the perspective of understanding the interactions among atmospheric processes.

- Hui plans to ask Guang Zhang to present a tutorial on using AI/ML-based surrogate models for representing subgrid physics in atmospheric models, as well as Tao Zhang (BNL) to present a tutorial on other applications of AI/ML in atmosphere modeling.

- Berk says Kitware’s AI team is more familiar with using AI for analysis than building surrogates. Hui suggests our project might be able to use Kitware’s AI expertise for feature tracking – one very relevant example would be detecting 2-delta-t noise or non-physical oscillations in the z-direction in our simulations.
