# trace generated using paraview version 5.11.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'NetCDF CAM reader'
pD_1800_ad4fd8_ANN_climo_SEnc = NetCDFCAMreader(registrationName='PD_1800_ad4fd8_ANN_climo_SE.nc', ConnectivityFileName='',
    FileName=['/Users/wanh895/Desktop/vis/ParaView/PD_1800_ad4fd8_ANN_climo_SE.nc'])
pD_1800_ad4fd8_ANN_climo_SEnc.VerticalDimension = 'Midpoint layers [time, lev, ncol]'
pD_1800_ad4fd8_ANN_climo_SEnc.PointArrayStatus = ['AEROD_v [time,ncol]', 'AODDUST1 [time,ncol]', 'AODDUST3 [time,ncol]', 'AODVIS [time,ncol]', 'CDNUMC [time,ncol]', 'CLDHGH [time,ncol]', 'CLDLOW [time,ncol]', 'CLDMED [time,ncol]', 'CLDTOT [time,ncol]', 'FLDS [time,ncol]', 'FLNS [time,ncol]', 'FLNSC [time,ncol]', 'FLNT [time,ncol]', 'FLNTC [time,ncol]', 'FLUT [time,ncol]', 'FLUTC [time,ncol]', 'FSDS [time,ncol]', 'FSDSC [time,ncol]', 'FSNS [time,ncol]', 'FSNSC [time,ncol]', 'FSNT [time,ncol]', 'FSNTC [time,ncol]', 'FSNTOA [time,ncol]', 'FSNTOAC [time,ncol]', 'ICEFRAC [time,ncol]', 'LANDFRAC [time,ncol]', 'LHFLX [time,ncol]', 'LWCF [time,ncol]', 'OCNFRAC [time,ncol]', 'PBLH [time,ncol]', 'PHIS [time,ncol]', 'PRECC [time,ncol]', 'PRECL [time,ncol]', 'PRECSC [time,ncol]', 'PRECSL [time,ncol]', 'PS [time,ncol]', 'PSL [time,ncol]', 'QFLX [time,ncol]', 'SHFLX [time,ncol]', 'SNOWHICE [time,ncol]', 'SNOWHLND [time,ncol]', 'SOLIN [time,ncol]', 'SWCF [time,ncol]', 'TAUX [time,ncol]', 'TAUY [time,ncol]', 'TGCLDIWP [time,ncol]', 'TGCLDLWP [time,ncol]', 'TMQ [time,ncol]', 'TREFHT [time,ncol]', 'TS [time,ncol]', 'U10 [time,ncol]', 'ANRAIN [time,lev, ncol]', 'ANSNOW [time,lev, ncol]', 'AQRAIN [time,lev, ncol]', 'AQSNOW [time,lev, ncol]', 'AREI [time,lev, ncol]', 'AREL [time,lev, ncol]', 'AWNC [time,lev, ncol]', 'AWNI [time,lev, ncol]', 'CCN3 [time,lev, ncol]', 'CLDICE [time,lev, ncol]', 'CLDLIQ [time,lev, ncol]', 'CLOUD [time,lev, ncol]', 'DCQ [time,lev, ncol]', 'DTCOND [time,lev, ncol]', 'DTV [time,lev, ncol]', 'FICE [time,lev, ncol]', 'FREQI [time,lev, ncol]', 'FREQL [time,lev, ncol]', 'FREQR [time,lev, ncol]', 'FREQS [time,lev, ncol]', 'ICIMR [time,lev, ncol]', 'ICWMR [time,lev, ncol]', 'IWC [time,lev, ncol]', 'NUMICE [time,lev, ncol]', 'NUMLIQ [time,lev, ncol]', 'OMEGA [time,lev, ncol]', 'OMEGAT [time,lev, ncol]', 'Q [time,lev, ncol]', 'QRL [time,lev, ncol]', 'QRS [time,lev, ncol]', 'RELHUM [time,lev, ncol]', 'T [time,lev, ncol]', 'U [time,lev, ncol]', 'UU [time,lev, ncol]', 'V [time,lev, ncol]', 'VD01 [time,lev, ncol]', 'VQ [time,lev, ncol]', 'VT [time,lev, ncol]', 'VU [time,lev, ncol]', 'VV [time,lev, ncol]', 'WSUB [time,lev, ncol]', 'Z3 [time,lev, ncol]']
pD_1800_ad4fd8_ANN_climo_SEnc.SingleMidpointLayer = 0
pD_1800_ad4fd8_ANN_climo_SEnc.MidpointLayerIndex = 0
pD_1800_ad4fd8_ANN_climo_SEnc.SingleInterfaceLayer = 0
pD_1800_ad4fd8_ANN_climo_SEnc.InterfaceLayerIndex = 0

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on pD_1800_ad4fd8_ANN_climo_SEnc
pD_1800_ad4fd8_ANN_climo_SEnc.ConnectivityFileName = '/Users/wanh895/Desktop/vis/ParaView/ne30np4_latlon.nc'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
pD_1800_ad4fd8_ANN_climo_SEncDisplay = Show(pD_1800_ad4fd8_ANN_climo_SEnc, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Selection = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Representation = 'Surface'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ColorArrayName = [None, '']
pD_1800_ad4fd8_ANN_climo_SEncDisplay.LookupTable = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay.MapScalars = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.MultiComponentsMapping = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.InterpolateScalarsBeforeMapping = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Opacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PointSize = 2.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.LineWidth = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.RenderLinesAsTubes = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.RenderPointsAsSpheres = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Interpolation = 'Gouraud'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Specular = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SpecularColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SpecularPower = 100.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Luminosity = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Ambient = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Diffuse = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Roughness = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Metallic = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.EdgeTint = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Anisotropy = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.AnisotropyRotation = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.BaseIOR = 1.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay.CoatStrength = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.CoatIOR = 2.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.CoatRoughness = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.CoatColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectTCoordArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectNormalArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectTangentArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Texture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay.RepeatTextures = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.InterpolateTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SeamlessU = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SeamlessV = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.UseMipmapTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ShowTexturesOnBackface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.BaseColorTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay.NormalTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay.NormalScale = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.CoatNormalTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay.CoatNormalScale = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.MaterialTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OcclusionStrength = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.AnisotropyTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay.EmissiveTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.FlipTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.BackfaceRepresentation = 'Follow Frontface'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.BackfaceOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Position = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Scale = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Orientation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Origin = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Pickable = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Triangulate = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.UseShaderReplacements = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ShaderReplacements = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.NonlinearSubdivisionLevel = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.UseDataPartitions = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OSPRayUseScaleArray = 'All Approximate'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OSPRayScaleArray = 'ANRAIN'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OSPRayMaterial = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.BlockSelectors = ['/']
pD_1800_ad4fd8_ANN_climo_SEncDisplay.BlockColors = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay.BlockOpacities = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Orient = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OrientationMode = 'Direction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectOrientationVectors = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Scaling = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ScaleMode = 'No Data Scaling Off'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ScaleFactor = 36.00000000000003
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectScaleArray = 'ANRAIN'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.GlyphType = 'Arrow'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.UseGlyphTable = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.GlyphTableIndexArray = 'ANRAIN'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.UseCompositeGlyphTable = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.UseGlyphCullingAndLOD = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.LODValues = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ColorByLODIndex = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.GaussianRadius = 1.8000000000000014
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ShaderPreset = 'Sphere'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.CustomTriangleScale = 3
pD_1800_ad4fd8_ANN_climo_SEncDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
pD_1800_ad4fd8_ANN_climo_SEncDisplay.Emissive = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ScaleByArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SetScaleArray = ['POINTS', 'ANRAIN']
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ScaleArrayComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.UseScaleFunction = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OpacityByArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OpacityArray = ['POINTS', 'ANRAIN']
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OpacityArrayComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid = 'GridAxesRepresentation'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionCellLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionCellLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionCellLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionCellLabelFontSize = 18
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionCellLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionCellLabelJustification = 'Left'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionCellLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionCellLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionPointLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionPointLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionPointLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionPointLabelFontSize = 18
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionPointLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionPointLabelJustification = 'Left'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionPointLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectionPointLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes = 'PolarAxesRepresentation'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ScalarOpacityFunction = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ScalarOpacityUnitDistance = 3.599181859937947
pD_1800_ad4fd8_ANN_climo_SEncDisplay.UseSeparateOpacityArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OpacityArrayName = ['POINTS', 'ANRAIN']
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OpacityComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectMapper = 'Projected tetra'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SamplingDimensions = [128, 128, 128]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.UseFloatingPointFrameBuffer = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SelectInputVectors = [None, '']
pD_1800_ad4fd8_ANN_climo_SEncDisplay.NumberOfSteps = 40
pD_1800_ad4fd8_ANN_climo_SEncDisplay.StepSize = 0.25
pD_1800_ad4fd8_ANN_climo_SEncDisplay.NormalizeVectors = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.EnhancedLIC = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ColorMode = 'Blend'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.LICIntensity = 0.8
pD_1800_ad4fd8_ANN_climo_SEncDisplay.MapModeBias = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.EnhanceContrast = 'Off'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.LowLICContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.HighLICContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.LowColorContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.HighColorContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.AntiAlias = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.MaskOnSurface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.MaskThreshold = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.MaskIntensity = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.MaskColor = [0.5, 0.5, 0.5]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.GenerateNoiseTexture = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.NoiseType = 'Gaussian'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.NoiseTextureSize = 128
pD_1800_ad4fd8_ANN_climo_SEncDisplay.NoiseGrainSize = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay.MinNoiseValue = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.MaxNoiseValue = 0.8
pD_1800_ad4fd8_ANN_climo_SEncDisplay.NumberOfNoiseLevels = 1024
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ImpulseNoiseProbability = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ImpulseNoiseBackgroundValue = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.NoiseGeneratorSeed = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.CompositeStrategy = 'AUTO'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.UseLICForLOD = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.GlyphType.TipResolution = 6
pD_1800_ad4fd8_ANN_climo_SEncDisplay.GlyphType.TipRadius = 0.1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.GlyphType.TipLength = 0.35
pD_1800_ad4fd8_ANN_climo_SEncDisplay.GlyphType.ShaftResolution = 6
pD_1800_ad4fd8_ANN_climo_SEncDisplay.GlyphType.ShaftRadius = 0.03
pD_1800_ad4fd8_ANN_climo_SEncDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 81995.0234375, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 81995.0234375, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XTitle = 'X Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YTitle = 'Y Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZTitle = 'Z Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.FacesToRender = 63
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.CullBackface = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.CullFrontface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ShowGrid = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ShowEdges = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ShowTicks = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.AxesToLabel = 63
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.XAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.YAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.ZAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.UseCustomBounds = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.Visibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.EnableCustomRange = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.CustomRange = [0.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.RadialAxesVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.DrawRadialGridlines = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarArcsVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.DrawPolarArcsGridlines = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.NumberOfRadialAxes = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.AutoSubdividePolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.NumberOfPolarAxis = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.MinimumRadius = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.MinimumAngle = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.MaximumAngle = 90.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.Ratio = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTitleVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarLabelVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.RadialLabelVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.RadialUnitsVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.ScreenSize = 10.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisTextBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisTextItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisTextShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.EnableDistanceLOD = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.DistanceLODThreshold = 0.7
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.EnableViewAngleLOD = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarTicksVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.TickLocation = 'Both'
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.AxisTickVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.AxisMinorTickVisibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.ArcTickVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.ArcMinorTickVisibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.DeltaAngleMajor = 10.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.DeltaAngleMinor = 5.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.ArcMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.ArcTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.ArcMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.ArcTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.Use2DMode = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.UseCache = 0
renderView2.ViewSize = [400, 400]
renderView2.UseInteractiveRenderingForScreenshots = 0
renderView2.InteractionMode = '3D'
renderView2.CollectGeometryThreshold = 100.0
renderView2.SuppressRendering = 0
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterAxesVisibility = 0
renderView2.OrientationAxesVisibility = 1
renderView2.OrientationAxesInteractivity = 0
renderView2.CenterOfRotation = [0.0, 0.0, 0.0]
renderView2.RotationFactor = 1.0
renderView2.EnableRenderOnInteraction = 1
renderView2.UseLight = 1
renderView2.KeyLightWarmth = 0.6
renderView2.KeyLightIntensity = 0.75
renderView2.KeyLightElevation = 50.0
renderView2.KeyLightAzimuth = 10.0
renderView2.FillLightWarmth = 0.4
renderView2.FillLightKFRatio = 3.0
renderView2.FillLightElevation = -75.0
renderView2.FillLightAzimuth = -10.0
renderView2.BackLightWarmth = 0.5
renderView2.BackLightKBRatio = 3.5
renderView2.BackLightElevation = 0.0
renderView2.BackLightAzimuth = 110.0
renderView2.HeadLightWarmth = 0.5
renderView2.HeadLightKHRatio = 3.0
renderView2.MaintainLuminance = 0
renderView2.HiddenLineRemoval = 0
renderView2.UseToneMapping = 0
renderView2.Exposure = 1.0
renderView2.UseAmbientOcclusion = 0
renderView2.StereoRender = 0
renderView2.StereoType = 'Crystal Eyes'
renderView2.ServerStereoType = 'Same As Client'
renderView2.MultiSamples = 0
renderView2.AlphaBitPlanes = 1
renderView2.StencilCapable = 1
renderView2.CameraPosition = [0.0, 0.0, 6.69]
renderView2.CameraFocalPoint = [0.0, 0.0, 0.0]
renderView2.CameraViewUp = [0.0, 1.0, 0.0]
renderView2.CameraViewAngle = 30.0
renderView2.CameraFocalDisk = 1.0
renderView2.CameraFocalDistance = 0.0
renderView2.CameraParallelScale = 1.73
renderView2.EyeAngle = 2.0
renderView2.CameraParallelProjection = 0
renderView2.UseColorPaletteForBackground = 1
renderView2.BackgroundColorMode = 'Single Color'
renderView2.BackgroundTexture = None
renderView2.Background2 = [0.0, 0.0, 0.165]
renderView2.Background = [0.329, 0.349, 0.427]
renderView2.UseEnvironmentLighting = 0
renderView2.MaxClipBounds = [0.0, -1.0, 0.0, -1.0, 0.0, -1.0]
renderView2.LockBounds = 0
renderView2.EnableRayTracing = 0
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.Shadows = 0
renderView2.AmbientSamples = 0
renderView2.SamplesPerPixel = 1
renderView2.ProgressivePasses = 1
renderView2.RouletteDepth = 5
renderView2.VolumeAnisotropy = 0.0
renderView2.Denoise = 1
renderView2.LightScale = 1.0
renderView2.TemporalCacheSize = 0
renderView2.Backgroundmode = 'Environment'
renderView2.EnvironmentNorth = [0.0, 1.0, 0.0]
renderView2.EnvironmentEast = [1.0, 0.0, 0.0]
renderView2.EnvironmentalBG = [0.329, 0.349, 0.427]
renderView2.EnvironmentalBG2 = [0.0, 0.0, 0.165]
renderView2.UseGradientEnvironmentalBG = 0
renderView2.UseTexturedEnvironmentalBG = 0
renderView2.EnvironmentalBGTexture = None
renderView2.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.Visibility = 0
renderView2.AxesGrid.XTitle = 'X Axis'
renderView2.AxesGrid.YTitle = 'Y Axis'
renderView2.AxesGrid.ZTitle = 'Z Axis'
renderView2.AxesGrid.XTitleOpacity = 1.0
renderView2.AxesGrid.XTitleFontFamily = 'Arial'
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.XTitleBold = 0
renderView2.AxesGrid.XTitleItalic = 0
renderView2.AxesGrid.XTitleShadow = 0
renderView2.AxesGrid.XTitleFontSize = 12
renderView2.AxesGrid.YTitleOpacity = 1.0
renderView2.AxesGrid.YTitleFontFamily = 'Arial'
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.YTitleBold = 0
renderView2.AxesGrid.YTitleItalic = 0
renderView2.AxesGrid.YTitleShadow = 0
renderView2.AxesGrid.YTitleFontSize = 12
renderView2.AxesGrid.ZTitleOpacity = 1.0
renderView2.AxesGrid.ZTitleFontFamily = 'Arial'
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.ZTitleBold = 0
renderView2.AxesGrid.ZTitleItalic = 0
renderView2.AxesGrid.ZTitleShadow = 0
renderView2.AxesGrid.ZTitleFontSize = 12
renderView2.AxesGrid.FacesToRender = 63
renderView2.AxesGrid.CullBackface = 0
renderView2.AxesGrid.CullFrontface = 1
renderView2.AxesGrid.ShowGrid = 0
renderView2.AxesGrid.ShowEdges = 1
renderView2.AxesGrid.ShowTicks = 1
renderView2.AxesGrid.AxesToLabel = 63
renderView2.AxesGrid.LabelUniqueEdgesOnly = 1
renderView2.AxesGrid.XLabelOpacity = 1.0
renderView2.AxesGrid.XLabelFontFamily = 'Arial'
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.XLabelBold = 0
renderView2.AxesGrid.XLabelItalic = 0
renderView2.AxesGrid.XLabelShadow = 0
renderView2.AxesGrid.XLabelFontSize = 12
renderView2.AxesGrid.YLabelOpacity = 1.0
renderView2.AxesGrid.YLabelFontFamily = 'Arial'
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.YLabelBold = 0
renderView2.AxesGrid.YLabelItalic = 0
renderView2.AxesGrid.YLabelShadow = 0
renderView2.AxesGrid.YLabelFontSize = 12
renderView2.AxesGrid.ZLabelOpacity = 1.0
renderView2.AxesGrid.ZLabelFontFamily = 'Arial'
renderView2.AxesGrid.ZLabelFontFile = ''
renderView2.AxesGrid.ZLabelBold = 0
renderView2.AxesGrid.ZLabelItalic = 0
renderView2.AxesGrid.ZLabelShadow = 0
renderView2.AxesGrid.ZLabelFontSize = 12
renderView2.AxesGrid.XAxisNotation = 'Mixed'
renderView2.AxesGrid.XAxisPrecision = 2
renderView2.AxesGrid.XAxisUseCustomLabels = 0
renderView2.AxesGrid.XAxisLabels = []
renderView2.AxesGrid.YAxisNotation = 'Mixed'
renderView2.AxesGrid.YAxisPrecision = 2
renderView2.AxesGrid.YAxisUseCustomLabels = 0
renderView2.AxesGrid.YAxisLabels = []
renderView2.AxesGrid.ZAxisNotation = 'Mixed'
renderView2.AxesGrid.ZAxisPrecision = 2
renderView2.AxesGrid.ZAxisUseCustomLabels = 0
renderView2.AxesGrid.ZAxisLabels = []
renderView2.AxesGrid.UseCustomBounds = 0
renderView2.AxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
renderView2.AxesGrid.DataScale = [1.0, 1.0, 1.0]
renderView2.AxesGrid.DataPosition = [0.0, 0.0, 0.0]
renderView2.AxesGrid.DataBoundsScaleFactor = 1.0008
renderView2.AxesGrid.ModelTransformMatrix = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
renderView2.AxesGrid.ModelBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
renderView2.AxesGrid.UseModelTransform = 0

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView2, layout=layout1, hint=2)

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.UseCache = 0
renderView3.ViewSize = [400, 400]
renderView3.UseInteractiveRenderingForScreenshots = 0
renderView3.InteractionMode = '3D'
renderView3.CollectGeometryThreshold = 100.0
renderView3.SuppressRendering = 0
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.CenterAxesVisibility = 0
renderView3.OrientationAxesVisibility = 1
renderView3.OrientationAxesInteractivity = 0
renderView3.CenterOfRotation = [0.0, 0.0, 0.0]
renderView3.RotationFactor = 1.0
renderView3.EnableRenderOnInteraction = 1
renderView3.UseLight = 1
renderView3.KeyLightWarmth = 0.6
renderView3.KeyLightIntensity = 0.75
renderView3.KeyLightElevation = 50.0
renderView3.KeyLightAzimuth = 10.0
renderView3.FillLightWarmth = 0.4
renderView3.FillLightKFRatio = 3.0
renderView3.FillLightElevation = -75.0
renderView3.FillLightAzimuth = -10.0
renderView3.BackLightWarmth = 0.5
renderView3.BackLightKBRatio = 3.5
renderView3.BackLightElevation = 0.0
renderView3.BackLightAzimuth = 110.0
renderView3.HeadLightWarmth = 0.5
renderView3.HeadLightKHRatio = 3.0
renderView3.MaintainLuminance = 0
renderView3.HiddenLineRemoval = 0
renderView3.UseToneMapping = 0
renderView3.Exposure = 1.0
renderView3.UseAmbientOcclusion = 0
renderView3.StereoRender = 0
renderView3.StereoType = 'Crystal Eyes'
renderView3.ServerStereoType = 'Same As Client'
renderView3.MultiSamples = 0
renderView3.AlphaBitPlanes = 1
renderView3.StencilCapable = 1
renderView3.CameraPosition = [0.0, 0.0, 6.69]
renderView3.CameraFocalPoint = [0.0, 0.0, 0.0]
renderView3.CameraViewUp = [0.0, 1.0, 0.0]
renderView3.CameraViewAngle = 30.0
renderView3.CameraFocalDisk = 1.0
renderView3.CameraFocalDistance = 0.0
renderView3.CameraParallelScale = 1.73
renderView3.EyeAngle = 2.0
renderView3.CameraParallelProjection = 0
renderView3.UseColorPaletteForBackground = 1
renderView3.BackgroundColorMode = 'Single Color'
renderView3.BackgroundTexture = None
renderView3.Background2 = [0.0, 0.0, 0.165]
renderView3.Background = [0.329, 0.349, 0.427]
renderView3.UseEnvironmentLighting = 0
renderView3.MaxClipBounds = [0.0, -1.0, 0.0, -1.0, 0.0, -1.0]
renderView3.LockBounds = 0
renderView3.EnableRayTracing = 0
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.Shadows = 0
renderView3.AmbientSamples = 0
renderView3.SamplesPerPixel = 1
renderView3.ProgressivePasses = 1
renderView3.RouletteDepth = 5
renderView3.VolumeAnisotropy = 0.0
renderView3.Denoise = 1
renderView3.LightScale = 1.0
renderView3.TemporalCacheSize = 0
renderView3.Backgroundmode = 'Environment'
renderView3.EnvironmentNorth = [0.0, 1.0, 0.0]
renderView3.EnvironmentEast = [1.0, 0.0, 0.0]
renderView3.EnvironmentalBG = [0.329, 0.349, 0.427]
renderView3.EnvironmentalBG2 = [0.0, 0.0, 0.165]
renderView3.UseGradientEnvironmentalBG = 0
renderView3.UseTexturedEnvironmentalBG = 0
renderView3.EnvironmentalBGTexture = None
renderView3.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView3.AxesGrid.Visibility = 0
renderView3.AxesGrid.XTitle = 'X Axis'
renderView3.AxesGrid.YTitle = 'Y Axis'
renderView3.AxesGrid.ZTitle = 'Z Axis'
renderView3.AxesGrid.XTitleOpacity = 1.0
renderView3.AxesGrid.XTitleFontFamily = 'Arial'
renderView3.AxesGrid.XTitleFontFile = ''
renderView3.AxesGrid.XTitleBold = 0
renderView3.AxesGrid.XTitleItalic = 0
renderView3.AxesGrid.XTitleShadow = 0
renderView3.AxesGrid.XTitleFontSize = 12
renderView3.AxesGrid.YTitleOpacity = 1.0
renderView3.AxesGrid.YTitleFontFamily = 'Arial'
renderView3.AxesGrid.YTitleFontFile = ''
renderView3.AxesGrid.YTitleBold = 0
renderView3.AxesGrid.YTitleItalic = 0
renderView3.AxesGrid.YTitleShadow = 0
renderView3.AxesGrid.YTitleFontSize = 12
renderView3.AxesGrid.ZTitleOpacity = 1.0
renderView3.AxesGrid.ZTitleFontFamily = 'Arial'
renderView3.AxesGrid.ZTitleFontFile = ''
renderView3.AxesGrid.ZTitleBold = 0
renderView3.AxesGrid.ZTitleItalic = 0
renderView3.AxesGrid.ZTitleShadow = 0
renderView3.AxesGrid.ZTitleFontSize = 12
renderView3.AxesGrid.FacesToRender = 63
renderView3.AxesGrid.CullBackface = 0
renderView3.AxesGrid.CullFrontface = 1
renderView3.AxesGrid.ShowGrid = 0
renderView3.AxesGrid.ShowEdges = 1
renderView3.AxesGrid.ShowTicks = 1
renderView3.AxesGrid.AxesToLabel = 63
renderView3.AxesGrid.LabelUniqueEdgesOnly = 1
renderView3.AxesGrid.XLabelOpacity = 1.0
renderView3.AxesGrid.XLabelFontFamily = 'Arial'
renderView3.AxesGrid.XLabelFontFile = ''
renderView3.AxesGrid.XLabelBold = 0
renderView3.AxesGrid.XLabelItalic = 0
renderView3.AxesGrid.XLabelShadow = 0
renderView3.AxesGrid.XLabelFontSize = 12
renderView3.AxesGrid.YLabelOpacity = 1.0
renderView3.AxesGrid.YLabelFontFamily = 'Arial'
renderView3.AxesGrid.YLabelFontFile = ''
renderView3.AxesGrid.YLabelBold = 0
renderView3.AxesGrid.YLabelItalic = 0
renderView3.AxesGrid.YLabelShadow = 0
renderView3.AxesGrid.YLabelFontSize = 12
renderView3.AxesGrid.ZLabelOpacity = 1.0
renderView3.AxesGrid.ZLabelFontFamily = 'Arial'
renderView3.AxesGrid.ZLabelFontFile = ''
renderView3.AxesGrid.ZLabelBold = 0
renderView3.AxesGrid.ZLabelItalic = 0
renderView3.AxesGrid.ZLabelShadow = 0
renderView3.AxesGrid.ZLabelFontSize = 12
renderView3.AxesGrid.XAxisNotation = 'Mixed'
renderView3.AxesGrid.XAxisPrecision = 2
renderView3.AxesGrid.XAxisUseCustomLabels = 0
renderView3.AxesGrid.XAxisLabels = []
renderView3.AxesGrid.YAxisNotation = 'Mixed'
renderView3.AxesGrid.YAxisPrecision = 2
renderView3.AxesGrid.YAxisUseCustomLabels = 0
renderView3.AxesGrid.YAxisLabels = []
renderView3.AxesGrid.ZAxisNotation = 'Mixed'
renderView3.AxesGrid.ZAxisPrecision = 2
renderView3.AxesGrid.ZAxisUseCustomLabels = 0
renderView3.AxesGrid.ZAxisLabels = []
renderView3.AxesGrid.UseCustomBounds = 0
renderView3.AxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
renderView3.AxesGrid.DataScale = [1.0, 1.0, 1.0]
renderView3.AxesGrid.DataPosition = [0.0, 0.0, 0.0]
renderView3.AxesGrid.DataBoundsScaleFactor = 1.0008
renderView3.AxesGrid.ModelTransformMatrix = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
renderView3.AxesGrid.ModelBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
renderView3.AxesGrid.UseModelTransform = 0

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView3, layout=layout1, hint=6)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# split cell
layout1.SplitVertical(5, 0.5)

