#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
import sys
import math
import datetime
import os
import random
import urllib2
import subprocess
import afplay
import webbrowser
import time

#Creates a variable for each data file path.
FIRST_BOOT_FILE = 'data/extra/first_boot.txt'
NAME_FILE = 'data/profile/name.txt'
AGE_FILE = 'data/profile/age.txt'
PARENTAL_CONTROLS_FILE = 'data/profile/parental_controls.txt'
PASSWORD_FILE = 'data/profile/password.txt'

TARGET_URL = 'http://thelukeguy.github.io/oasis_update_check/'

oasisVersion = "2.0 Firefly"

def read_data():
	with open(NAME_FILE, "r") as nf:
		name = ''.join(nf.readlines())
	with open(AGE_FILE, "r") as af:
		age = ''.join(af.readlines())
	with open(PASSWORD_FILE, "r") as pf:
		password = ''.join(pf.readlines())
	return (name, age, password)

def clear():
	os.system('clear')

clear()
dots = 10
while dots > 0:
	print(".")
	time.sleep(0.2)
	clear()
	print("..")
	time.sleep(0.2)
	clear()
	print("...")
	time.sleep(0.2)
	clear()
	dots -= 1
time.sleep(3)
clear()
if not os.path.isfile(FIRST_BOOT_FILE):
	open(FIRST_BOOT_FILE, 'a').close()
	set_name_orig = raw_input("name - ")
	clear()
	set_name_two = set_name_orig[1:]
	set_name_three = set_name_orig[0]
	set_name_four = set_name_three.upper()
	set_name_final = "{}{}".format(set_name_four, set_name_two)
	nf = open(NAME_FILE, 'w')
	nf.write(set_name_final)
	nf.close()
	set_age = int(raw_input("your age - "))
	clear()
	af = open(AGE_FILE, 'wt')
	af.write(str(set_age))
	af.close()
	pcf = open(PARENTAL_CONTROLS_FILE, 'a').close()
	if set_age < 18:
		set_parental_controls = raw_input("parental controls? (y/n) - ")
		clear()
		if set_parental_controls == "y":
			pcf = open(PARENTAL_CONTROLS_FILE, 'w')
			set_pc_pin = raw_input("parental controls pin - ")
			clear()
			pcf.write(set_pc_pin)
			pcf.close()
		else:
			pcf = open(PARENTAL_CONTROLS_FILE, 'a').close()
		if set_parental_controls not in ["y","n"]:
			print("error - invalid answer")
			sys.exit(1)
	set_password = raw_input("password - ")
	clear()
	pf = open(PASSWORD_FILE, 'w')
	pf.write(set_password)
	pf.close()
	clear()
	print("Success! oasis is all set up!")
	print("Reading data...")
	name, age, password = read_data()
	print("oasis {} - type \"help\" for a list of commands".format(oasisVersion))
	print("Welcome to oasis, {}!".format(name))
else:
	print("Reading data...")
	name, age, password = read_data()
	try_password = raw_input("Please enter the password for {}. ".format(name))
	if try_password == password:
		clear()
		print("oasis {} - type \"help\" for a list of commands".format(oasisVersion))
	else:
		print("Incorrect password")
		sys.exit(1)
	print('Welcome back, {}!'.format(name))

while True:
	try:
		command = raw_input("> ")
		if command == "help":
			print("Available commands:")
			print("calculator - a basic calculator")
			print("clear - clears console")
			print("quit - quits oasis")
			print("reset - resets oasis")
			print("editor - a work in progress text editor")
			print("credits - oasis credits")
			print("about - about your copy of oasis")
			print("update - checks for oasis updates")
			print("copyright - views copyright info")
			print("music - plays music you upload")

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
				continue
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
			print("To reset, type quit, then, type \"python reset.py\".")

		if command == "editor":
			print("Note: This editor is still in beta. You CAN NOT:")
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
			print("Luke Chambers (TheLukeGuy) - creator of oasis project")
			print("my dad - helped me with making this when I needed it")

		if command == "about":
			print("oasis {} running on {}.".format(oasisVersion, os.uname()[1]))
			print("Written in the Python programming language")
			print("Coded in the Atom, TextWrangler, and Xcode text editors")

		if command == "update":
			current_version = "oasis {}".format(oasisVersion)
			for line in urllib2.urlopen(TARGET_URL):
				version = line
			print("The latest version of oasis is {}".format(version))
			print("You are running {}".format(current_version))

		if command == "copyright":
			print("Licensed under the MIT license")
			print("The MIT License (MIT)")

			print("Copyright (c) 2016 Luke Chambers")

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

		if command == "music":
			print("To add music, locate to the files folder and place your music there.")
			MUSIC_FILE = raw_input("What is the song saved as? ex. radioactive.mp3 ")
			afplay.afplay("files/{}".format(MUSIC_FILE))

	except KeyboardInterrupt:
		continue
