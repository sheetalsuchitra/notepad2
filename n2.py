import pyautogui as pg
import time
pyautogui.FAILSAFE = False

pg.moveTo(722,54)
pg.click(722,54)
pg.hotkey('shift','h')
pg.moveTo(722,54)
pg.click(722,54)
pg.hotkey('shift','e')
pg.moveTo(722,54)
pg.click(722,54)
pg.hotkey('shift','l')
pg.moveTo(722,54)
pg.click(722,54)
pg.hotkey('shift','l')
pg.moveTo(722,54)
pg.click(722,54)
pg.hotkey('shift','o')

pg.moveTo(695,31)
pg.click(695,31)
pg.hotkey('down', 'down','down','down')
pg.press('enter')
File_name = 'C:\\Notepad'
pg.typewrite(File_name)
pg.hotkey('enter')
pg.moveTo(1211,494)
pg.click(1211,494)
