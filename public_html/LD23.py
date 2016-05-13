import numpy
from PythonMagick import Image
m = numpy.matrix([ \
[0,1,1,1,1,0], \
[0,0,0,0,1,0], \
[0,0,0,1,0,0], \
[0,0,1,0,0,0], \
[0,1,0,0,0,0], \
[0,1,1,1,1,0], \
])

bilde = Image ("6x6", "#FFF")
for i in range (0,6):
 for j in range (0,6):
  if(m[j,i]==1):
   bilde.pixelColor (i,j,"#FF4081")
bilde . scale ( "300x300" )
bilde . write ( "231.png" )
