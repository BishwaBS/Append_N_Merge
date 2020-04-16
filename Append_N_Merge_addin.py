import arcpy
import pythonaddins

class Button1(object):
    """Implementation for Append_N_Merge_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        self.mxd = arcpy.mapping.MapDocument("current")
        layers = arcpy.mapping.ListLayers(self.mxd)
        for layer in layers:
            arcpy.AddField_management(layer, "Name", "TEXT")
            with arcpy.da.UpdateCursor(layer, 'Name') as cur:
                for row in cur:
                    row[0] = layer.name
                    cur.updateRow(row)
        arcpy.Merge_management(layers)
        
        pythonaddins.MessageBox("Completed", "Info", 0)
