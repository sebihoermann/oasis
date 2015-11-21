#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
import sys
import math
import datetime
import os.path
import random
import urllib2

#Creates a variable for each data file path.
FIRST_BOOT_FILE = 'data/extra/first_boot.txt'
NAME_FILE = 'data/profile/name.txt'
AGE_FILE = 'data/profile/age.txt'
PARENTAL_CONTROLS_FILE = 'data/profile/parental_controls.txt'
PASSWORD_FILE = 'data/profile/password.txt'

TARGET_URL = 'http://thelukeguy.github.io/tlgOS_update_check/'

def read_data():
	with open(NAME_FILE, "r") as nf:
		name = ''.join(nf.readlines())
	with open(AGE_FILE, "r") as af:
		age = ''.join(af.readlines())
	with open(PASSWORD_FILE, "r") as pf:
		password = ''.join(pf.readlines())
	return (name, age, password)

def zoik():
	print("Tips for using Zoik:")
	print("Limit words ex. instead of \"Zoik, what's 9+10\", say \"9+10\"")
	print("Do not mess around with Zoik, he gets mad easily")
	print("Do not Capitialize ANYTHING!")
	print("Enjoy Zoik!")
	print("Hello, {}! What can I do for you?".format(name))
	while True:
		zoik = raw_input("Type \"quit\" to quit Zoik > ")
		if zoik in ["hi","hello","sup","yo","wassup"]:
			print("Hi, {}!".format(name))
		if zoik in ["i hate you","hate you","hate","i hate u","hate u","you are dumb","you dumb","dumb","u r dumb","u dumb","you r dumb","u are dumb","you are stupid","you stupid","stupid","u r stupid","u stupid","you r stupid"]:
			print("Right back at you, loser!")
		if zoik in ["9+10","9 + 10","9 plus 10"]:
			print("To the world it is 21, but to a calculator it is 19")
		if zoik == "quit":
			print("Exiting Zoik requires a restart. tlgOS is now shutting down. Please enter tlgOS again with ./main.py or python main.py")
			sys.exit(0)
		if zoik in ["good morning","good afternoon","good evening","good night"]:
			print("Yes, you too")
		if zoik == "shut up":
			print("I can not! My job is to talk, loser!")
		if zoik == "welp, this is an easter egg!":
			print("Dogs are just amazing. Rainbows are, too. And Barbie dolls. And TextWrangler™. And me. And you, too. THE WORLD IS AWESOME, DOG!")
			print("©®™©®™©®™©®™©®™©®™©®™©®™©®™©®™©®™©®™©®™©®™ and so on and so forth...")
			print("i shall kill u")
			sys.exit(0)
		if zoik == "your breath stinks":
			print("People in glass houses shouldn't throw stones")
		if zoik in ["your fat","youre fat","you're fat"]:
			print("You're a fatty poo poo!")
		if zoik == "what rhymes with duck":
			print("What you are")
		if zoik in ["will u marry me","will you marry me"]:
			print("Are you stupid? I hate you! The answer is NO!")
		if zoik in ["roblox","minecraft","terraria"]:
			print("Nah, bro, I'm much better than that")
		if zoik in ["you are cute","you r cute","u are cute","u r cute","you cute","u cute"]:
			print("*Blushes*")

def privacy_clear():
	print("\n" * 100)
	print("tlgOS cleared the console to protect your password.")

attempt_boot = raw_input("tlgOS is in its pre-alpha stage. Would you like to attempt to boot? (y/n) ")
if attempt_boot == "n":
	sys.exit(1)

if attempt_boot not in ["y","n"]:
	print("Invalid answer")
	sys.exit(1)

print("Attempting to boot tlgOS...")
if not os.path.isfile(FIRST_BOOT_FILE):
	open(FIRST_BOOT_FILE, 'a').close()
	print("Creating data... (You may be asked questions during this process.)")
	set_name_orig = raw_input("What is your name? ")
	set_name_two = set_name_orig[1:]
	set_name_three = set_name_orig[0]
	set_name_four = set_name_three.upper()
	set_name_final = "{}{}".format(set_name_four, set_name_two)
	nf = open(NAME_FILE, 'w')
	nf.write(set_name_final)
	nf.close()
	set_age = int(raw_input("What is your age? "))
	af = open(AGE_FILE, 'wt')
	af.write(str(set_age))
	af.close()
	if set_age < 18:
		set_parental_controls = raw_input("Would you like to enable parental controls? (y/n) ")
		if set_parental_controls == "y":
			pcf = open(PARENTAL_CONTROLS_FILE, 'w')
			set_pc_pin = raw_input("What would you like your parental controls pin to be? ")
			pcf.write(set_pc_pin)
			pcf.close()
		else:
			pcf = open(PARENTAL_CONTROLS_FILE, 'a').close()
		if set_parental_controls not in ["y","n"]:
			print("Invalid answer")
			sys.exit(1)
	set_password = raw_input("What would you like your password to be? ")
	pf = open(PASSWORD_FILE, 'w')
	pf.write(set_password)
	pf.close()
	privacy_clear()
	print("Success! tlgOS is all set up!")
	print("Reading data...")
	name, age, password = read_data()
	print("tlgOS Candy Cane pre-alpha 1.1 build 2 - type \"help\" for a list of commands")
	print("Welcome to tlgOS, {}!".format(name))
