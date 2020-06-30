import pyb
import time
import uos
import color
import gc
import ujson
VARS = {"mp":"MICROPYTHON",
"VAR":"test",
"test":"test"}
import sys
import machine
def makeNormalVar(name,value):
	with open('/flash/os/path/'+name+".json",'w') as fw:
		f = """
{\"1\":\"2\"}
""".replace("1",name).replace("2",value)
	fw.write(f)



def makeVar(var,value):
	if var == "USER":
		print("You cannot change the $USER variable.")
		return False
	if var == "$USER":
		print("You cannot change the $USER variable.")
		return False
	else:
		with open("/flash/os/env/"+var,'w') as f:
			f.write(listToStr(value.split()))
			f.close()
		return True
"""def getAllVars:
	return uos.listdir("/flash/os/env/")"""
def getUser():
	with open("/flash/os/path/USER","r") as f:
		ff = f.read()
	return ff.replace(" ","").replace("\n","")
COMMANDS = ["echo","led-toggle","exit","hard-reset","cd","ls","pwd","rmdir","mkdir","prompt","sw-status","free","rm","clear-cache","su","mkuser","set","del","./<file>","load","shell","wait","loop","loop-delay","cat","dump"]
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
"set":"set | <VARIABLE NAME | VARIABLE VALUE | CREATES A VARIABLE> | e.g set <variable name> to <variable value>",
"del":"del | <VARIABLE NAME | DELETES A VARIABLE>",
"load":"load | <TIME (INT OF FLOAT) | DISPLAYS A LOADING BAR FOR (TIME)>",
"./<file>":"./<file> | <NONE | EXECUTE A SHELL SCRIPT>",
"shell":"shell | <FILENAME>",
"cat":"cat | <FILENAME>",
"dump":"dump | <FILENAME | TEXT>",
"wait":"wait | <TIME IN SECONDS>",
"loop":"loop | <TIMES | COMMAND>",
"loop-delay":"loop-delay | <TIMES | DELAY | COMMANDS>"

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
		name = name.replace("$","")
		if name == "USER":
			return getUser()
		else:
			with open("/flash/os/env/"+name,"r") as f:
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
			uos.mkdir("/flash/os/home/"+args)
			print(color.blue("Created user: ")+color.yellow(args))
			#print(color.blue("Use")+color.yellow(f" su {args}")+color.blue(" to switch to that user"))
		except:
			error()
			print("Failed.")

	if command == "su":
		try:
			for i in uos.listdir("/flash/os/home"):
				if i == args:
					with open("/flash/os/path/USER","w") as f:
						f.write(args)
						f.close()
						uos.chdir("/flash/os/home/"+getUser())
				#else:
				#	print(color.red("Unkown user:")+color.yellow (" "+args))
		except:
			print("Failed.")
			error()

	if command == "set":
		try:
			#print(args.partition("to ")[2:])
		#d("Error: ")+color.yellow("this comand takes two arguments"))#try:
			makeVar(args.split()[0],listToStr(args.partition("to ")[2:]))
			#print(args.replace("="," ").split())	#print(args.partition("="))
			#if makeVar(args.upper().partition(" to")[0],listToStr(args.partition("to")[2:])):
				#p#rint("New variable: $"+args.upper().partition(" to")[0]+" with value "+listToStr(args.partition("to")[2:]))
			#else:
				#pass
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
				uos.remove("/flash/os/env/"+args.replace("$","").upper())
		except:
			print("Failed.")
			error()
	if command == "clear":
		try:
			clear()
		except:
			error()
			print("Failed.")

	if command == "shell":
		try:
			x = args
			for line in open(x,'r'):
				line = line.strip()
				if not line:
					pass
				if line.startswith("//"):
					pass
				if line.startswith("#"):
					pass
				if line.startswith("::"):
					pass
				if line.startswith("~"):
					pass
				if line:
					#lines = [line for line in file.readlines() if line.strip()]
					#print(line)
					for i in line.split():
						if "$" in i:
							#print(i)
							line = line.replace(i,getVar(i))
					x2 = listToStr(line.partition(line.split()[0])[2:])
					x2 = list(x2)
					x2[0] = ""
					x2 = ''.join(x2)
					#print(l
					#print(line)
					line = line.replace("%arg["+str(leng)+"]",i)
					
				#line = line.replace("%arg[1]",args.split()[1]).replace("%arg[2]",args.split()[2]).replace("%arg[3]",args.split()[3]).replace("%arg[4]",args.split()[4]).replace("%arg[5]",args.split()[5]).replace("%arg[6]",args.split()[6]).replace("%all_arg",listToStr(args.split()[1]))
				if not line:
					pass
				if line.startswith("//"):
					pass
				if line.startswith("#"):
					pass
				if line.startswith("::"):
					pass
				if line.startswith("~"):
					pass
				if line:
					#lines = [line for line in file.readlines() if line.strip()]
					#print(line)
					for i in line.split():
						if "$" in i:
							#print(i)
							line = line.replace(i,getVar(i))
					x2 = listToStr(line.partition(line.split()[0])[2:])
					x2 = list(x2)
					x2[0] = ""
					x2 = ''.join(x2)
					#print(line)
					execute(line.split()[0],x2)
		except:
			pass#print(color.red("Unkown file: ")+color.yellow(args))

	if command == "cmdshell":
		try:
			x = args.split()[0]
			for line in open(x,'r'):
				line = line.strip()
				line = line.replace("%arg[all]",''.join(args.partition(".command ")[2]))
				leng = -1
				for i in args.split():
					leng = leng + 1
					line = line.replace("%arg["+str(leng)+"]",i)

				for i in line.split():
					if "%arg" in i:
						line = line.replace(i,"None")

				if not line:
					pass
				if line.startswith("//"):
					pass
				if line.startswith("#"):
					pass
				if line.startswith("::"):
					pass
				if line.startswith("~"):
					pass
				if line:
					#lines = [line for line in file.readlines() if line.strip()]
					#print(line)
					for i in line.split():
						if "$" in i:
							#print(i)
							line = line.replace(i,getVar(i))
					x2 = listToStr(line.partition(line.split()[0])[2:])
					x2 = list(x2)
					x2[0] = ""
					x2 = ''.join(x2)
					#print(line)
					execute(line.split()[0],x2)
		except:
			pass#print(color.red("Unkown file: ")+color.yellow(args))
	
	if command.startswith("./"):
		execute("shell",command.replace("./",""))
	if command == "pass":
		pass

	if command == "nothing":
		pass


