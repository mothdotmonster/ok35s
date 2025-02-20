import random, microcontroller, time, board, digitalio, supervisor

random.seed(int.from_bytes(microcontroller.cpu.uid)) # read serial as pRNG seed so this is actually determinstic

for i in range(0, random.randint(0, 10)): # increment pRNG randomly for randomer randomness
	random.random()

delay = random.random() # wait a (pseudo)random amount
time.sleep(delay/10)

with digitalio.DigitalInOut(board.D0) as d0:
	d0.direction = digitalio.Direction.INPUT
	if d0.value:
		while True:
			print("Invalid connection detected. Panicking!")
	d0.direction = digitalio.Direction.OUTPUT
	d0.value = True

	with digitalio.DigitalInOut(board.D2) as d2:
		d2.direction = digitalio.Direction.INPUT
		time.sleep(0.1)
		leftSide = d2.value

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()

if supervisor.runtime.usb_connected:
	if leftSide:
		split = Split(
		split_flip=False,
		split_side=SplitSide.LEFT,
		data_pin=board.D2,
		data_pin2=board.D3,
		uart_flip=True,
		use_pio=True,
		split_target_left=True)
	else:
		split = Split(
		split_flip=False,
		split_side=SplitSide.RIGHT,
		data_pin=board.D0,
		data_pin2=board.D1,
		uart_flip=True,
		use_pio=True,
		split_target_left=False)
else:
	if leftSide:
		split = Split(
		split_flip=False,
		split_side=SplitSide.LEFT,
		data_pin=board.D2,
		data_pin2=board.D3,
		uart_flip=True,
		use_pio=True,
		split_target_left=False)
	else:
		split = Split(
		split_flip=False,
		split_side=SplitSide.RIGHT,
		data_pin=board.D0,
		data_pin2=board.D1,
		uart_flip=True,
		use_pio=True,
		split_target_left=True)

keyboard.modules.append(Layers())
keyboard.modules.append(split)

keyboard.col_pins = (board.D4, board.D5, board.D6, board.D7, board.D8, board.D9, board.A1)
keyboard.row_pins = (board.D10, board.MOSI, board.MISO, board.SCK, board.A0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

import keymap

keyboard.keymap = keymap.keymap

if __name__ == '__main__':
	keyboard.go()