# set active view
SetActiveView(None)

# close an empty frame
layout1.Collapse(12)

# set active view
SetActiveView(renderView2)

# set active view
SetActiveView(renderView1)

# split cell
layout1.SplitVertical(1, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.UseCache = 0
renderView4.ViewSize = [400, 400]
renderView4.UseInteractiveRenderingForScreenshots = 0
renderView4.InteractionMode = '3D'
renderView4.CollectGeometryThreshold = 100.0
renderView4.SuppressRendering = 0
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.CenterAxesVisibility = 0
renderView4.OrientationAxesVisibility = 1
renderView4.OrientationAxesInteractivity = 0
renderView4.CenterOfRotation = [0.0, 0.0, 0.0]
renderView4.RotationFactor = 1.0
renderView4.EnableRenderOnInteraction = 1
renderView4.UseLight = 1
renderView4.KeyLightWarmth = 0.6
renderView4.KeyLightIntensity = 0.75
renderView4.KeyLightElevation = 50.0
renderView4.KeyLightAzimuth = 10.0
renderView4.FillLightWarmth = 0.4
renderView4.FillLightKFRatio = 3.0
renderView4.FillLightElevation = -75.0
renderView4.FillLightAzimuth = -10.0
renderView4.BackLightWarmth = 0.5
renderView4.BackLightKBRatio = 3.5
renderView4.BackLightElevation = 0.0
renderView4.BackLightAzimuth = 110.0
renderView4.HeadLightWarmth = 0.5
renderView4.HeadLightKHRatio = 3.0
renderView4.MaintainLuminance = 0
renderView4.HiddenLineRemoval = 0
renderView4.UseToneMapping = 0
renderView4.Exposure = 1.0
renderView4.UseAmbientOcclusion = 0
renderView4.StereoRender = 0
renderView4.StereoType = 'Crystal Eyes'
renderView4.ServerStereoType = 'Same As Client'
renderView4.MultiSamples = 0
renderView4.AlphaBitPlanes = 1
renderView4.StencilCapable = 1
renderView4.CameraPosition = [0.0, 0.0, 6.69]
renderView4.CameraFocalPoint = [0.0, 0.0, 0.0]
renderView4.CameraViewUp = [0.0, 1.0, 0.0]
renderView4.CameraViewAngle = 30.0
renderView4.CameraFocalDisk = 1.0
renderView4.CameraFocalDistance = 0.0
renderView4.CameraParallelScale = 1.73
renderView4.EyeAngle = 2.0
renderView4.CameraParallelProjection = 0
renderView4.UseColorPaletteForBackground = 1
renderView4.BackgroundColorMode = 'Single Color'
renderView4.BackgroundTexture = None
renderView4.Background2 = [0.0, 0.0, 0.165]
renderView4.Background = [0.329, 0.349, 0.427]
renderView4.UseEnvironmentLighting = 0
renderView4.MaxClipBounds = [0.0, -1.0, 0.0, -1.0, 0.0, -1.0]
renderView4.LockBounds = 0
renderView4.EnableRayTracing = 0
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.Shadows = 0
renderView4.AmbientSamples = 0
renderView4.SamplesPerPixel = 1
renderView4.ProgressivePasses = 1
renderView4.RouletteDepth = 5
renderView4.VolumeAnisotropy = 0.0
renderView4.Denoise = 1
renderView4.LightScale = 1.0
renderView4.TemporalCacheSize = 0
renderView4.Backgroundmode = 'Environment'
renderView4.EnvironmentNorth = [0.0, 1.0, 0.0]
renderView4.EnvironmentEast = [1.0, 0.0, 0.0]
renderView4.EnvironmentalBG = [0.329, 0.349, 0.427]
renderView4.EnvironmentalBG2 = [0.0, 0.0, 0.165]
renderView4.UseGradientEnvironmentalBG = 0
renderView4.UseTexturedEnvironmentalBG = 0
renderView4.EnvironmentalBGTexture = None
renderView4.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView4.AxesGrid.Visibility = 0
renderView4.AxesGrid.XTitle = 'X Axis'
renderView4.AxesGrid.YTitle = 'Y Axis'
renderView4.AxesGrid.ZTitle = 'Z Axis'
renderView4.AxesGrid.XTitleOpacity = 1.0
renderView4.AxesGrid.XTitleFontFamily = 'Arial'
renderView4.AxesGrid.XTitleFontFile = ''
renderView4.AxesGrid.XTitleBold = 0
renderView4.AxesGrid.XTitleItalic = 0
renderView4.AxesGrid.XTitleShadow = 0
renderView4.AxesGrid.XTitleFontSize = 12
renderView4.AxesGrid.YTitleOpacity = 1.0
renderView4.AxesGrid.YTitleFontFamily = 'Arial'
renderView4.AxesGrid.YTitleFontFile = ''
renderView4.AxesGrid.YTitleBold = 0
renderView4.AxesGrid.YTitleItalic = 0
renderView4.AxesGrid.YTitleShadow = 0
renderView4.AxesGrid.YTitleFontSize = 12
renderView4.AxesGrid.ZTitleOpacity = 1.0
renderView4.AxesGrid.ZTitleFontFamily = 'Arial'
renderView4.AxesGrid.ZTitleFontFile = ''
renderView4.AxesGrid.ZTitleBold = 0
renderView4.AxesGrid.ZTitleItalic = 0
renderView4.AxesGrid.ZTitleShadow = 0
renderView4.AxesGrid.ZTitleFontSize = 12
renderView4.AxesGrid.FacesToRender = 63
renderView4.AxesGrid.CullBackface = 0
renderView4.AxesGrid.CullFrontface = 1
renderView4.AxesGrid.ShowGrid = 0
renderView4.AxesGrid.ShowEdges = 1
renderView4.AxesGrid.ShowTicks = 1
renderView4.AxesGrid.AxesToLabel = 63
renderView4.AxesGrid.LabelUniqueEdgesOnly = 1
renderView4.AxesGrid.XLabelOpacity = 1.0
renderView4.AxesGrid.XLabelFontFamily = 'Arial'
renderView4.AxesGrid.XLabelFontFile = ''
renderView4.AxesGrid.XLabelBold = 0
renderView4.AxesGrid.XLabelItalic = 0
renderView4.AxesGrid.XLabelShadow = 0
renderView4.AxesGrid.XLabelFontSize = 12
renderView4.AxesGrid.YLabelOpacity = 1.0
renderView4.AxesGrid.YLabelFontFamily = 'Arial'
renderView4.AxesGrid.YLabelFontFile = ''
renderView4.AxesGrid.YLabelBold = 0
renderView4.AxesGrid.YLabelItalic = 0
renderView4.AxesGrid.YLabelShadow = 0
renderView4.AxesGrid.YLabelFontSize = 12
renderView4.AxesGrid.ZLabelOpacity = 1.0
renderView4.AxesGrid.ZLabelFontFamily = 'Arial'
renderView4.AxesGrid.ZLabelFontFile = ''
renderView4.AxesGrid.ZLabelBold = 0
renderView4.AxesGrid.ZLabelItalic = 0
renderView4.AxesGrid.ZLabelShadow = 0
renderView4.AxesGrid.ZLabelFontSize = 12
renderView4.AxesGrid.XAxisNotation = 'Mixed'
renderView4.AxesGrid.XAxisPrecision = 2
renderView4.AxesGrid.XAxisUseCustomLabels = 0
renderView4.AxesGrid.XAxisLabels = []
renderView4.AxesGrid.YAxisNotation = 'Mixed'
renderView4.AxesGrid.YAxisPrecision = 2
renderView4.AxesGrid.YAxisUseCustomLabels = 0
renderView4.AxesGrid.YAxisLabels = []
renderView4.AxesGrid.ZAxisNotation = 'Mixed'
renderView4.AxesGrid.ZAxisPrecision = 2
renderView4.AxesGrid.ZAxisUseCustomLabels = 0
renderView4.AxesGrid.ZAxisLabels = []
renderView4.AxesGrid.UseCustomBounds = 0
renderView4.AxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
renderView4.AxesGrid.DataScale = [1.0, 1.0, 1.0]
renderView4.AxesGrid.DataPosition = [0.0, 0.0, 0.0]
renderView4.AxesGrid.DataBoundsScaleFactor = 1.0008
renderView4.AxesGrid.ModelTransformMatrix = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
renderView4.AxesGrid.ModelBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
renderView4.AxesGrid.UseModelTransform = 0

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView4, layout=layout1, hint=4)

