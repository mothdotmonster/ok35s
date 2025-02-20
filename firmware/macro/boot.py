import board, supervisor
from kmk.bootcfg import bootcfg

# Only mount storage when [0,0] is held
bootcfg(
	sense=board.D4,   # Col0
	source=board.D10, # Row0
	storage=False
)

supervisor.set_usb_identification(
	manufacturer = 'moth.monster',
	product = 'OK35s',
	vid = 34558, # 86FE
	pid = 13573  # 3505
)