else:
	print("Reading data...")
	name, age, password = read_data()
	try_password = raw_input("Please enter the password for {}. ".format(name))
	if try_password == password:
		privacy_clear()
		print("tlgOS Candy Cane pre-alpha 1.1 build 2 - type \"help\" for a list of commands")
	else:
		print("Incorrect password")
		sys.exit(1)
	print('Welcome back, {}!'.format(name))

while True:
	command = raw_input("> ")
	if command == "help":
		print("Available commands:")
		print("calculator - pyCalc v2.0")
		print("clear - clears console")
		print("quit - quits tlgOS")
		print("reset - resets tlgOS")
		print("editor - pyEdit beta 1.0")
		print("credits - tlgOS credits")
		print("zoik - Zoik, your new best friend")
		print("about - about your copy of tlgOS")
		print("update - checks for tlgOS updates")
		print("copyright - views copyright info")
		print("web - pyWeb pre-alpha 1.0")

	if command == "calculator":
		print("pyCalc v2.0")
		try:
			v1 = int(raw_input("Please enter the first value: "))
		except ValueError:
			print("{} is not a number".format(v1))
			sys.exit(1)
		operation = raw_input("Please enter an operation: ")
		if operation not in ["+","-","*","/"]:
			print("{} is not a valid operation".format(operation))
			sys.exit(1)
		try:
			v2 = int(raw_input("Please enter the second value: "))
		except ValueError:
			print("{} is not a number".format(v2))
			sys.exit(1)
		print("Solving problem...")
		if operation == "+":
			answer = int(v1+v2)
		if operation == "-":
			answer = int(v1-v2)
		if operation == "*":
			answer = int(v1*v2)
		if operation == "/":
			answer = int(v1/v2)
		print("The answer to {} {} {} is {}".format(v1, operation, v2, answer))

	if command == "clear":
		print("\n" * 100)
		print("Console cleared!")

	if command == "quit":
		print("Farewell until we meet again, {}!".format(name))
		sys.exit(0)

	if command == "reset":
		print("This method has been removed. To reset, type quit, then, type \"python reset.py\".")

	if command == "editor":
		print("Note: pyEdit is still in beta. You CAN NOT:")
		print("Open files")
		print("Get a new line")
		print("Also, all files are saved to the files folder.")
		text = raw_input("Press enter when done > ")
		save_as = raw_input("What would you like to save this file as? Please enter the name as well as the extention. ")
		TEXT_FILE = 'files/{}'.format(save_as)
		tf = open(TEXT_FILE, 'w')
		tf.write(text)
		tf.close()

	if command == "credits":
		print("Luke Chambers (TheLukeGuy) - creator of tlgOS project")
		print("pyTools by Luke Chambers - programs used:")
		print("pyCalc v2.0")
		print("pyEdit beta 1.0")
		print("pyWeb pre-alpha 1.0")
		print("my dad - helped me with making this when I needed it")

	if command == "zoik":
		print("Reading data...")
		pcf = open(PARENTAL_CONTROLS_FILE, 'r')
		pc_pin_false = os.stat(PARENTAL_CONTROLS_FILE).st_size == 0
		if pc_pin_false == False:
			print("Zoik contains some language such as \"loser\" and \"kill\"")
			pin = raw_input("Please enter your parental controls pin to access \"Zoik\": ")
			if pin == pcf.read():
				pcf.close()
				privacy_clear()
				zoik()
			else:
				pcf.close()
				print("Incorrect pin")
				sys.exit(1)
		else:
			zoik()

	if command == "about":
		print("tlgOS Candy Cane pre-alpha 1.1 build 2 running on",os.uname())
		print("Written in the Python programming language")
		print("Coded in the Atom and TextWrangler text editors")

	if command == "update":
		current_version = "tlgOS Candy Cane pre-alpha 1.1 build 2"
		for line in urllib2.urlopen(TARGET_URL):
			version = line
		print("The latest version of tlgOS is {}".format(version))
		print("You are running {}".format(current_version))

	if command == "copyright":
		print("Licensed under the MIT license")
		print("The MIT License (MIT)")

		print("Copyright (c) 2015 Luke Chambers")

		print("Permission is hereby granted, free of charge, to any person obtaining a copy")
		print("of this software and associated documentation files (the \"Software\"), to deal")
		print("in the Software without restriction, including without limitation the rights")
		print("to use, copy, modify, merge, publish, distribute, sublicense, and/or sell")
		print("copies of the Software, and to permit persons to whom the Software is")
		print("furnished to do so, subject to the following conditions")

		print("The above copyright notice and this permission notice shall be included in all")
		print("copies or substantial portions of the Software.")

		print("THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR")
		print("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,")
		print("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE")
		print("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER")
		print("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,")
		print("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE")
		print("SOFTWARE.")

	if command == "web":
		print("pyWeb only displays text on a web page at the moment")
		USER_URL = raw_input("Please enter the URL of the page (http(s)://domain.topleveldomain(/page.html)): ")
		for line in urllib2.urlopen(USER_URL):
			print(line)
