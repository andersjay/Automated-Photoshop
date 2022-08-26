import os

import win32com.client

from pathvalidate import sanitize_filename


class Photoclass:
    app = None
    psd_file = None

    def __init__(self):
        self.app = win32com.client.Dispatch("Photoshop.Application")
 

    def closePhotoshop(self):
        self.app.Quit()

    def openPSD(self, filename):
        if os.path.isfile(filename) == False:
            self.closePhotoshop()
            return False

        self.app.Open(filename)
        self.psd_file = self.app.Application.ActiveDocument
        return True

    def closePSD(self):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)

        self.app.Application.ActiveDocument.Close(2)

    def updateLayerText(self, group, layer_name, text):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)

        group = self.psd_file.LayerSets[group]
        layer = group.ArtLayers[layer_name] 
        layer.TextItem.Contents = text
        return True

    def exportJPEG(self,filename, folder='', quality=10):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)
        
        filename = sanitize_filename(filename)
        full_path = os.path.join(folder, filename)

        options = win32com.client.Dispatch("Photoshop.ExportOptionsSaveForWeb")
        options.Format = 6
        options.Quality = quality

        self.psd_file.Export(ExportIn=full_path, ExportAs=2,Options=options)
        
        return os.path.isfile(full_path)

