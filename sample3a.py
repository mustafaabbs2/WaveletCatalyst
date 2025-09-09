from paraview.simple import *

wavelet1 = Wavelet()

slice1 = Slice(registrationName='Slice1', Input=wavelet1)
slice1.SliceType = 'Plane'
slice1.SliceType.Normal = [0, 0, 1]

sliceDisplay = Show(slice1)

ResetCamera()   # fit the object into the view
