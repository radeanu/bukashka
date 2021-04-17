import pyautogui
import mouse
import time

pyautogui.PAUSE = 0.01
iterations = 1000
current = 0

# pyautogui.screenshot('preview.png', region=(355,290, 400, 540))
scanRegion = (355,290, 400, 540)

while current < iterations:
  print('Nr: ', current)
  match = pyautogui.locateCenterOnScreen('target.png', confidence=0.8, grayscale=True, region=scanRegion)

  if(match):
    print('Kill: ', match)
    mouse.move(match.x, match.y)
    mouse.click()
    time.sleep(1.5)
    current = current+1
