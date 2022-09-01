# Screenshot 
#### pip install pyautogui 

import pyautogui

# get Screenshot

screenshot = pyautogui.screenshot()

screenshot_path = str(input("Enter path to save: \n"))
# save screenshot 
if(screenshot_path!=''):
    screenshot.save(screenshot_path + "/screenshot.png")