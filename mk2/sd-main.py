import pyb
import time
import uos
import color
import gc
import sys
import machine
def makeVar(var,value):
	if var == "USER":
		print("You cannot change the $USER variable.")
		return False
	if var == "$USER":
		print("You cannot change the $USER variable.")
		return False
	else:
		with open("/sd/os/env/"+var,'w') as f:
			f.write(value)
			f.close()
		return True
"""def getAllVars:
	return uos.listdir("/sd/os/env/")"""
def getUser():
	with open("/sd/os/path/USER","r") as f:
		ff = f.read()
	return ff.replace(" ","").replace("\n","")
COMMANDS = ["echo","led-toggle","exit","hard-reset","cd","ls","pwd","rmdir","mkdir","prompt","sw-status","free","rm","clear-cache","su","mkuser","set","del"]
COMMANDS_DESC = {"echo":"echo | <TEXT>",
"led-toggle":"led-toggle | <COLOR>",
"exit":"exit | <NONE | EXITS>",
"hard-reset":"hard-reset | <NONE | HARD RESTART>",
"cd":"cd | <DIRECTORY>",
"ls":"ls | <NONE / DIRECTORY>",
"pwd":"pwd | <NONE | PRINTS WORKING DIRECTORY>",
"rmdir":"rmdir | <DIRECTORY>",
"mkdir":"mkdir | <DIRECTORY NAME>",
"prompt":"prompt | <NONE | RETURNS TO MICROPYTHON PROMPT>",
"sw-status":"sw-status | <NONE | PRINTS SWITCHES STATUS>",
"free":"free | <NONE | PRINTS FREE AND ALLOCATED MEMORY>",
"rm":"rm | <FILE>",
"clear-cache":"clear-cache | <NONE | CLEARS CACHE AND FREES MEMORY>",
"su":"su | <USER | SWITCHES USER>",
"mkuser":"mkuser | <USERNAME | CREATES A USER",
"set":"set | <VARIABLE NAME | VARIABLE VALUE | CREATES A VARIABLE>",
"del":"del | <VARIABLE NAME | DELETES A VARIABLE>"
}
def error():
	try:
		RED_LED.toggle()
		time.sleep_ms(350)
		RED_LED.toggle()
	except:
		pass

def getVar(name):
	try:
		if name == "USER":
			return getUser()
		else:
			with open("/sd/os/env/"+name,"r") as f:
				ff = f.read()
			return ff.replace(" ","").replace("\n","")
	except:
		return " "
		error()
