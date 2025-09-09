from paraview.simple import *

wavelet1 = Wavelet(registrationName="Wavelet1")

slice1 = Slice(registrationName='Slice1', Input=wavelet1)
slice1.SliceType = 'Plane'
slice1.SliceType.Normal = [0, 0, 1]

sliceDisplay = Show(slice1)

ResetCamera()   # fit the object into the view

from paraview import print_info
view = GetActiveView()

# create a data extractor
vtp1 = CreateExtractor('VTP', slice1, registrationName='VTP1')
vtp1.Trigger = 'TimeStep'
vtp1.Writer.FileName = 'Slice1_{timestep:06d}.pvtp'
