#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
from getpass import getpass
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

try:
	import console
	def clear():
		console.clear()
except ImportError:
	def clear():
		os.system('clear')

def pre_release():
	clear()
	bootup = raw_input("pre-releases may contain bugs - boot? (y/n) ")
	if bootup == "n":
		clear()
		sys.exit(0)
	elif bootup not in ["y", "n"]:
		clear()
		print("Invalid answer")
		sys.exit(1)
	clear()

pre_release()

FIRST_BOOT_FILE = 'data/extra/first_boot.txt'
NAME_FILE = 'data/profile/name.txt'
PASSWORD_FILE = 'data/profile/password.txt'

TARGET_URL = 'http://thelukeguy.github.io/oasis_update_check/'

oasisVersion = "2.2-pre3 Firefly"
current_version = "oasis {} (11/12/16)".format(oasisVersion)

def read_data():
	with open(NAME_FILE, "r") as nf:
		name = ''.join(nf.readlines())
	with open(PASSWORD_FILE, "r") as pf:
		password = ''.join(pf.readlines())
	return (name, password)

clear()

print("(                              )")
time.sleep(0.1)
clear()
print(" (                            )")
time.sleep(0.1)
clear()
print("  (                          )")
time.sleep(0.1)
clear()
print("   (                        )")
time.sleep(0.1)
clear()
print("    (                      )")
time.sleep(0.1)
clear()
print("     (                    )")
time.sleep(0.1)
clear()
print("      (                  )")
time.sleep(0.1)
clear()
print("       (                )")
time.sleep(0.1)
clear()
print("        (              )")
time.sleep(0.1)
clear()
print("         (            )")
time.sleep(0.1)
clear()
print("          (          )")
time.sleep(0.1)
clear()
print("           (        )")
time.sleep(0.1)
clear()
print("            (      )")
time.sleep(0.1)
clear()
print("             (    )")
time.sleep(0.1)
clear()
print("              (  )")
time.sleep(0.1)
clear()
print("               ()")
time.sleep(0.1)
clear()
print("               O")
time.sleep(0.1)
clear()
print("             O")
time.sleep(0.1)
clear()
print("           O")
time.sleep(0.1)
clear()
print("         O")
time.sleep(0.1)
clear()
print("       O")
time.sleep(0.1)
clear()
print("     o")
time.sleep(0.1)
clear()
print("   o")
time.sleep(0.1)
clear()
print(" o")
time.sleep(0.1)
clear()
print("o")
time.sleep(0.1)
clear()
print("oa")
time.sleep(0.1)
clear()
print("oas")
time.sleep(0.1)
clear()
print("oasi")
time.sleep(0.1)
clear()
print("oasis")
time.sleep(5)
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
	set_password = getpass("password - ")
	clear()
	pf = open(PASSWORD_FILE, 'w')
	pf.write(set_password)
	pf.close()
	clear()
	print("Success! oasis is all set up!")
	print("Reading data...")
	name, password = read_data()
	print("oasis {} - type \"help\" for a list of commands".format(oasisVersion))
	print("Welcome to oasis, {}!".format(name))
else:
	print("Reading data...")
	name, password = read_data()
	try_password = getpass("Please enter the password for {}. ".format(name))
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
			print("editor - a work in progress text editor")
			print("about - about your copy of oasis")
			print("update - checks for oasis updates")
			print("music - plays music you upload")
			print("lock - locks oasis until you enter your password")

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
			clear()
			print("Console cleared!")

		if command == "quit":
			clear()
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

		if command == "about":
			print("oasis {} running on {}.".format(oasisVersion, os.uname()[1]))
			print("Written in the Python programming language")
			print("Coded in the Atom, TextWrangler, and Xcode text editors")

		if command == "update":
			for line in urllib2.urlopen(TARGET_URL):
				version = line
			print("The latest version of oasis is {}".format(version))
			print("You are running {}".format(current_version))

		if command == "music":
			print("To add music, locate to the files folder and place your music there.")
			MUSIC_FILE = raw_input("What is the song saved as? ex. Masked_Heroes.mp3 ")
			afplay.afplay("files/{}".format(MUSIC_FILE))

		if command == "lock":
			clear()
			tries = 0
			while tries < 3:
				unlock = getpass("Password for {}: ".format(name))
				if unlock == password:
					clear()
					print("Welcome back, {}.".format(name))
					break
				else:
					tries += 1
			else:
				clear()
				print("Password entered incorrectly 3 times.")
				print("Shutting down...")
				sys.exit(0)

	except KeyboardInterrupt:
		continue
