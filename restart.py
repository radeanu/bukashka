import pyautogui
import mouse
import time

pyautogui.PAUSE = 0.001
iterations = 1000
current = 0

# pyautogui.screenshot('full.png', region=(420,500, 250, 100))

while current < iterations:
  again = pyautogui.locateCenterOnScreen('again.png', confidence=0.8, grayscale=True, region=(420,500, 250, 100))

  if(again):
    print('Restarting...')
    mouse.move(again.x, again.y)
    mouse.click()
    time.sleep(2)
    current = current+1
