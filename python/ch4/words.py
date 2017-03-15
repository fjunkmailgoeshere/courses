#!/usr/bin/python
import urllib

def read_text():
	quotes = open("words.txt")
	contents_of_file = quotes.read()
	print contents_of_file
	quotes.close()
	return contents_of_file

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	if output == "true":
		print "Profanity Alert!"
	else:
		print "This text is OK!"
	connection.close()


contents_of_file = read_text()
check_profanity(contents_of_file)