# set active view
SetActiveView(renderView1)

# Properties modified on pD_1800_ad4fd8_ANN_climo_SEnc
pD_1800_ad4fd8_ANN_climo_SEnc.VerticalDimension = 'Single layer [time, ncol]'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView3.Update()

# set scalar coloring
ColorBy(pD_1800_ad4fd8_ANN_climo_SEncDisplay, ('POINTS', 'PHIS'))

# rescale color and/or opacity maps used to include current data range
pD_1800_ad4fd8_ANN_climo_SEncDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
pD_1800_ad4fd8_ANN_climo_SEncDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'PHIS'
pHISLUT = GetColorTransferFunction('PHIS')

# get opacity transfer function/opacity map for 'PHIS'
pHISPWF = GetOpacityTransferFunction('PHIS')

# get 2D transfer function for 'PHIS'
pHISTF2D = GetTransferFunction2D('PHIS')

# get color legend/bar for pHISLUT in view renderView1
pHISLUTColorBar = GetScalarBar(pHISLUT, renderView1)

# change scalar bar placement
pHISLUTColorBar.Orientation = 'Horizontal'
pHISLUTColorBar.WindowLocation = 'Any Location'
pHISLUTColorBar.Position = [0.337693661971831, 0.0]
pHISLUTColorBar.ScalarBarLength = 0.33

