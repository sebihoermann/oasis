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

#development_build()

FIRST_BOOT_FILE = 'data/extra/first_boot.txt'
NAME_FILE = 'data/profile/name.txt'
PASSWORD_FILE = 'data/profile/password.txt'
GUEST_MESSAGE_FILE = 'data/settings/guest_message.txt'
ALIAS_FILE = 'data/settings/aliases.txt'

TARGET_URL = 'http://thelukeguy.github.io/oasis_update_check/'

oasisVersion = "3.2.1"
current_version = "oasis {} (2/9/17)".format(oasisVersion)

def read_data():
	with open(NAME_FILE, "r") as nf:
		name = ''.join(nf.readlines())
	with open(PASSWORD_FILE, "r") as pf:
		password = ''.join(pf.readlines())
		password = decrypt("oasis", password)
		password = password.decode('utf8')
	with open(GUEST_MESSAGE_FILE, "r") as gmf:
		guest_message = ''.join(gmf.readlines())
	with open(ALIAS_FILE, "r") as af:
		aliases = af.readlines()
		alias = {}
		for i in aliases:
			current_alias = i.find(":")
			current_alias = i[:current_alias]
			current_command = i.find(":") + 1
			current_command = i[current_command:]
			alias[current_alias] = current_command

	return (name, password, guest_message, alias)

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
	time.sleep(3)
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
	clear()
	print("A")
	time.sleep(0.1)
	clear()
	print("Au")
	time.sleep(0.1)
	clear()
	print(" ur")
	time.sleep(0.1)
	clear()
	print("  ro")
	time.sleep(0.1)
	clear()
	print("   or")
	time.sleep(0.1)
	clear()
	print("    ra")
	time.sleep(0.1)
	clear()
	print("     a")
	clear()
	time.sleep(1)
	print("A")
	time.sleep(0.1)
	clear()
	print("Au")
	time.sleep(0.1)
	clear()
	print("Aur")
	time.sleep(0.1)
	clear()
	print("Auro")
	time.sleep(0.1)
	clear()
	print("Auror")
	time.sleep(0.1)
	clear()
	print("Aurora")
	time.sleep(3)

if ANIMATION:
	do_animation()

if not os.path.isfile(FIRST_BOOT_FILE):
	clear()
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
	name, password, guest_message, alias = read_data()
	print("oasis {} - type \"help\" for a list of commands".format(oasisVersion))
	print("Welcome to oasis, {}!".format(name))
	mode = name
else:
	print("Reading data...")
	name, password, guest_message, alias = read_data()
	clear()
	print("Reading data...")
	print("users - {}, guest".format(name))
	mode = raw_input("name - ")
	if mode == "guest":
		clear()
		print(guest_message)
		print("oasis {} - type \"help\" for a list of commands".format(oasisVersion))

	elif mode == name:
		tries = 0
		while tries < 3:
			try_password = getpass("password for {} - ".format(name))
			if try_password == password:
				clear()
				print("oasis {} - type \"help\" for a list of commands".format(oasisVersion))
				print('Welcome back, {}!'.format(name))
				break
			else:
				print("Incorrect password")
				tries += 1
		else:
			print("Multiple failed attempts")
			sys.exit(1)

	else:
		clear()
		print("error - unknown user")
		sys.exit(1)

if mode == "guest":
	commands = ["help", "reset", "animation", "calculator", "clear", "quit", "about", "update", "xmas", "convert", "piglatin", "reload", "python", "stopwatch", "rps"]
else:
	commands = ["help", "reset", "animation", "calculator", "clear", "quit", "text", "about", "update", "music", "lock", "xmas", "convert", "piglatin", "books", "downloader", "settings", "reload", "python", "stopwatch", "rps"]

if not mode == "guest":
	for i in alias:
		commands.append(i)

readline.clear_history()

runalias = False