color.autoreset(True)
RED_LED = pyb.LED(1)
GREEN_LED = pyb.LED(2)
YELLOW_LED = pyb.LED(3)
BLUE_LED = pyb.LED(4)
LEDS = [RED_LED,GREEN_LED,YELLOW_LED,BLUE_LED]
def execute(command,args):
	if command == "echo":
		try:
			print(args)
			#if "$" in args:
				#print(args.split())
			#	f = args.split()
			#	for i in f:
			#		if "$" in i:
			#			print(args.replace(i,getVar(i.replace("$",""))))
			#else:
			#	print(args)

		except:
			error()

	if command == "led-toggle":
		if uos.uname()[1] == "pyboard":
			#if args == "help":
			#	error()
			#	print("usage: led-toggle | <LED NUMBER OR COLOR>")
			#else:
			if args == "red": #or "RED" or "Red":
				try:
					RED_LED.toggle()
				except:
					error()
			if args == "green":# or "GREEN" or "Green":
				try:
					GREEN_LED.toggle()
				except:
					error()
			if args == "yellow":# or "YELLOW" or "Yellow":
				try:
					YELLOW_LED.toggle()
				except:
					error()
			if args == "blue":# or "BLUE" or "Blue":
				try:
					BLUE_LED.toggle()
				except:
					error()
			if args == "all":
				for i in LEDS:
					i.toggle()

			if args == "help":
				print("usage: led-toggle | <COLOR>")

		else:
			error()
			print(color.red("The ")+color.yellow("led-toggle")+color.red("command is only compatible with a pyboard."))
	
	if command == "exit":
		try:
			sys.exit()
		except:
			print("Failed.")
			error()

	if command == "hard-reset":
		try:
			machine.reset()
		except:
			error()
			print("Failed.")

	if command == "cd":
		if not args:
			print("usage: cd | <DIRECTORY>")
		if args:
			try:
				uos.chdir(args)
			except:
				print(color.red("Unkown directory: ")+color.yellow(args))

	if command == "ls":
		if not args:
			try:
				for i in uos.listdir():
					print(color.yellow(i)+color.blue(","))
			except:
				print("Failed")
				error()
		if args:
			try:
				for i in uos.listdir(args):
					print(color.blue(i+", "))
			except:
				print(color.red("Unkown directory: ")+color.yellow(args))

	if command == "pwd":
		try:
			print(uos.getcwd())
		except:
			error()
			print("Failed.")

	if command == "rmdir":
		try:
			uos.rmdir(args)
		except:
			print(color.red("Unkown directory: ")+color.yellow(args))
			error()

	if command == "mkdir":
		try:
			uos.mkdir(args)
		except:
			print("Failed")
			error()

	if command == "prompt":
		try:
			sys.exit()
		except:
			print("Failed.")
			error()

	if command == "sw-status":
		try:
			switch = pyb.Switch()
			if switch.value():
				print("Switch being pressed.")
			else:
				print("Switched not being pressed.")
		except:
			error()

	if command == "help":
		if not args:
			try:	
				for i in COMMANDS:
					print(COMMANDS_DESC[i])
			except:
				print("Failed.")
				error()
		if args:
			try:
				print(COMMANDS_DESC[args])
			except:
				print(color.red("Unkown command: ")+color.yellow(args))
	
	if command == "free":
		try:
			print("ALLOCATED_MEMORY = "+str(int(gc.mem_alloc()/1000))+"KB")
			print("FREE_MEMORY = "+str(int(gc.mem_free()/1000))+"KB")
			#print("CPU_FREQ = "+str(machine.freq()))
		except:
			print("Failed.")
			error()

	if command == "touch":
		if not args:
			print("usage: "+COMMANDS_DESC["touch"])
			error()
		if args:
			try:
				f = open(args,"w")
				f.close()
			except:
				print("Failed.")
				error()

	if command == "rm":
		if not args:
			print("usage: "+COMMANDS_DESC["rm"])
			error()
		if args:
			try:
				if args == "main.py":
					print("You can not remove main or boot files.")
				if args == "boot.py":
					print("You can not remove main or boot files.")
				if args == "color.py":
					print("This file is needed.")
				else:
					try:
						uos.remove(args)
					except:
						error()
						print(color.red("Unkown file: ")+color.yellow(args))
			except:
				print("Failed.")
				error()

	if command == "clear-cache":
		try:
			gc.collect()
		except:
			print("Failed.")
			error()

	if command == "mkuser":
		try:
			uos.mkdir("/sd/os/home/"+args)
			print(color.blue("Created user: ")+color.yellow(args))
			#print(color.blue("Use")+color.yellow(f" su {args}")+color.blue(" to switch to that user"))
		except:
			error()
			print("Failed.")

	if command == "su":
		try:
			for i in uos.listdir("/sd/os/home"):
				if i == args:
					with open("/sd/os/path/USER","w") as f:
						f.write(args)
						f.close()
						uos.chdir("/sd/os/home/"+getUser())
				#else:
				#	print(color.red("Unkown user:")+color.yellow (" "+args))
		except:
			print("Failed.")
			error()

	if command == "set":
		try:
			if len(args.split()) > 2:
				print(color.red("Error: ")+color.yellow("this comand takes two arguments"))#try:
			if len(args.split()) < 2:
				print(color.red("Error: ")+color.yellow("this comand takes two arguments"))#try:
			else:
			#print(args.replace("="," ").split())	#print(args.partition("="))
				if makeVar(args.upper().split()[0],args.replace("="," ").split()[1]):
					print("New variable: $"+args.upper().split()[0]+" with value "+args.split()[1])
				else:
					pass
		except:

			error()
			print("Failed.")

	if command == "del":
		try:
			args = args.upper()
			if args == "USER":
				print("You cannot remove the $USER variable")
			if args == "$USER":
				print("You cannot remove the $USER variable")
			if args == "user":
				print("You cannot remove the $USER variable")
			else:
				uos.remove("/sd/os/env/"+args.replace("$","").upper())
		except:
			print("Failed.")
			error()


	#	except:
		#	error()
		#	print("Failed.")


uos.chdir("/sd/os/home/"+getUser())


while True:
	f = input(color.green(getUser())+color.yellow("@")+color.green(uos.uname()[1])+color.yellow("~")+color.blue((uos.getcwd()+" $ ")))
	#print(f.partition(" "))
	if "$" in f:
		#print(f.split())		#print(args.split())				f = args.split()
		for i in f.split():
			if "$" in i:
				execute(f.partition(" ")[0],f.partition(" ")[2].replace(i,getVar(i.replace("$",""))))
				break
	else:			
		execute(f.partition(" ")[0],f.partition(" ")[2])
		#		break
