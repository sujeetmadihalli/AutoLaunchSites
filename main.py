import pyautogui, time

time.sleep(2)

pyautogui.keyDown('ctrl')   #1
pyautogui.hotkey('win','d') #2
pyautogui.keyUp('ctrl')     #3 for opening a new window

pyautogui.press('win')
pyautogui.write('chrome') # "chrome" can be changed to any browser you like that you have installed
pyautogui.press('enter')
time.sleep(2)
f= open ("sites", 'r')
pyautogui.hotkey('ctrl', ' n') #for a new window in chrome
for word in f:
    pyautogui.write(word)
    pyautogui.press("enter")
    pyautogui.hotkey('ctrl', 't') #for new tab
    #pyautogui.hotkey('ctrl', ' n') #for new window in chrome


