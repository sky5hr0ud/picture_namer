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
#  This script appends the folder name to picture filenames.

import os

list_of_filetypes = ['.jpg', '.png', '.mp4', '.jpeg', '.dng', '.gif']


def main():
    path = input('Folder path: ')
    os.chdir(path)
    file_namer(path)
    return 0


def list_of_filetypes_modifier():  # generate uppercase and lowercase filenames
    new_list_of_filetypes = []
    for filetype in list_of_filetypes:
        uppercase = filetype.upper()
        lowercase = filetype.lower()
        new_list_of_filetypes.append(uppercase)
        new_list_of_filetypes.append(lowercase)
    return new_list_of_filetypes


def file_namer(path):
    count = file_counter()
    lead_zeros = 5
    if len(str(count)) >= lead_zeros:
        lead_zeros = len(str(count)) + 2
    filetypes = list_of_filetypes_modifier()
    files = os.listdir('.')
    files = sorted(files, key=os.path.getmtime)
    for file in files:
        if file.endswith(tuple(filetypes)):
            rel_path = os.path.relpath('.', '..').replace(' ', '_')
            if file.startswith(rel_path):
                continue
            else:
                print(file)
                new_file = os.path.relpath('.', '..') + '_'
                new_file = new_file.replace(' ', '_')
                new_file = new_file + str(count).zfill(lead_zeros) + '_'
                os.rename(file, new_file + file)
                count = count + 1


def file_counter():  # returns the number of files in a directory
    filetypes = list_of_filetypes_modifier()
    count = 0
    for file in os.listdir('.'):
        if file.endswith(tuple(filetypes)):
            rel_path = os.path.relpath('.', '..').replace(' ', '_')
            if file.startswith(rel_path):
                count = count + 1
    return count


main()
