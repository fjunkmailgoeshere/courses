#!/usr/bin/python

import os, string

def rename_files(path):
	saved_path = os.getcwd()

	#1 get file names from folder
	file_list = os.listdir(path+"/")
	os.chdir(saved_path+"/"+path)
	print file_list

	#2 for each file, rename filename
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))

	os.chdir(saved_path)
rename_files("message")
