#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
from fractions import Fraction
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
import datetime

# Set to False to turn off animation
animation = True
dot = True


now = datetime.datetime.now()
year = now.year

try:
	import console
	def clear():
		console.clear()
except ImportError:
	def clear():
		os.system('clear')

try:
	from simplecrypt import encrypt, decrypt
except ImportError:
	clear()
	print("missing - simple-crypt")
	sys.exit(1)

def development_build():
	clear()
	bootup = raw_input("development builds may contain bugs - boot? (y/n) ")
	if bootup == "n":
		clear()
		sys.exit(0)
	elif bootup not in ["y", "n"]:
		clear()
		print("invalid answer")
		sys.exit(1)
	clear()

development_build()

FIRST_BOOT_FILE = 'data/extra/first_boot.txt'
NAME_FILE = 'data/profile/name.txt'
PASSWORD_FILE = 'data/profile/password.txt'

TARGET_URL = 'http://thelukeguy.github.io/oasis_update_check/'

oasisVersion = "3.0-dev4 Aurora"
current_version = "oasis {} (11/15/16)".format(oasisVersion)

def read_data():
	with open(NAME_FILE, "r") as nf:
		name = ''.join(nf.readlines())
	with open(PASSWORD_FILE, "r") as pf:
		password = ''.join(pf.readlines())
		password = decrypt("oasis", password)
		password = password.decode('utf8')
	return (name, password)

clear()

if animation:
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
	print("oasi")
	time.sleep(0.1)
	clear()
	time.sleep(0.1)
	clear()
	print("oas")
	time.sleep(0.1)
	clear()
	print("oa")
	time.sleep(0.1)
	clear()
	print("o")
	time.sleep(0.1)
	clear()
	time.sleep(3)

if dot:
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
	while True:
		set_password = getpass("password - ")
		clear()
		password_confirm = getpass("confirm password - ")
		if password_confirm == set_password:
			clear()
			break
		else:
			clear()
			print("passwords do not match")
			time.sleep(3)
		clear()
	print("please wait - encoding password")
	set_password = encrypt("oasis", set_password.encode('utf8'))
	pf = open(PASSWORD_FILE, 'w')
	pf.write(set_password)
	pf.close()
	clear()
	print("setup - success")
	print("Reading data...")
	name, password = read_data()
	print("oasis {} - type \"help\" for a list of commands".format(oasisVersion))
	print("Welcome to oasis, {}!".format(name))
	mode = name
else:
	print("Reading data...")
	name, password = read_data()
	print("users - {}, guest".format(name))
	mode = raw_input("name - ")
	if mode == "guest":
		clear()
		print("logged in as a guest")
		print("oasis {} - type \"help\" for a list of commands".format(oasisVersion))

	elif mode == name:
		try_password = getpass("password for {} - ".format(name))
		if try_password == password:
			clear()
			print("oasis {} - type \"help\" for a list of commands".format(oasisVersion))
			print('Welcome back, {}!'.format(name))
		else:
			print("Incorrect password")
			sys.exit(1)

	else:
		clear()
		print("error - unknown user")
		sys.exit(1)

