#!/usr/bin/python
import urllib

def read_text():
	quotes = open("words.txt")
	contents_of_file = quotes.read()
	print contents_of_file
	quotes.close()
	return contents_of_file

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.isithackday.com/arrpi.php?text="+text_to_check)
	output = connection.read()
	print output
	connection.close()


contents_of_file = read_text()
check_profanity(contents_of_file)