#		except:
		#	print(color.red("Unkown file: ")+color.yellow(x))

	"""if command == ">":
		#try:
		for line in open(args,'r'):
			x = line.split()
			for i in x:
				if "$" in i:
					line = line.replace(i,getVar(i.replace("$","")))
				if "#" in i:
					try:
						line = line.replace(i,VARS[i.replace("#","")])
					except:
						print("Undefined variable: "+i.replace("#",""))

			if line.startswith("if"):
				cmd = line.partition("->")[2]
				cmd1 = cmd.partition(":")[0]
				args1 = cmd.partition(":")[2]
				cmd1 = cmd1.partition(",")[0]
				args1 = args1.partition("else")[0]
				args1 = list(args1)
				cmd1 = list(cmd1)
				cmd1[0] = ""
				args1[0] = ""
				args1 = ''.join(args1)
				cmd1 = ''.join(cmd1)
				value = line.partition("==")[0]
				value1 = value.replace("if","")
				value2 = line.partition("==")[2]
				value2 = line.partition("->")[0]
				value2 = value2.partition("==")[2]
				else1 = line.partition("else")[2]
				else1cmd = else1.partition(";")[0]
				else1cmd = list(else1cmd)
				else1cmd[0] = ""
				else1cmd = ''.join(else1cmd)
				else1arg = else1.partition(";")[2]
				else1arg = list(else1arg)
				else1arg[0] = ""
				else1arg = ''.join(else1arg)
				if value1.replace(" ","") == value2.replace(" ",""):
					execute(cmd1,args1)
				else:
					execute(else1cmd,else1arg)
		if line.startswith("//"):
			pass

		if line.startswith("cmd"):
			cmd1 = line.partition("->")[2]
			cmd1 = cmd1.partition(":")[0]
			args1 = line.partition("->")[2]
			args1 = args1.partition(":")[2]
			args1 = list(args1)
			args1[0] = ""
			args1 = ''.join(args1)
			cmd1 = list(cmd1)
			cmd1[0] = ""
			cmd1 = ''.join(cmd1)
			execute(cmd1,args1)
		
		if line.startswith("set"):
			print(line.split())
			x3 = line.split()
			VARS[x3[1]] = listToStr(x3[3:])

		if line.startswith("ask"):
			question1 = line.partition("->")[0].replace("ask ","")
			var1 = line.partition("-> ")[2]
			VARS[question1] = input(var1)			

				
				
	#	except:
	#		print("Failed.")
			#error()
"""
	if command == "load":
		try:
			load(args)
			#if test == test -> echo: hello user, echo; hello not user

		except:
			print("Failed.")
			error()

	if command == "if":
		try:
			value1 = args.partition("->")
			#print(value1)
			#print(value1[2].partition(","))
			if value1[0].partition(" ==")[0].replace(" ","").replace("\n","") == value1[0].partition("== ")[2].partition(" then")[0].replace(" ","").replace("\n",""):#:#:
				execute(args.partition("-> ")[2].partition(" else")[0].partition(" ")[0].replace(" ",""),listToStr(args.partition("-> ")[2].partition(" else")[0].partition(" ")[2:]))#print(val1.replace(" ","").replace("\n",""))
			
			#print(value1[0].partition("-> ")[2].partition(":")[0].partition(" ")[0],value1[0].partition("-> ")[2].partition(":")[0].partition(" ")[2])
			if value1[0].partition(" ==")[0].replace(" ","").replace("\n","") != value1[0].partition("== ")[2].partition(" then")[0].replace(" ","").replace("\n",""):
				try:
					val1 = args.partition("-> ")[2].partition(" else")[2].partition(" ")[0]
					val2 = args.partition("-> ")[2].partition(" else")[2].partition(" ")[2]
					execute(val2.replace("\n","").partition(" ")[0].replace(" ",""),listToStr(val2.replace("\n","").partition(" ")[2:]))#.partition(" ")[0])#,args.partition("-> ")[2].partition(" ")[2].partition(" else")[0])
				except:
					pass#,value1[2].partition(": ")[2])
					
		except Exception as e:
			error()
			print("Failed.")

	if command == "ask":
		try:
			value1 = args.partition("->")
			
			#print(value1[0])
			f = input(value1[0])
			#print(f)
			#print(''.join(f.split()))
			execute("set",value1[2]+" to "+f)
		except:
			print("Failed.")
			error()

	if command == "print":
		print(args)

	if command == "dump":
		try:
			with open(args.split()[0],"w") as f:
				f.write(listToStr(args.split()[2:]).replace("\\n","\n"))
				f.close()
		except Exception as e:
			print(e)
			print("Failed")
			error()

	if command == "cat":
		try:
			with open(args,"r") as f:
				f = f.read()
				for i in COMMANDS:
					if i in f:
						f = f.replace(i,color.blue(i)).replace("==",color.red("==")).replace("->",color.green("->"))
						f = f.replace("else",color.red("else"))
				print(f.replace("else",color.red("else")))
		except:
			print(color.red("Unkown file: ")+color.yellow(args))

	if command == "math":
		try:
			if args.split()[0] == "once":
				args1 = args.replace("once ","")

				if args1.split()[0] == "add":
					print(float(args1.split()[1])+float(args1.split()[2]))
				if args1.split()[0] == "multiply":
					print(float(args1.split()[1])*float(args1.split()[2]))
				if args1.split()[0] == "subtract":
					print(float(args1.split()[1])-float(args1.split()[2]))
				if args1.split()[0] == "divide":
					print(float(args1.split()[1])/float(args1.split()[2]))
				if args1.split()[0] == "modulus":
					print(float(args1.split()[1])%float(args1.split()[2]))
			if args.split()[0] == "store":
				args1 = args.replace("store ","")
				if args1.split()[0] == "add":
					makeVar(args1.split()[1],str(float(args1.split()[2])+float(args1.split()[3])))
				if args1.split()[0] == "multiply":
					makeVar(args1.split()[1],str(float(args1.split()[2])*float(args1.split()[3])))
				if args1.split()[0] == "subtract":
					makeVar(args1.split()[1],str(float(args1.split()[2])-float(args1.split()[3])))
				if args1.split()[0] == "divide":
					makeVar(args1.split()[1],str(float(args1.split()[2])/float(args1.split()[3])))
				if args1.split()[0] == "modulus":
					makeVar(args1.split()[1],str(float(args1.split()[2])%float(args1.split()[3])))

				
				
			

		except Exception as e:
			print(e)
			error()

	if command == "wait":
		try:
			time.sleep(float(args))
		except:
			print("Failed.")
			error()

	if command == "loop":
		try:
			#print(args.split())
			for i in range(int(args.split()[0])):
				execute(args.split()[1],listToStr(args.split()[2:]))
		except:
			error()
			print("Failed.")

	if command == "loop-delay":
		try:
			#print(args.split())
			for i in range(int(args.split()[0])):
				execute(args.split()[2],listToStr(args.split()[3:]))
				time.sleep(float(args.split()[1]))
		except:
			error()
			print("Failed.")



	else:
		try:
			cmd = command
			if not command:
				pass
			if command:
				execute("cmdshell","/flash/os/cmds/"+cmd+".command "+args)
		except:
			pass






	"""if pyb.Switch().value:
		execute("led-toggle","all")"""
def listToStr(s):
	return ''.join([str(elem) for elem in s])   

def load(amount):
    for i in range(0, 100):
    	time.sleep(float(amount))
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%" +  " |"+"."*i)
    print("\n")


    
	


def clear():
    print("\x1B\x5B2J", end="")
    print("\x1B\x5BH", end="")
	#	except:
		#	error()
		#	print("Failed.")





uos.chdir("/flash/os/home/"+getUser())


def start():
	while True:
		f = input(color.green(getUser())+color.yellow("@")+color.green(uos.uname()[1])+color.yellow("~")+color.blue((uos.getcwd()+" $ ")))
		#print(f.partition(" "))
		if "$" in f:
			#print(f.split())		#print(args.split())				f = args.split()
			for i in f.split():
				if "$" in i:
					f = f.replace(i,getVar(i.replace("$","")))#
			
		execute(f.partition(" ")[0],listToStr(f.partition(" ")[2:]))
		

					
					
			#execute(f.partition(" ")[0],listToStr(f.partition(" ")[2:]))
			#		break

start()
#start()
