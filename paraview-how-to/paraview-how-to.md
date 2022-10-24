# Basics

## Shortcuts

| Key combination    | Action |
|--------------------|---------|
| `cmd+O`            | Open a new file |
| `option+space`     | Open the search window for filters|

## Load EAM output on cubed sphere

Key points: Because the cubed sphere mesh is an unstructured mesh, we needs to use ParaView's `CAM Reader` and provide a connectivity file in order to properly load EAM output in ParaView.

Detailed steps:

- Use `cmd+O`, the `Open File` button or the main menu -> `File` -> `Open...` to specify the EAM output file.
- ParaView will pop up a window asking which reader to use. Choose `NetCDF CAM Reader`.
- **Very important**: before hitting the `Apply` button in the `Properties panel`, find the box with the text `Connectivity File Name` to its left, click on the button with `...` to the right of the box to specify the connectivity file.
After specifying the connectivity file, click on the `Apply` button.

## "Auto Apply"

To let ParaView automatically apply changes specified in the `Properties` panel, go to `ParaView` -> `Preferences` -> `General` panel, check `Auto Apply`.

# Coordinates

## Tickmarks

- To turn on tickmarks and labels of the axes, go to the `Propoerties` panel and check the `Axis Grid` box
- Using the `Edit` button to the right of `Axis Grid`, one can also change the axis titles and their properties.


## Vertical coordinate

### Changing the aspect ratio of lat-z cross sections

- `option+space` then start typing `transform`. Click on the `Transform` box.
- In the `Properties` window, 
  - uncheck `Show Box` (optional)
  - for `scale`, change the 3rd number to a larger value (e.g., for ne30L30 data, since we have ~180 data points from North Pole to South Pole and 30 layers, setting the 3rd number to 6 will give us approximately a square for the lat-z cross section.

# Working with selections of grid points

## Conditional sampling

- A selection of grid points can be created using the `Find Data` functionality.
- Specify the selection criterion, then click on `Find Data`. The selected grid points will be marked in the renderview.
- In the `Find Data` panel, below the spreadsheet, there is an `Extract` button that can be used to create a new module in the pipline. 