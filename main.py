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
import readline

readline.parse_and_bind('set editing-mode vi')

# Set to False to turn off animations
ANIMATION = True
DOT = False

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
GUEST_MESSAGE_FILE = 'data/settings/guest_message.txt'

TARGET_URL = 'http://thelukeguy.github.io/oasis_update_check/'

oasisVersion = "3.1"
current_version = "oasis {} (12/12/16)".format(oasisVersion)

def read_data():
	with open(NAME_FILE, "r") as nf:
		name = ''.join(nf.readlines())
	with open(PASSWORD_FILE, "r") as pf:
		password = ''.join(pf.readlines())
		password = decrypt("oasis", password)
		password = password.decode('utf8')
	with open(GUEST_MESSAGE_FILE, "r") as gmf:
		guest_message = ''.join(gmf.readlines())
	return (name, password, guest_message)

clear()

def do_animation():
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

if ANIMATION:
	do_animation()

if DOT:
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
	name, password, guest_message = read_data()
	print("oasis {} - type \"help\" for a list of commands".format(oasisVersion))
	print("Welcome to oasis, {}!".format(name))
	mode = name
else:
	print("Reading data...")
	name, password, guest_message = read_data()
	print("users - {}, guest".format(name))
	mode = raw_input("name - ")
	if mode == "guest":
		clear()
		print(guest_message)
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

if mode == "guest":
	commands = ["help", "reset", "animation", "calculator", "clear", "quit", "about", "update", "xmas", "convert", "piglatin", "reload", "python"]
else:
	commands = ["help", "reset", "animation", "calculator", "clear", "quit", "text", "about", "update", "music", "lock", "xmas", "convert", "piglatin", "books", "downloader", "settings", "reload", "python"]

