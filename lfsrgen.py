
def quit_or_new():
	quit = (input("\nQ to exit, N to continue:\n")).lower()
	if quit == "n":
		menu()
	else:
		pass

def menu():
	mode = int(input("\nEnter how many thousand digits, or '0' for continuous output:\n"))
	if mode == 0:
		infinite_output()
	else:
		set_output(mode*1000)

def infinite_output():
	rout = 1 << 127 | 1
	while True:
		print(rout & 1, end = "")
		shiftval = (rout) ^ (rout >> 1) ^ (rout >> 2) ^ (rout >> 7)
		rout = rout >> 1 | shiftval << 127

def set_output(charlimit):
	rout = 1 << 127 | 1
	for i in range(charlimit):
		print(rout & 1, end = "")
		shiftval = (rout) ^ (rout >> 1) ^ (rout >> 2) ^ (rout >> 7)
		rout = rout >> 1 | shiftval << 127
	quit_or_new()




menu()