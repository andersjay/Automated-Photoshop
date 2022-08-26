from turtle import st
import win32com.client
import os
from photoclass import Photoclass


def main():
  p = Photoclass()
  folder_path = "D:\Documents\Programming\CodeUniverse\Games\Games novos\game5\game5"
  

  file_count = len(os.listdir(folder_path))

  print(file_count)
  for passo in range(file_count):
    passo += 1
    psd_origin_path = "D:\Documents\Programming\CodeUniverse\Games\Games novos\game7\game7" + "\\" + "passo" + str(passo) + ".psd"
    psd_origin_new = "D:\Documents\Programming\CodeUniverse\Games\Games novos\game7\game7" + "\\" + "passo3.0.psd"
    psd_origin = psd_origin_path
    jpeg_path = os.path.abspath('./tests/resources/game7')
    jpeg_name = 'passo'
    jpeg_num = passo
    jpeg_num_str = str(jpeg_num)
    jpeg_name_with_extension = jpeg_name + jpeg_num_str + '.jpg'
    jpeg_full_path = os.path.join(jpeg_path, jpeg_name_with_extension)

    if os.path.exists(jpeg_full_path):
      os.remove(jpeg_full_path)

    if not os.path.exists(jpeg_path):
      os.mkdir(jpeg_path)
    
    if passo == 3:
      psd_origin = psd_origin_new
      exported = False
      opened = p.openPSD(psd_origin)
      p.openPSD(psd_origin)
      if opened:
        group = 'passo'
        layer_name = 'PASSO 51'

        step_num_text = passo
        setp_num_text_str = str(step_num_text)
        text = 'PASSO ' + setp_num_text_str
        updated = p.updateLayerText(group, layer_name, text)

        if updated:
          exported = p.exportJPEG(jpeg_name_with_extension, jpeg_path)
          p.closePSD()
    
        
    if passo != 3:
      p.openPSD(psd_origin)

      exported = False

      opened = p.openPSD(psd_origin)
      if opened:
        group = 'passo'
        step_num = passo
        setp_num_str = str(step_num)
        layer_name = 'PASSO ' + setp_num_str

        step_num_text = passo
        setp_num_text_str = str(step_num_text)
        text = 'PASSO ' + setp_num_text_str
        updated = p.updateLayerText(group, layer_name, text)

        if updated:
          exported = p.exportJPEG(jpeg_name_with_extension, jpeg_path)
          p.closePSD()

main()
