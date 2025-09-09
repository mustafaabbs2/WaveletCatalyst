# script-version: 2.0
# Catalyst state generated using paraview version 5.12.1-3871-g11255fd09e
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.Set(
    ViewSize=[923, 471],
    CameraPosition=[57.41224450053896, -17.183645690376135, 29.782838536328494],
    CameraViewUp=[-0.2329028117550135, -0.9664148418938354, -0.10862151556631013],
)

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Wavelet'
wavelet1 = Wavelet(registrationName='Wavelet1')

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=wavelet1)
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Normal = [-0.8452055877234708, -0.07596757215005974, -0.5290145956990673]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from wavelet1
wavelet1Display = Show(wavelet1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
wavelet1Display.Set(
    Representation='Outline',
    ColorArrayName=['POINTS', ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
wavelet1Display.ScaleTransferFunction.Points = [37.35310363769531, 0.0, 0.5, 0.0, 276.8288269042969, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
wavelet1Display.OpacityTransferFunction.Points = [37.35310363769531, 0.0, 0.5, 0.0, 276.8288269042969, 1.0, 0.5, 0.0]

# show data from slice1
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'RTData'
rTDataLUT = GetColorTransferFunction('RTData')
rTDataLUT.Set(
    RGBPoints=GenerateRGBPoints(
        range_min=37.35310363769531,
        range_max=276.68310546875,
    ),
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
slice1Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'RTData'],
    LookupTable=rTDataLUT,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [37.35310363769531, 0.0, 0.5, 0.0, 276.68310546875, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [37.35310363769531, 0.0, 0.5, 0.0, 276.68310546875, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for rTDataLUT in view renderView1
rTDataLUTColorBar = GetScalarBar(rTDataLUT, renderView1)
rTDataLUTColorBar.Set(
    Title='RTData',
    ComponentTitle='',
)

# set color bar visibility
rTDataLUTColorBar.Visibility = 1

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'RTData'
rTDataPWF = GetOpacityTransferFunction('RTData')
rTDataPWF.Set(
    Points=[37.35310363769531, 0.0, 0.5, 0.0, 276.68310546875, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
# init the 'PNG' selected for 'Writer'
pNG1.Writer.Set(
    FileName='RenderView1_{timestep:06d}{camera}.png',
    ImageResolution=[923, 471],
    Format='PNG',
)

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)