# reset view to fit data
renderView1.ResetCamera(True)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(pD_1800_ad4fd8_ANN_climo_SEnc)

# show data in view
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1 = Show(pD_1800_ad4fd8_ANN_climo_SEnc, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Selection = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Representation = 'Surface'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ColorArrayName = [None, '']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.LookupTable = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.MapScalars = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.MultiComponentsMapping = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.InterpolateScalarsBeforeMapping = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Opacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PointSize = 2.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.LineWidth = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.RenderLinesAsTubes = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.RenderPointsAsSpheres = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Interpolation = 'Gouraud'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Specular = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SpecularColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SpecularPower = 100.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Luminosity = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Ambient = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Diffuse = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Roughness = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Metallic = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.EdgeTint = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Anisotropy = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.AnisotropyRotation = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.BaseIOR = 1.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.CoatStrength = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.CoatIOR = 2.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.CoatRoughness = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.CoatColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectTCoordArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectNormalArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectTangentArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Texture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.RepeatTextures = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.InterpolateTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SeamlessU = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SeamlessV = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.UseMipmapTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ShowTexturesOnBackface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.BaseColorTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.NormalTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.NormalScale = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.CoatNormalTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.CoatNormalScale = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.MaterialTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OcclusionStrength = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.AnisotropyTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.EmissiveTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.EmissiveFactor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.FlipTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.BackfaceRepresentation = 'Follow Frontface'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.BackfaceAmbientColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.BackfaceOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Position = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Scale = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Orientation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Origin = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Pickable = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Triangulate = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.UseShaderReplacements = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ShaderReplacements = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.NonlinearSubdivisionLevel = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.UseDataPartitions = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OSPRayUseScaleArray = 'All Approximate'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OSPRayScaleArray = 'AEROD_v'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OSPRayMaterial = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.BlockSelectors = ['/']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.BlockColors = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.BlockOpacities = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Orient = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OrientationMode = 'Direction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectOrientationVectors = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Scaling = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ScaleMode = 'No Data Scaling Off'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ScaleFactor = 36.00000000000003
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectScaleArray = 'AEROD_v'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.GlyphType = 'Arrow'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.UseGlyphTable = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.GlyphTableIndexArray = 'AEROD_v'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.UseCompositeGlyphTable = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.UseGlyphCullingAndLOD = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.LODValues = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ColorByLODIndex = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.GaussianRadius = 1.8000000000000014
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ShaderPreset = 'Sphere'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.CustomTriangleScale = 3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.Emissive = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ScaleByArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SetScaleArray = ['POINTS', 'AEROD_v']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ScaleArrayComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.UseScaleFunction = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OpacityByArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OpacityArray = ['POINTS', 'AEROD_v']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OpacityArrayComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionCellLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionCellLabelColor = [0.0, 1.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionCellLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionCellLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionCellLabelFontSize = 18
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionCellLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionCellLabelJustification = 'Left'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionCellLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionCellLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionPointLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionPointLabelColor = [1.0, 1.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionPointLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionPointLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionPointLabelFontSize = 18
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionPointLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionPointLabelJustification = 'Left'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionPointLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectionPointLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes = 'PolarAxesRepresentation'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ScalarOpacityFunction = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ScalarOpacityUnitDistance = 11.029235690267397
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.UseSeparateOpacityArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OpacityArrayName = ['POINTS', 'AEROD_v']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OpacityComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectMapper = 'Projected tetra'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SamplingDimensions = [128, 128, 128]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.UseFloatingPointFrameBuffer = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SelectInputVectors = [None, '']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.NumberOfSteps = 40
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.StepSize = 0.25
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.NormalizeVectors = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.EnhancedLIC = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ColorMode = 'Blend'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.LICIntensity = 0.8
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.MapModeBias = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.EnhanceContrast = 'Off'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.LowLICContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.HighLICContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.LowColorContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.HighColorContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.AntiAlias = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.MaskOnSurface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.MaskThreshold = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.MaskIntensity = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.MaskColor = [0.5, 0.5, 0.5]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.GenerateNoiseTexture = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.NoiseType = 'Gaussian'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.NoiseTextureSize = 128
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.NoiseGrainSize = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.MinNoiseValue = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.MaxNoiseValue = 0.8
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.NumberOfNoiseLevels = 1024
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ImpulseNoiseProbability = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ImpulseNoiseBackgroundValue = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.NoiseGeneratorSeed = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.CompositeStrategy = 'AUTO'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.UseLICForLOD = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.GlyphType.TipResolution = 6
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.GlyphType.TipRadius = 0.1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.GlyphType.TipLength = 0.35
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.GlyphType.ShaftResolution = 6
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.GlyphType.ShaftRadius = 0.03
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ScaleTransferFunction.Points = [0.0019428791711106896, 0.0, 0.5, 0.0, 1.6548664569854736, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OpacityTransferFunction.Points = [0.0019428791711106896, 0.0, 0.5, 0.0, 1.6548664569854736, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XTitle = 'X Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YTitle = 'Y Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZTitle = 'Z Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.FacesToRender = 63
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.CullBackface = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.CullFrontface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ShowGrid = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ShowEdges = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ShowTicks = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.LabelUniqueEdgesOnly = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.AxesToLabel = 63
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.XAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.YAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.ZAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.UseCustomBounds = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.Visibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.Translation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.Scale = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.Orientation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.EnableCustomBounds = [0, 0, 0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.EnableCustomRange = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.CustomRange = [0.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.RadialAxesVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.DrawRadialGridlines = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarArcsVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.DrawPolarArcsGridlines = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.NumberOfRadialAxes = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.AutoSubdividePolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.NumberOfPolarAxis = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.MinimumRadius = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.MinimumAngle = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.MaximumAngle = 90.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.RadialAxesOriginToPolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.Ratio = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTitleVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTitle = 'Radial Distance'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTitleLocation = 'Bottom'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarLabelVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarLabelFormat = '%-#6.3g'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarLabelExponentLocation = 'Labels'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.RadialLabelVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.RadialLabelFormat = '%-#3.1f'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.RadialLabelLocation = 'Bottom'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.RadialUnitsVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.ScreenSize = 10.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisTextOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisTextFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisTextBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisTextItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisTextShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisTextFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.SecondaryRadialAxesTextBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.SecondaryRadialAxesTextItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.SecondaryRadialAxesTextShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.SecondaryRadialAxesTextFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.EnableDistanceLOD = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.DistanceLODThreshold = 0.7
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.EnableViewAngleLOD = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.ViewAngleLODThreshold = 0.7
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.SmallestVisiblePolarAngle = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarTicksVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.ArcTicksOriginToPolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.TickLocation = 'Both'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.AxisTickVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.AxisMinorTickVisibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.ArcTickVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.ArcMinorTickVisibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.DeltaAngleMajor = 10.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.DeltaAngleMinor = 5.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.PolarAxisTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.ArcMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.ArcTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.ArcMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.ArcTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.Use2DMode = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.PolarAxes.UseLogAxis = 0

#changing interaction mode based on data extents
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [179.99999999999986, 0.0, 10001.0]
renderView2.CameraFocalPoint = [179.99999999999986, 0.0, 1.0]

# reset view to fit data
renderView2.ResetCamera(False)

# set scalar coloring
ColorBy(pD_1800_ad4fd8_ANN_climo_SEncDisplay_1, ('POINTS', 'CLDTOT'))

# rescale color and/or opacity maps used to include current data range
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
pD_1800_ad4fd8_ANN_climo_SEncDisplay_1.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'CLDTOT'
cLDTOTLUT = GetColorTransferFunction('CLDTOT')

# get opacity transfer function/opacity map for 'CLDTOT'
cLDTOTPWF = GetOpacityTransferFunction('CLDTOT')

# get 2D transfer function for 'CLDTOT'
cLDTOTTF2D = GetTransferFunction2D('CLDTOT')

# get color legend/bar for cLDTOTLUT in view renderView2
cLDTOTLUTColorBar = GetScalarBar(cLDTOTLUT, renderView2)

# change scalar bar placement
cLDTOTLUTColorBar.Orientation = 'Horizontal'
cLDTOTLUTColorBar.WindowLocation = 'Any Location'
cLDTOTLUTColorBar.Position = [0.35732369534555697, 0.0]
cLDTOTLUTColorBar.ScalarBarLength = 0.33000000000000007

# reset view to fit data
renderView2.ResetCamera(True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
cLDTOTLUT.ApplyPreset('X Ray', True)

# set active view
SetActiveView(renderView4)

# show data in view
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2 = Show(pD_1800_ad4fd8_ANN_climo_SEnc, renderView4, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Selection = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Representation = 'Surface'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ColorArrayName = [None, '']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.LookupTable = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.MapScalars = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.MultiComponentsMapping = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.InterpolateScalarsBeforeMapping = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Opacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PointSize = 2.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.LineWidth = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.RenderLinesAsTubes = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.RenderPointsAsSpheres = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Interpolation = 'Gouraud'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Specular = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SpecularColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SpecularPower = 100.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Luminosity = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Ambient = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Diffuse = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Roughness = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Metallic = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.EdgeTint = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Anisotropy = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.AnisotropyRotation = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.BaseIOR = 1.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.CoatStrength = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.CoatIOR = 2.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.CoatRoughness = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.CoatColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectTCoordArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectNormalArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectTangentArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Texture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.RepeatTextures = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.InterpolateTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SeamlessU = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SeamlessV = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.UseMipmapTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ShowTexturesOnBackface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.BaseColorTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.NormalTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.NormalScale = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.CoatNormalTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.CoatNormalScale = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.MaterialTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OcclusionStrength = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.AnisotropyTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.EmissiveTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.EmissiveFactor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.FlipTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.BackfaceRepresentation = 'Follow Frontface'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.BackfaceAmbientColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.BackfaceOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Position = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Scale = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Orientation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Origin = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Pickable = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Triangulate = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.UseShaderReplacements = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ShaderReplacements = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.NonlinearSubdivisionLevel = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.UseDataPartitions = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OSPRayUseScaleArray = 'All Approximate'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OSPRayScaleArray = 'AEROD_v'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OSPRayMaterial = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.BlockSelectors = ['/']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.BlockColors = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.BlockOpacities = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Orient = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OrientationMode = 'Direction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectOrientationVectors = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Scaling = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ScaleMode = 'No Data Scaling Off'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ScaleFactor = 36.00000000000003
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectScaleArray = 'AEROD_v'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.GlyphType = 'Arrow'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.UseGlyphTable = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.GlyphTableIndexArray = 'AEROD_v'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.UseCompositeGlyphTable = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.UseGlyphCullingAndLOD = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.LODValues = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ColorByLODIndex = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.GaussianRadius = 1.8000000000000014
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ShaderPreset = 'Sphere'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.CustomTriangleScale = 3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.Emissive = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ScaleByArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SetScaleArray = ['POINTS', 'AEROD_v']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ScaleArrayComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.UseScaleFunction = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OpacityByArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OpacityArray = ['POINTS', 'AEROD_v']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OpacityArrayComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionCellLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionCellLabelColor = [0.0, 1.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionCellLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionCellLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionCellLabelFontSize = 18
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionCellLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionCellLabelJustification = 'Left'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionCellLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionCellLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionPointLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionPointLabelColor = [1.0, 1.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionPointLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionPointLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionPointLabelFontSize = 18
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionPointLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionPointLabelJustification = 'Left'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionPointLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectionPointLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes = 'PolarAxesRepresentation'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ScalarOpacityFunction = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ScalarOpacityUnitDistance = 11.029235690267397
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.UseSeparateOpacityArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OpacityArrayName = ['POINTS', 'AEROD_v']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OpacityComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectMapper = 'Projected tetra'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SamplingDimensions = [128, 128, 128]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.UseFloatingPointFrameBuffer = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SelectInputVectors = [None, '']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.NumberOfSteps = 40
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.StepSize = 0.25
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.NormalizeVectors = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.EnhancedLIC = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ColorMode = 'Blend'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.LICIntensity = 0.8
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.MapModeBias = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.EnhanceContrast = 'Off'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.LowLICContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.HighLICContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.LowColorContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.HighColorContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.AntiAlias = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.MaskOnSurface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.MaskThreshold = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.MaskIntensity = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.MaskColor = [0.5, 0.5, 0.5]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.GenerateNoiseTexture = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.NoiseType = 'Gaussian'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.NoiseTextureSize = 128
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.NoiseGrainSize = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.MinNoiseValue = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.MaxNoiseValue = 0.8
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.NumberOfNoiseLevels = 1024
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ImpulseNoiseProbability = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ImpulseNoiseBackgroundValue = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.NoiseGeneratorSeed = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.CompositeStrategy = 'AUTO'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.UseLICForLOD = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.GlyphType.TipResolution = 6
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.GlyphType.TipRadius = 0.1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.GlyphType.TipLength = 0.35
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.GlyphType.ShaftResolution = 6
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.GlyphType.ShaftRadius = 0.03
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ScaleTransferFunction.Points = [0.0019428791711106896, 0.0, 0.5, 0.0, 1.6548664569854736, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OpacityTransferFunction.Points = [0.0019428791711106896, 0.0, 0.5, 0.0, 1.6548664569854736, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XTitle = 'X Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YTitle = 'Y Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZTitle = 'Z Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.FacesToRender = 63
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.CullBackface = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.CullFrontface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ShowGrid = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ShowEdges = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ShowTicks = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.LabelUniqueEdgesOnly = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.AxesToLabel = 63
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.XAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.YAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.ZAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.UseCustomBounds = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.Visibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.Translation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.Scale = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.Orientation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.EnableCustomBounds = [0, 0, 0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.EnableCustomRange = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.CustomRange = [0.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.RadialAxesVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.DrawRadialGridlines = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarArcsVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.DrawPolarArcsGridlines = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.NumberOfRadialAxes = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.AutoSubdividePolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.NumberOfPolarAxis = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.MinimumRadius = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.MinimumAngle = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.MaximumAngle = 90.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.RadialAxesOriginToPolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.Ratio = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTitleVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTitle = 'Radial Distance'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTitleLocation = 'Bottom'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarLabelVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarLabelFormat = '%-#6.3g'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarLabelExponentLocation = 'Labels'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.RadialLabelVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.RadialLabelFormat = '%-#3.1f'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.RadialLabelLocation = 'Bottom'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.RadialUnitsVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.ScreenSize = 10.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisTextOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisTextFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisTextBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisTextItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisTextShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisTextFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.SecondaryRadialAxesTextBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.SecondaryRadialAxesTextItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.SecondaryRadialAxesTextShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.SecondaryRadialAxesTextFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.EnableDistanceLOD = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.DistanceLODThreshold = 0.7
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.EnableViewAngleLOD = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.ViewAngleLODThreshold = 0.7
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.SmallestVisiblePolarAngle = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarTicksVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.ArcTicksOriginToPolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.TickLocation = 'Both'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.AxisTickVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.AxisMinorTickVisibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.ArcTickVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.ArcMinorTickVisibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.DeltaAngleMajor = 10.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.DeltaAngleMinor = 5.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.PolarAxisTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.ArcMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.ArcTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.ArcMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.ArcTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.Use2DMode = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.PolarAxes.UseLogAxis = 0

#changing interaction mode based on data extents
renderView4.InteractionMode = '2D'
renderView4.CameraPosition = [179.99999999999986, 0.0, 10001.0]
renderView4.CameraFocalPoint = [179.99999999999986, 0.0, 1.0]

# reset view to fit data
renderView4.ResetCamera(False)

# set scalar coloring
ColorBy(pD_1800_ad4fd8_ANN_climo_SEncDisplay_2, ('POINTS', 'AODDUST3'))

# rescale color and/or opacity maps used to include current data range
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
pD_1800_ad4fd8_ANN_climo_SEncDisplay_2.SetScalarBarVisibility(renderView4, True)

# get color transfer function/color map for 'AODDUST3'
aODDUST3LUT = GetColorTransferFunction('AODDUST3')

# get opacity transfer function/opacity map for 'AODDUST3'
aODDUST3PWF = GetOpacityTransferFunction('AODDUST3')

# get 2D transfer function for 'AODDUST3'
aODDUST3TF2D = GetTransferFunction2D('AODDUST3')

# reset view to fit data
renderView4.ResetCamera(True)

# get color legend/bar for aODDUST3LUT in view renderView4
aODDUST3LUTColorBar = GetScalarBar(aODDUST3LUT, renderView4)

# change scalar bar placement
aODDUST3LUTColorBar.Orientation = 'Horizontal'
aODDUST3LUTColorBar.WindowLocation = 'Any Location'
aODDUST3LUTColorBar.Position = [0.36234154929577456, 0.0]
aODDUST3LUTColorBar.ScalarBarLength = 0.32999999999999974

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
aODDUST3LUT.ApplyPreset('Viridis (matplotlib)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
aODDUST3LUT.ApplyPreset('Rainbow Desaturated', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
aODDUST3LUT.ApplyPreset('Blue Orange (divergent)', True)

# set active view
SetActiveView(renderView3)

# show data in view
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3 = Show(pD_1800_ad4fd8_ANN_climo_SEnc, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Selection = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Representation = 'Surface'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ColorArrayName = [None, '']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.LookupTable = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.MapScalars = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.MultiComponentsMapping = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.InterpolateScalarsBeforeMapping = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Opacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PointSize = 2.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.LineWidth = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.RenderLinesAsTubes = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.RenderPointsAsSpheres = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Interpolation = 'Gouraud'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Specular = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SpecularColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SpecularPower = 100.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Luminosity = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Ambient = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Diffuse = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Roughness = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Metallic = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.EdgeTint = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Anisotropy = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.AnisotropyRotation = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.BaseIOR = 1.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.CoatStrength = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.CoatIOR = 2.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.CoatRoughness = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.CoatColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectTCoordArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectNormalArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectTangentArray = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Texture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.RepeatTextures = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.InterpolateTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SeamlessU = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SeamlessV = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.UseMipmapTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ShowTexturesOnBackface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.BaseColorTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.NormalTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.NormalScale = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.CoatNormalTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.CoatNormalScale = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.MaterialTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OcclusionStrength = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.AnisotropyTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.EmissiveTexture = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.EmissiveFactor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.FlipTextures = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.BackfaceRepresentation = 'Follow Frontface'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.BackfaceAmbientColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.BackfaceOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Position = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Scale = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Orientation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Origin = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Pickable = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Triangulate = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.UseShaderReplacements = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ShaderReplacements = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.NonlinearSubdivisionLevel = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.UseDataPartitions = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OSPRayUseScaleArray = 'All Approximate'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OSPRayScaleArray = 'AEROD_v'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OSPRayMaterial = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.BlockSelectors = ['/']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.BlockColors = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.BlockOpacities = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Orient = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OrientationMode = 'Direction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectOrientationVectors = 'None'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Scaling = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ScaleMode = 'No Data Scaling Off'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ScaleFactor = 36.00000000000003
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectScaleArray = 'AEROD_v'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.GlyphType = 'Arrow'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.UseGlyphTable = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.GlyphTableIndexArray = 'AEROD_v'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.UseCompositeGlyphTable = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.UseGlyphCullingAndLOD = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.LODValues = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ColorByLODIndex = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.GaussianRadius = 1.8000000000000014
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ShaderPreset = 'Sphere'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.CustomTriangleScale = 3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.Emissive = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ScaleByArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SetScaleArray = ['POINTS', 'AEROD_v']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ScaleArrayComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.UseScaleFunction = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OpacityByArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OpacityArray = ['POINTS', 'AEROD_v']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OpacityArrayComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionCellLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionCellLabelColor = [0.0, 1.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionCellLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionCellLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionCellLabelFontSize = 18
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionCellLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionCellLabelJustification = 'Left'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionCellLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionCellLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionPointLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionPointLabelColor = [1.0, 1.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionPointLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionPointLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionPointLabelFontSize = 18
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionPointLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionPointLabelJustification = 'Left'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionPointLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectionPointLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes = 'PolarAxesRepresentation'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ScalarOpacityFunction = None
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ScalarOpacityUnitDistance = 11.029235690267397
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.UseSeparateOpacityArray = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OpacityArrayName = ['POINTS', 'AEROD_v']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OpacityComponent = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectMapper = 'Projected tetra'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SamplingDimensions = [128, 128, 128]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.UseFloatingPointFrameBuffer = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SelectInputVectors = [None, '']
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.NumberOfSteps = 40
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.StepSize = 0.25
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.NormalizeVectors = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.EnhancedLIC = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ColorMode = 'Blend'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.LICIntensity = 0.8
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.MapModeBias = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.EnhanceContrast = 'Off'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.LowLICContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.HighLICContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.LowColorContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.HighColorContrastEnhancementFactor = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.AntiAlias = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.MaskOnSurface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.MaskThreshold = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.MaskIntensity = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.MaskColor = [0.5, 0.5, 0.5]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.GenerateNoiseTexture = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.NoiseType = 'Gaussian'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.NoiseTextureSize = 128
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.NoiseGrainSize = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.MinNoiseValue = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.MaxNoiseValue = 0.8
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.NumberOfNoiseLevels = 1024
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ImpulseNoiseProbability = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ImpulseNoiseBackgroundValue = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.NoiseGeneratorSeed = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.CompositeStrategy = 'AUTO'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.UseLICForLOD = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.GlyphType.TipResolution = 6
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.GlyphType.TipRadius = 0.1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.GlyphType.TipLength = 0.35
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.GlyphType.ShaftResolution = 6
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.GlyphType.ShaftRadius = 0.03
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ScaleTransferFunction.Points = [0.0019428791711106896, 0.0, 0.5, 0.0, 1.6548664569854736, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OpacityTransferFunction.Points = [0.0019428791711106896, 0.0, 0.5, 0.0, 1.6548664569854736, 1.0, 0.5, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XTitle = 'X Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YTitle = 'Y Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZTitle = 'Z Axis'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.FacesToRender = 63
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.CullBackface = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.CullFrontface = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ShowGrid = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ShowEdges = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ShowTicks = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.LabelUniqueEdgesOnly = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.AxesToLabel = 63
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.XAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.YAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZAxisNotation = 'Mixed'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZAxisPrecision = 2
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZAxisUseCustomLabels = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.ZAxisLabels = []
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.UseCustomBounds = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.Visibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.Translation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.Scale = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.Orientation = [0.0, 0.0, 0.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.EnableCustomBounds = [0, 0, 0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.EnableCustomRange = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.CustomRange = [0.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.RadialAxesVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.DrawRadialGridlines = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarArcsVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.DrawPolarArcsGridlines = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.NumberOfRadialAxes = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.AutoSubdividePolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.NumberOfPolarAxis = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.MinimumRadius = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.MinimumAngle = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.MaximumAngle = 90.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.RadialAxesOriginToPolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.Ratio = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTitleVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTitle = 'Radial Distance'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTitleLocation = 'Bottom'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarLabelVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarLabelFormat = '%-#6.3g'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarLabelExponentLocation = 'Labels'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.RadialLabelVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.RadialLabelFormat = '%-#3.1f'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.RadialLabelLocation = 'Bottom'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.RadialUnitsVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.ScreenSize = 10.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTitleOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTitleFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTitleBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTitleItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTitleShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTitleFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisLabelOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisLabelFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisLabelBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisLabelItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisLabelShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisLabelFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisTextOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisTextFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisTextBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisTextItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisTextShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisTextFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.SecondaryRadialAxesTextFontFile = ''
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.SecondaryRadialAxesTextBold = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.SecondaryRadialAxesTextItalic = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.SecondaryRadialAxesTextShadow = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.SecondaryRadialAxesTextFontSize = 12
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.EnableDistanceLOD = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.DistanceLODThreshold = 0.7
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.EnableViewAngleLOD = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.ViewAngleLODThreshold = 0.7
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.SmallestVisiblePolarAngle = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarTicksVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.ArcTicksOriginToPolarAxis = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.TickLocation = 'Both'
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.AxisTickVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.AxisMinorTickVisibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.ArcTickVisibility = 1
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.ArcMinorTickVisibility = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.DeltaAngleMajor = 10.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.DeltaAngleMinor = 5.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.PolarAxisTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.ArcMajorTickSize = 0.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.ArcTickRatioSize = 0.3
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.ArcMajorTickThickness = 1.0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.ArcTickRatioThickness = 0.5
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.Use2DMode = 0
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.PolarAxes.UseLogAxis = 0

#changing interaction mode based on data extents
renderView3.InteractionMode = '2D'
renderView3.CameraPosition = [179.99999999999986, 0.0, 10001.0]
renderView3.CameraFocalPoint = [179.99999999999986, 0.0, 1.0]

# reset view to fit data
renderView3.ResetCamera(False)

# set scalar coloring
ColorBy(pD_1800_ad4fd8_ANN_climo_SEncDisplay_3, ('POINTS', 'LHFLX'))

# rescale color and/or opacity maps used to include current data range
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
pD_1800_ad4fd8_ANN_climo_SEncDisplay_3.SetScalarBarVisibility(renderView3, True)

# get color transfer function/color map for 'LHFLX'
lHFLXLUT = GetColorTransferFunction('LHFLX')

# get opacity transfer function/opacity map for 'LHFLX'
lHFLXPWF = GetOpacityTransferFunction('LHFLX')

# get 2D transfer function for 'LHFLX'
lHFLXTF2D = GetTransferFunction2D('LHFLX')

# reset view to fit data
renderView3.ResetCamera(True)

# get color legend/bar for lHFLXLUT in view renderView3
lHFLXLUTColorBar = GetScalarBar(lHFLXLUT, renderView3)

# change scalar bar placement
lHFLXLUTColorBar.Orientation = 'Horizontal'
lHFLXLUTColorBar.WindowLocation = 'Any Location'
lHFLXLUTColorBar.Position = [0.40034203102961907, 0.0]
lHFLXLUTColorBar.ScalarBarLength = 0.33000000000000007

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
lHFLXLUT.ApplyPreset('Inferno (matplotlib)', True)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2839, 1713)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [179.99999999999986, 0.0, 778.5552911698041]
renderView1.CameraFocalPoint = [179.99999999999986, 0.0, 1.0]
renderView1.CameraViewAngle = 17.347417840375588
renderView1.CameraParallelScale = 201.2461179749812

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [179.99999999999986, 0.0, 778.5552911698041]
renderView2.CameraFocalPoint = [179.99999999999986, 0.0, 1.0]
renderView2.CameraParallelScale = 120.63413277766854

# current camera placement for renderView3
renderView3.InteractionMode = '2D'
renderView3.CameraPosition = [179.99999999999986, 0.0, 778.5552911698041]
renderView3.CameraFocalPoint = [179.99999999999986, 0.0, 1.0]
renderView3.CameraParallelScale = 120.63413277766854

# current camera placement for renderView4
renderView4.InteractionMode = '2D'
renderView4.CameraPosition = [179.99999999999986, 0.0, 778.5552911698041]
renderView4.CameraFocalPoint = [179.99999999999986, 0.0, 1.0]
renderView4.CameraParallelScale = 120.77916470016476

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).