import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = (board.D4, board.D5, board.D6, board.D7, board.D8, board.D9, board.A1)
keyboard.row_pins = (board.D10, board.MOSI, board.MISO, board.SCK, board.A0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

import keymap

keyboard.keymap = keymap.keymap

if __name__ == '__main__':
	keyboard.go()
