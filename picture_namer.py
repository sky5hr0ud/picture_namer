#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  picture_namer.py
#
#  Copyright 2021 sky5hr0ud <sky5hr0ud>
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
#  Picture filenames are read in from list_of_filetypes.txt.

import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--filename', help='Sort by filename', action='store_true')
    parser.add_argument(
        '-m', '--moddate', help='Sort by file modified date',
        action='store_true')
    parser.add_argument(
        '-p', '--folderpath', type=str, help='Add a path to the folder')
    args = parser.parse_args()
    if args.folderpath:
        path = args.folderpath
    else:
        path = input('Folder path: ')
    file_namer(path, args.filename, args.moddate)
    input('Press Enter to exit.')
    return 0


def list_of_filetypes_modifier():  # generate clean list of filenames
    list_of_filetypes = get_filetypes()
    clean_list = clean_list_of_filetypes(list_of_filetypes)
    new_list_of_filetypes = []
    for filetype in clean_list:
        uppercase = filetype.upper()
        lowercase = filetype.lower()
        new_list_of_filetypes.append(uppercase)
        new_list_of_filetypes.append(lowercase)
    return new_list_of_filetypes


def get_filetypes():
    default_filetype_list = (
        ['.jpg', '.png', '.mp4', '.jpeg', '.dng', '.gif', '.nef', '.bmp'])
    try:
        if (os.path.isfile('_list_of_filetypes.txt')):
            filetypes_file = open('_list_of_filetypes.txt', 'r')
            list_of_filetypes = filetypes_file.readlines()
            filetypes_file.close()
            return list_of_filetypes
        else:
            print('Error: _list_of_filetypes.txt not found.')
            path = input('Input path with txt file containing filetypes: ')
        if (os.path.isfile(path)):
            filetypes_file = open(path, 'r')
            list_of_filetypes = filetypes_file.readlines()
            filetypes_file.close()
            return list_of_filetypes
        else:
            print('Cannot find file. Using default list instead.')
            return default_filetype_list
    except Exception as e:
        print(e)
        print('Using default list instead.')
        return default_filetype_list


def clean_list_of_filetypes(list_of_filetypes):
    clean_list_of_filetypes = []
    for filetype in list_of_filetypes:
        filetype = filetype.replace(' ', '')
        comment_c = filetype.find('//')
        comment_py = filetype.find('#')
        if (comment_c >= 0 or comment_py >= 0):
            if (comment_c == 0 or comment_py == 0):
                continue
            elif (comment_c < comment_py or comment_py == (-1)):
                clean_list_of_filetypes.append(filetype[:comment_c])
            else:
                clean_list_of_filetypes.append(filetype[:comment_py])
        else:
            clean_list_of_filetypes.append(filetype.replace('\n', ''))
    return clean_list_of_filetypes


def file_namer(path, argfilename, argmoddate):
    count = file_counter()
    lead_zeros = 5
    if len(str(count)) >= lead_zeros:
        lead_zeros = len(str(count)) + 2
    filetypes = list_of_filetypes_modifier()
    os.chdir(path)
    files = os.listdir('.')
    if argfilename is True:
        files = sorted(files)
    elif argmoddate is True:
        files = sorted(files, key=os.path.getmtime)
    else:
        files = sorted(files, key=os.path.getmtime)
    for file in files:
        if file.endswith(tuple(filetypes)):
            rel_path = os.path.relpath('.', '..').replace(' ', '_')
            if file.startswith(rel_path):
                continue
            else:
                new_file = os.path.relpath('.', '..') + '_'
                new_file = new_file.replace(' ', '_')
                new_file = new_file + str(count).zfill(lead_zeros) + '_'
                print(file + ' -> ' + new_file + file)
                os.rename(file, new_file + file)
                count = count + 1
    print('Renamed', count, 'files.')


def file_counter():  # returns the number of files in a directory
    filetypes = list_of_filetypes_modifier()
    count = 0
    for file in os.listdir('.'):
        if file.endswith(tuple(filetypes)):
            rel_path = os.path.relpath('.', '..').replace(' ', '_')
            if file.startswith(rel_path):
                count = count + 1
    return count


if __name__ == '__main__':
    main()
