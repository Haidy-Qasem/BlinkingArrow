import time
import os 
while True:
	n=int(input("Enter the height of te arrow"))
	# up
	for i in range(n):
		for j in range (i,n):
			print("  ",end="")
		for j in range(i+1):
			print(" *",end="")
		for j in range(i):
			print(" *",end="")
		print()
	time.sleep(.5)
	os.system("cls")

	# right arrow
	for i in range (0,n):

		for j in range(i+1):

			print("*", end=" ")
		print()
	for i in range(n):
		for j in range(i,n-1):
			print("*",end=" ")
		print()

	time.sleep(.5)
	os.system("cls")

	# down
	for i in range (0,n):
		for j in range(i+1):
			print("  ",end="")
		for j in range(i,n):
			print(" *",end="")
		for j in range(i,n-1):
			print(" *",end="")
		
		print()
	print()

	time.sleep(.5)
	os.system("cls")

	# left
	for i in range(0,n):
		for j in range (i,n):
			print("  ",end="")
		for j in range(i+1):
			print(" *",end="")
		print()
	for i in range(n):
		for j in range(0,i+2):
			print("  ",end="")
		for j in range(i,n-1):
			print (" *",end="")
		print()
	time.sleep(.5)	
	os.system("cls")