while True:
	try:
		print("\n")
		if runalias:
			runalias = False
		else:
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
				print("stopwatch - a simple stopwatch")
				print("rps - rock, paper, scissors")
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
			print("stopwatch - a simple stopwatch")
			print("rps - rock, paper, scissors")

			for i in alias:
				if not i.strip() == "":
					print("{} - alias for \"{}\"".format(i.strip(), alias[i.strip()].strip()))

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

		if command == "about-legacy":
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
			if not version == current_version:
				print("stable release available - {}".format(version))
			else:
				print("oasis is up to date")

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
			print("setalias - add a command alias")
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

			elif setting == "setalias":
				get_aliases = []
				with open(ALIAS_FILE, "r") as af:
					get_aliases = af.readlines()
					af.close()
				with open(ALIAS_FILE, "w") as af:
					get_aliases.append("{}:{}".format(raw_input("Alias: "), raw_input("Command: ")))
					af.write("\n".join(get_aliases))
				print("success - add alias")
				print("for changes to take effect, you must restart oasis")
				while True:
					restart = raw_input("restart now? (y/n) ")
					if restart == "y":
						clear()
						print("to start - \"python main.py\"")
						sys.exit(0)
					elif restart == "n":
						break
					else:
						print("invalid input")
						time.sleep(1)
						print("\n")

			else:
				print("error - invalid setting")
				raise KeyboardInterrupt

		if command == "reload":
			clear()
			print("reloading oasis - this may take a moment")
			read_data()
			name, password, guest_message, alias = read_data()
			clear()
			print("success - reload")

		if command == "python":
			if mode == "guest":
				raise KeyboardInterrupt
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
				elif to_exec[0:5] == "mode=" or to_exec[0:6] == "mode =":
					print("[oasis] error - you can not change mode variable")
				else:
					try:
						exec(to_exec)
					except Exception as e:
						print("error - {}".format(e))
				print("\n")

		if command == "":
			raise KeyboardInterrupt

		if command in alias:
			if mode == "guest":
				raise KeyboardInterrupt
			runalias = True
			command = alias[command]
			command = command.strip()

		if command == "stopwatch":
			clear()
			print("Stopwatch")
			print("\n")
			print("Use ctrl + C to stop stopwatch")
			raw_input("Press enter to begin")
			clear()
			hours = 0
			minutes = 0
			seconds = 0
			try:
				while True:
					time.sleep(1)
					if str(seconds) == "59":
						minutes += 1
						seconds = 0
					elif str(minutes) == "59":
						hours += 1
						minutes = 0
					else:
						seconds += 1
					clear()
					if hours < 10:
						printableh = "0{}".format(str(hours))
					else:
						printableh = str(hours)
					if minutes < 10:
						printablem = "0{}".format(str(minutes))
					else:
						printablem = str(minutes)
					if seconds < 10:
						printables = "0{}".format(str(seconds))
					else:
						printables = str(seconds)
					print("{}:{}:{}".format(printableh, printablem, printables))
			except KeyboardInterrupt:
				clear()
				print("{}:{}:{}".format(printableh, printablem, printables))

		if command == "rps":
			print("mode - (1) against computer or (2) multiplayer")
			rpsmode = raw_input()
			if rpsmode not in ["1", "2"]:
				print("Invalid input")
				raise KeyboardInterrupt
			elif rpsmode == "1":
				while True:
					rps = raw_input("rock, paper, or scissors? ")
					if not rps in ["rock", "paper", "scissors"]:
						print("Invalid input")
						pass
					else:
						cpu = random.choice(["rock", "paper", "scissors"])
						print("computer chooses {}".format(cpu))
						if rps == cpu:
							print("tie game")
							print("\n")
						elif rps == "rock" and cpu == "paper":
							print("computer wins")
							print("\n")
						elif rps == "paper" and cpu == "rock":
							print("player wins")
							print("\n")
						elif rps == "paper" and cpu == "scissors":
							print("computer wins")
							print("\n")
						elif rps == "scissors" and cpu == "paper":
							print("player wins")
							print("\n")
						elif rps == "scissors" and cpu == "rock":
							print("computer wins")
							print("\n")
						elif rps == "rock" and cpu == "scissors":
							print("player wins")
							print("\n")
			else:
				while True:
					p1 = getpass("P1: rock, paper, or scissors? ")
					if not p1 in ["rock", "paper", "scissors"]:
						print("Invalid input")
						pass
					else:
						p2 = getpass("P2: rock, paper, or scissors? ")
						if not p2 in ["rock", "paper", "scissors"]:
							print("Invalid input")
							pass
						else:
							print("P1 picked {}".format(p1))
							print("P2 picked {}".format(p2))
							if p1 == p2:
								print("tie game")
								print("\n")
							elif p1 == "rock" and p2 == "paper":
								print("P2 wins")
								print("\n")
							elif p1 == "paper" and p2 == "rock":
								print("P1 wins")
								print("\n")
							elif p1 == "paper" and p2 == "scissors":
								print("P2 wins")
								print("\n")
							elif p1 == "scissors" and p2 == "paper":
								print("P1 wins")
								print("\n")
							elif p1 == "scissors" and p2 == "rock":
								print("P2 wins")
								print("\n")
							elif p1 == "rock" and p2 == "scissors":
								print("P1 wins")
								print("\n")

		if command == "about":
			clear()
			time.sleep(5)
			print("o")
			time.sleep(0.1)
			clear()
			print("oa")
			time.sleep(0.1)
			clear()
			print(" as")
			time.sleep(0.1)
			clear()
			print("  si")
			time.sleep(0.1)
			clear()
			print("   is")
			time.sleep(0.1)
			clear()
			print("    s")
			clear()
			time.sleep(1)
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
			time.sleep(3)
			clear()
			print("oasis")
			time.sleep(2)
			print("version {}".format(oasisVersion))
			time.sleep(3)
			print("\n")
			print("a project by TheLukeGuy")
			time.sleep(2)
			print("formally known as tlgOS")
			time.sleep(2)
			print("started late 2015")
			time.sleep(2)
			print("coded in Atom, TextWrangler, and Xcode")
			time.sleep(2)
			print("coded on two different MacBook Pros and a Mac mini")
			time.sleep(3)
			print("\n")
			print("website: http://lukepchambers.net/oasis")
			time.sleep(2)
			print("GitHub: https://github.com/TheLukeGuy/oasis")
			print("\n")
			time.sleep(3)
			print("press enter to exit")
			raw_input()
			clear()
			raise KeyboardInterrupt

		if not command in commands:
			print("invalid command - {} - type \"help\" for a list of commands".format(command))

	except KeyboardInterrupt:
		continue
