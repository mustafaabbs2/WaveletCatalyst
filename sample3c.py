from paraview.simple import *

wavelet1 = Wavelet(registrationName="Wavelet1")

slice1 = Slice(registrationName='Slice1', Input=wavelet1)
slice1.SliceType = 'Plane'
slice1.SliceType.Normal = [0, 0, 1]

sliceDisplay = Show(slice1)

ResetCamera()   # fit the object into the view

from paraview import print_info
view = GetActiveView()

def catalyst_initialize():
    print_info("in '%s::catalyst_initialize'", __name__)

def catalyst_finalize():
    print_info("in '%s::catalyst_finalize'", __name__)

def catalyst_execute(info):
    fname = "output-%d.png" % info.timestep
    print_info("time=%f, saving file: %s", info.time, fname)
    SaveScreenshot(fname, view, ImageResolution=[1000, 1000])
