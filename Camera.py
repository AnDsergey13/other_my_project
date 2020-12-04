import picamera
from PIL import Image
#import RPi.GPIO as GPIO
import keyboard
import time
import numpy as np

photo_width= 512
photo_height= 384

try:
    camera = picamera.PiCamera()
    # Задать размер видео
    camera.resolution = (photo_width, photo_height)
    # Отразим камеру по вертикали
    camera.vflip = True
    # photo = np.empty((photo_height, photo_width, 3), dtype=np.uint8)
    
    camera.start_preview()
    # Создан буфер для видео
    stream = picamera.PiCameraCircularIO(camera, seconds=20)
    # Запускаем запись видео
    camera.start_recording(stream, format='h264')
    
    while (not keyboard.is_pressed('esc')):
        pass    
        
    camera.stop_recording()
    camera.stop_preview()
    # Сохраняем видео длинной в 5 сек
    stream.copy_to("stream.h264", seconds=5)
    
finally:
    
    camera.close()
#    GPIO.cleanup()
    print("Конец программы")
    
    
'''
img = Image.open("test2.jpg")
        pad = Image.new("RGB", (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
        ))
        pad.paste(img, (0, 0))
        o = camera.add_overlay(pad.tobytes(), size=img.size)
        o.alpha = 255
        o.layer = 3
        
        time.sleep(0.05)
        
        camera.remove_overlay(o)
'''
# camera.image_effect = "none"
# negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation, colorswap, washedout, posterise, colorpoint, colorbalance, cartoon, deinterlace1, deinterlace2, none.