while True:
	try:
		print("\n")
		command = raw_input("> ")
		if command == "help":
			if mode == "guest":
				print("Available commands:")
				print("calculator - a basic calculator")
				print("clear - clears console")
				print("quit - quits oasis")
				print("about - about your copy of oasis")
				print("update - checks for oasis updates")
				print("xmas - {} Christmas countdown".format(year))
				print("convert - simple math conversions")
				raise KeyboardInterrupt

			print("Available commands:")
			print("calculator - a basic calculator")
			print("clear - clears console")
			print("quit - quits oasis")
			print("editor - a work in progress text editor")
			print("about - about your copy of oasis")
			print("update - checks for oasis updates")
			print("music - plays music you upload")
			print("lock - locks oasis until you enter your password")
			print("xmas - {} Christmas countdown".format(year))
			print("convert - simple math conversions")

		if command == "calculator":
			print("pyCalc v2.0")
			try:
				v1 = int(raw_input("first value - "))
			except ValueError:
				print("{} is not a number".format(v1))
				sys.exit(1)
			operation = raw_input("operation - ")
			if operation not in ["+","-","*","/"]:
				print("{} is not a valid operation".format(operation))
				continue
			try:
				v2 = int(raw_input("second value - "))
			except ValueError:
				print("{} is not a number".format(v2))
				sys.exit(1)
			print("solving...")
			if operation == "+":
				answer = int(v1+v2)
			if operation == "-":
				answer = int(v1-v2)
			if operation == "*":
				answer = int(v1*v2)
			if operation == "/":
				answer = int(v1/v2)
			print("{} {} {} = {}".format(v1, operation, v2, answer))

		if command == "clear":
			clear()
			print("console cleared")

		if command == "quit":
			clear()
			if mode == "guest":
				print("Farewell until we meet again!")
				sys.exit(0)
			print("Farewell until we meet again, {}!".format(name))
			sys.exit(0)

		if command == "reset":
			if mode == "guest":
				raise KeyboardInterrupt
			print("reset - type \"python reset.py\" in console")

		if command == "editor":
			if mode == "guest":
				raise KeyboardInterrupt
			print("still in beta - you cannot:")
			print("open files")
			print("get a new line")
			print("---")
			print("files are saved to \"files\" folder")
			text = raw_input("editor > ")
			while True:
				editorchoice = raw_input("save / discard file - ")
				if editorchoice == "save":
					save_as = raw_input("save file as - ")
					TEXT_FILE = 'files/{}'.format(save_as)
					tf = open(TEXT_FILE, 'w')
					tf.write(text)
					tf.close()
					print("success - save")
					break
				elif editorchoice == "discard":
					break
				else:
					print("error - invalid answer")
					time.sleep(3)

		if command == "about":
			print("oasis {} running on {}.".format(oasisVersion, os.uname()[1]))
			print("written in Python")
			print("coded in Atom, TextWrangler, and Xcode")

		if command == "update":
			for line in urllib2.urlopen(TARGET_URL):
				version = line
			print("latest - {}".format(version))
			print("running - {}".format(current_version))

		if command == "music":
			if mode == "guest":
				raise KeyboardInterrupt
			print("store music in \"files\" folder")
			MUSIC_FILE = raw_input("music file - ")
			afplay.afplay("files/{}".format(MUSIC_FILE))

		if command == "lock":
			if mode == "guest":
				raise KeyboardInterrupt
			clear()
			tries = 0
			while tries < 3:
				unlock = getpass("password for {} - ".format(name))
				if unlock == password:
					clear()
					print("Welcome back, {}!".format(name))
					break
				else:
					tries += 1
			else:
				clear()
				print("incorrect password 3 times")
				print("shutting down")
				sys.exit(0)

		if command == "xmas":
			months = 12 - now.month
			days = 25 - now.day
			if months == 1:
				month_format = "month"
			else:
				month_format = "months"
			if days == 1:
				day_format = "day"
			else:
				day_format = "days"
			print("Christmas {} is in only {} {} and {} {}!".format(year, months, month_format, days, day_format))

		if command == "convert":
			print("pyCalc convert v0.1")
			print("---")
			print("convert options - decimal, fraction, percent")
			convert1 = raw_input("convert what - ")
			if not convert1 in ["decimal", "fraction", "percent"]:
				print("error - invalid input")
				raise KeyboardInterrupt
			convert2 = raw_input("to what - ")
			if not convert2 in ["decimal", "fraction", "percent"]:
				print("error - invalid input")
				raise KeyboardInterrupt
			if convert1 == "fraction" and convert2 == "percent":
				numerator = raw_input("numerator - ")
				denominator = raw_input("denominator - ")
				answer = str(int(numerator) / int(denominator) * 100)
				print("{}/{} converted to a percent is {}".format(numerator, denominator, answer))
			elif convert1 == "decimal" and convert2 == "fraction":
				decimal = raw_input("decimal - ")
				answer = Fraction(float(decimal))
				print("{} converted to a fraction is {}".format(decimal, answer))
			else:
				print("error - this feature is work in progress")
				raise KeyboardInterrupt

	except KeyboardInterrupt:
		continue
