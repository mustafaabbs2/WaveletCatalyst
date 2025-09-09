from paraview.simple import *

wavelet1 = Wavelet(registrationName="Wavelet1")

slice1 = Slice(registrationName='Slice1', Input=wavelet1)
slice1.SliceType = 'Plane'
slice1.SliceType.Normal = [0, 0, 1]

sliceDisplay = Show(slice1)

ResetCamera()   # fit the object into the view

from paraview import print_info
view = GetActiveView()

# create an image extractor
png1 = CreateExtractor('PNG', view, registrationName='PNG1')
png1.Trigger = 'TimeStep'
png1.Writer.FileName = 'RenderView1_{timestep:06d}{camera}.png'
png1.Writer.ImageResolution = [1000, 1000]
png1.Writer.Format = 'PNG'
