"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *
from qgis.utils import qgsfunction
from qgis.core import qgsfunction
from math import atan2, degrees, pi

@qgsfunction(args='auto', group='Deep')
def anglePolygon(g, feature, parent):
	"""
        Calculates the rotation of the smallest bounding box!
    """
	x0 = g.vertexAt(0).x()
	x1 = g.vertexAt(1).x()
	x2 = g.vertexAt(2).x()
	y0 = g.vertexAt(0).y()
	y1 = g.vertexAt(1).y()
	y2 = g.vertexAt(2).y()
	a = x1-x0
	b = y1-y0
	d = x2-x1
	e = y2-y1
	width = math.sqrt(a**2 + b**2)
	height = math.sqrt(d**2 + e**2)
	rads = atan2(b,a)
	rads %= 2*pi
	degs = degrees(rads)	
	
	if width < height:
		ang2 = degs - 90
	else:
		if degs > 0:
			ang2 = degs + 180
		else:
			ang2 = degs + 180
	if ang2 > 180 and ang2 < 360:
		ang3 = ang2 - 180
	else:
		ang3 = ang2
	if ang3 < -90:
		ang4 = ang3 + 180
	else:
		ang4 = ang3
	if ang4 >150 and ang4 < 180:
		ang5 = ang4 - 180
	else:
		ang5 = ang4
	if ang5 > 360:
		ang6 = ang5 - 360
		if ang6 > 150 and ang6 <180:
			ang7 = ang6 - 180
		else:
			ang7 = ang6
	else:
		ang7 = ang5
	return ang7
