import arcpy
import pythonaddins
#from PyQt4 import QtGui
try:
    import DEMCreater
except ImportError as e:
    pythonaddins.MessageBox(e.message, "ImportError")
    print 'haha'
import sys

class ComputeReservoir(object):
    """Implementation for PyFile_addin.ComputeReservoirButton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class CreateDEM(object):
    """Implementation for PyFile_addin.CreateDEMButton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        DEMCreater.p()
        pythonaddins.MessageBox("haha", "ImportError")



class DrawInterestRegion(object):
    """Implementation for PyFile_addin.DrawInterestRegionTool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pass
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass