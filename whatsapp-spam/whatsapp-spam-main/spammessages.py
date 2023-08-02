import pyautogui as pt 
import time

limit = int(input("Enter the Number of messages: "))
message = input("Enter the message: ")
count = 0
time.sleep(3)

while count < limit:

	pt.typewrite(message)
	pt.press('enter')
	count += 1
