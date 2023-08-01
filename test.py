from pynput.keyboard import Key, Controller

keyboard = Controller()

while True:
	if keyboard.press('a'):
		print('helloWorld')