#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  picture_namer.py
#  
#  Copyright 2018 sky5hr0ud <sky5hr0ud>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Script modified to enable better functionality.

import os
import sys

def main():
	path = input('Folder path: ')
	os.chdir(path)
	file_namer(path)
	return 0

def file_namer(path):
	count = file_counter()
	for file in sorted(os.listdir('.')):
		if file.endswith(('.jpg','.png','.mp4','.jpeg','.JPG','.JPEG','.dng','.DNG')):
			rel_path = os.path.relpath(".","..").replace(" ","_")
			if file.startswith(rel_path):
				continue
			else:
				print (file)
				new_file = os.path.relpath(".", "..") + '_'
				new_file = new_file.replace(" ", "_")
				new_file = new_file + str(count).zfill(5) + '_'
				os.rename(file, new_file+file)
				count = count + 1
			
def file_counter(): #returns the number of files in a directory
	count = 0
	for file in os.listdir('.'):
		#if file.startswith(os.path.relpath(".","..")):
		rel_path = os.path.relpath(".","..").replace(" ","_")
		if file.startswith(rel_path):
			count = count + 1
	return count

main()
