import time, sys

print("Press enter to start, Ctrl + C to stop")
input()
start_time = time.time()
last_time = round(start_time, 2)
lap_num = 1

while True:
	try:
		input()
		lap_time = round(time.time()-last_time, 2)
		total_time = round(time.time()-start_time, 2)
		print(f"lap:{lap_num}  {total_time}sec  {lap_time}sec")
		lap_num += 1
		last_time = time.time()
	except KeyboardInterrupt:
		print('\nDone.')
		sys.exit()