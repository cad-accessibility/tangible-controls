import time
import board
import digitalio
import time
import analogio

slider = analogio.AnalogIn(board.POTENTIOMETER)
position = slider.value
print(position)

while True:
    time.sleep(0.1)
    print("Slider: ", slider.value/65535*100)
