import random
import time
#Python scripts control the mouse and keyboard to automate interactions with other applications
import pyautogui as pag

while True :
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    #time sleep is depend on your computer clock
    time.sleep(2)

#(function) def moveTo(
    #x: _NormalizeableXArg | None = None,
    #y: SupportsInt | None = None,
    #duration: float = 0,
    #tween: (float) -> float = ...,
    #logScreenshot: bool = False,
    #_pause: bool = True
#) -> None

