import os
from tokenize import group
import unittest
import sys
sys.path.insert(0, './src')
from photoclass import Photoclass


class TestPhotoclass(unittest.TestCase):

    def setUp(self):
        # Perguntar ao usuário qual o caminho do arquivo PSD
        caminho_psd = input('Qual o caminho do arquivo PSD? ')

        # self.psd_origin = os.path.abspath('tests/passo1.psd')
        self.psd_origin = os.path.abspath(caminho_psd)
        self.jpeg_path = os.path.abspath('./tests/resources/tmp')
        self.jpeg_name = 'passo1.jpg'
        self.jpeg_full_path = os.path.join(self.jpeg_path, self.jpeg_name)

        if not os.path.exists(self.jpeg_path):
            os.mkdir(self.jpeg_path)

        self.app = Photoclass()

    def tearDown(self):
        # self.app.closePhotoshop()

        if os.path.exists(self.jpeg_full_path):
            os.remove(self.jpeg_full_path)

        if os.path.exists(self.jpeg_path):
            os.rmdir(self.jpeg_path)

    def test_openPSD(self):
        opened = self.app.openPSD(self.psd_origin)

        if opened:
            self.app.closePSD()
        self.assertTrue(opened)

    def test_updateLayerText(self):
        updated = False

        opened = self.app.openPSD(self.psd_origin)
        if opened:
            group = input('Qual o nome do grupo? ')
            layer_name = input('Qual o nome da camada? ')
            text = input('Qual o texto? ')
            updated = self.app.updateLayerText(group, layer_name, text)
            self.app.closePSD()

        self.assertTrue(updated)

    def test_exportJPEG(self):
        exported = False

        opened = self.app.openPSD(self.psd_origin)
        if opened:
            group = input('Qual o nome do grupo? ')
            layer_name = input('Qual o nome da camada? ')
            text = input('Qual o texto? ')
            updated = self.app.updateLayerText(group, layer_name, text)

            if updated:
                exported = self.app.exportJPEG(self.jpeg_name, self.jpeg_path)
                self.app.closePSD()

            self.app.closePSD()
        
        self.assertTrue(exported)


if __name__ == '__main__':
    unittest.main()