readline.clear_history()

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
				print("piglatin - a simple pig latin translator")
				print("reload - reloads oasis")
				print("python - execute Python code")
				raise KeyboardInterrupt

			print("Available commands:")
			print("calculator - a basic calculator")
			print("clear - clears console")
			print("quit - quits oasis")
			print("text - save text to a local file")
			print("about - about your copy of oasis")
			print("update - checks for oasis updates")
			print("music - plays music you upload")
			print("lock - locks oasis until you enter your password")
			print("xmas - {} Christmas countdown".format(year))
			print("convert - simple math conversions")
			print("piglatin - a simple pig latin translator")
			print("books - read downloaded e-books")
			print("downloader - download files required by certain programs")
			print("settings - configure oasis to your liking")
			print("reload - reloads oasis")
			print("python - execute Python code")

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

		if command == "text":
			if mode == "guest":
				raise KeyboardInterrupt
			print("files are saved to \"files\" folder")
			text = raw_input("text > ")
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
			try:
				for line in urllib2.urlopen(TARGET_URL):
					version = line
			except:
				print("error - could not connect to \"http://thelukeguy.github.io/oasis_update_check/\"")
				raise KeyboardInterrupt
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
				print("error - this conversion is work in progress")
				raise KeyboardInterrupt

		if command == "animation":
			do_animation()
			print("played animation")

		if command == "piglatin":
			tofrom = raw_input("translate (to/from) pig latin - ")
			if tofrom not in ["to", "from"]:
				print("error - invalid input")
				raise KeyboardInterrupt
			if tofrom == "to":
				firstpl = raw_input("convert what to pig latin - ")
				secondpl = firstpl[0]
				thirdpl = firstpl[1:]
				answer = "{}{}ay".format(thirdpl, secondpl)
				print("{} in pig latin is {}".format(firstpl, answer))
			elif tofrom == "from":
				firstpl = raw_input("convert what from pig latin - ")
				getlettersbefore = len(firstpl) - 3
				secondpl = firstpl[:getlettersbefore]
				thirdpl = firstpl[getlettersbefore]
				answer = "{}{}".format(thirdpl, secondpl)
				print("{} from pig latin is {}".format(firstpl, answer))

		if command == "books":
			if mode == "guest":
				raise KeyboardInterrupt
			print("store books in \"files\" folder")
			print("books downloaded using the downloader are saved as [title]-[author].txt")
			BOOK_FILE = raw_input("book file - ")
			try:
				with open("files/{}".format(BOOK_FILE), "r") as bf:
					book = bf.read()
			except IOError:
				print("error - unknown file")
				raise KeyboardInterrupt
			clear()
			print("entering book mode - to exit, press enter or return")
			print("\n")
			print(book)
			raw_input()
			clear()
			print("exiting book mode")

		if command == "downloader":
			if mode == "guest":
				raise KeyboardInterrupt
			else:
				TARGET_URL = raw_input("download url - ")
				book_download = []
				try:
					for line in urllib2.urlopen(TARGET_URL):
						book_download.append(line)
				except:
					print("error - invalid url")
					raise KeyboardInterrupt
				book_title = book_download[0]
				book_author = book_download[1]
				book_download = book_download[2:]
				NEW_BOOK_FILE = "{}-{}.txt".format(book_title.strip(), book_author.strip())
				book_download_length = len(book_download)
				book_download_str = "".join(book_download)
				open("files/{}".format(NEW_BOOK_FILE), 'a').close()
				with open("files/{}".format(NEW_BOOK_FILE), 'w') as nbf:
					nbf.write(book_download_str)
				print("success - download")

		if command == "settings":
			print("Settings:")
			print("setpass - change your password to oasis")
			print("guestmessage - change the guest login message")
			print("\n")
			setting = raw_input("setting - ")
			if setting == "setpass":
				clear()
				if getpass("old password - ") == password:
					clear()
					while True:
						set_password = getpass("new password - ")
						clear()
						password_confirm = getpass("confirm new password - ")
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
					print("success - change password")
					time.sleep(3)
					clear()
					print("reloading oasis in 5")
					time.sleep(1)
					clear()
					print("reloading oasis in 4")
					time.sleep(1)
					clear()
					print("reloading oasis in 3")
					time.sleep(1)
					clear()
					print("reloading oasis in 2")
					time.sleep(1)
					clear()
					print("reloading oasis in 1")
					time.sleep(1)
					clear()
					print("reloading oasis...")
					time.sleep(3)
					clear()
					read_data()
					clear()
					print("success - reload")
					raise KeyboardInterrupt

				else:
					print("error - incorrect password")
					raise KeyboardInterrupt

			elif setting == "guestmessage":
				with open(GUEST_MESSAGE_FILE, "w") as gmf:
					gmf.write(raw_input("new message - "))
				print("success - change guest message")

			else:
				print("error - invalid setting")
				raise KeyboardInterrupt

		if command == "reload":
			clear()
			print("reloading oasis - this may take a moment")
			read_data()
			clear()
			print("success - reload")

		if command == "python":
			clear()
			print("oasis Python interpreter")
			print("---")
			print("for things that require two lines such as if statements")
			print("which have a colon at the end, use a space for a new line")
			print("---")
			print("type \"quit\" to exit")
			print("\n")
			while True:
				to_exec = raw_input("py> ")
				if to_exec == "quit":
					clear()
					print("exited Python interpreter")
					break
				elif to_exec[0:5] == "name=" or to_exec[0:6] == "name =":
					print("[oasis] error - you can not change name variable")
				elif to_exec[0:9] == "password=" or to_exec[0:10] == "password =":
					print("[oasis] error - you can not change password variable")
				elif to_exec[0:5] == "mode=" or to_exec[0:6] == "mode ="
					print("[oasis] error - you can not change mode variable")
				else:
					try:
						exec(to_exec)
					except Exception as e:
						print("error - {}".format(e))
				print("\n")

		if not command in commands:
			print("invalid command - type \"help\" for a list of commands")

	except KeyboardInterrupt:
		continue
