#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  picture_namer.py
#
#  Copyright 2022 sky5hr0ud <sky5hr0ud>
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
#  This script prepends the directory name to picture filenames.
#  Picture filenames are read in from list_of_filetypes.txt.

import os
import argparse
import sys


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-f', '--filename', help='Sort by filename', action='store_true')
        parser.add_argument(
            '-m', '--moddate', help='Sort by file modified date',
            action='store_true')
        parser.add_argument(
            '-p', '--folderpath', type=str, help='Add a path to the folder')
        parser.add_argument(
            '-i', '--input', help='Disable user input',
            action='store_false')
        parser.add_argument(
            '-l', '--list', type=str, help='Use a custom list of filetypes')
        parser.add_argument(
            '-e', '--explicit', help='Don\'t ignore letter case in filetypes',
            action='store_false')
        args = parser.parse_args()
        if args.folderpath:
            folder_path = args.folderpath
            if folder_path.endswith('"'):  # remove " from end if present
                folder_path = folder_path[:-1]
        elif args.input is True:
            folder_path = input('Folder path to images: ')
        filetypes_options = [False, args.list, args.explicit]
        if args.list:
            filetypes_options[0] = True
        file_namer(
            folder_path, args.filename, args.moddate, args.input,
            filetypes_options)
    except Exception as e:
        print(e)
    if args.input is True:
        try:
            input('Press Enter to exit...')
        except Exception as e:
            print(e)
    return 0


# generate clean list of filenames
def list_of_filetypes_modifier(arginput, filetypes_options):
    list_of_filetypes = get_filetypes(arginput, filetypes_options)
    clean_list = clean_list_of_filetypes(list_of_filetypes)
    new_list_of_filetypes = []
    if filetypes_options[2] is False:
        new_list_of_filetypes = clean_list
    else:
        for filetype in clean_list:
            uppercase = filetype.upper()
            lowercase = filetype.lower()
            new_list_of_filetypes.append(uppercase)
            new_list_of_filetypes.append(lowercase)
    return new_list_of_filetypes


def read_file(file_path):
    file = open(file_path, 'r')
    read_file = file.readlines()
    file.close()
    return read_file


def get_filetypes(arginput, filetypes_options):
    default_filetype_filename = '_list_of_filetypes.txt'
    default_filetype_list = (
        ['.jpg', '.png', '.mp4', '.jpeg', '.dng', '.gif', '.nef', '.bmp'])
    try:
        if filetypes_options[0] is True:
            if os.path.isfile(filetypes_options[1]):
                print('Using ' + filetypes_options[1])
                return read_file(filetypes_options[1])
        elif os.path.isfile(default_filetype_filename):
            print('Using ' + default_filetype_filename)
            return read_file(default_filetype_filename)
        # This code is for when a .exe created by Pyinstaller is used.
        # Pyinstaller will create a temp folder and stores the path in _MEIPASS
        try:
            if os.path.isfile(sys._MEIPASS + '\\' + default_filetype_filename):
                return read_file(
                    sys._MEIPASS + '\\' + default_filetype_filename)
        except Exception as e:
            print(e)
            print('sys._MEIPASS only exists if .exe file is ran')
        if arginput is True:
            print('Error: ' + default_filetype_filename + ' not found.')
            file_path = input('Input path to txt file containing filetypes: ')
        if os.path.isfile(file_path):
            print('Using filetypes list: ' + file_path.rsplit('\\', 1)[-1])
            return read_file(file_path)
        elif os.path.isfile(file_path + default_filetype_filename):
            print('Using ' + default_filetype_filename + ' at ' + file_path)
            return read_file(file_path + default_filetype_filename)
        elif os.path.isfile(file_path + '\\' + default_filetype_filename):
            print('Using ' + default_filetype_filename + ' at ' + file_path)
            return read_file(file_path + '\\' + default_filetype_filename)
        else:
            print('Warning: Cannot find file. Using default list instead.')
            return default_filetype_list
    except Exception as e:
        print(e)
        print('Warning: Using default list instead.')
        return default_filetype_list


def clean_list_of_filetypes(list_of_filetypes):
    clean_list_of_filetypes = []
    for filetype in list_of_filetypes:
        filetype = filetype.replace(' ', '')
        comment_c = filetype.find('//')
        comment_py = filetype.find('#')
        if comment_c >= 0 or comment_py >= 0:
            if comment_c == 0 or comment_py == 0:
                continue
            elif comment_c < comment_py or comment_py == (-1):
                clean_list_of_filetypes.append(filetype[:comment_c])
            else:
                clean_list_of_filetypes.append(filetype[:comment_py])
        else:
            clean_list_of_filetypes.append(filetype.replace('\n', ''))
    return clean_list_of_filetypes


def zero_padder(lead_zeros, count):
    if len(str(count)) >= lead_zeros:
        lead_zeros = len(str(count)) + 2
    return lead_zeros


def file_counter(filetypes):  # returns the number of files in a directory
    count = 0
    for file in os.listdir('.'):
        if os.path.isfile(file):
            if file.endswith(tuple(filetypes)):
                rel_path = os.path.relpath('.', '..').replace(' ', '_')
                if file.startswith(rel_path):
                    count = count + 1
        else:
            continue
    return count


# file_namer(directory path, filename sort, date modified sort, user input,
#   array[filetypes list exists, filetypes list, explicit case option])
def file_namer(folder_path, argfilename, argmoddate, arginput,
               filetypes_options):
    files_renamed = 0
    filetypes = list_of_filetypes_modifier(arginput, filetypes_options)
    try:
        os.chdir(folder_path)
    except Exception as e:
        print('Error with inputted path.', e, 'occurred.')
        return
    count = file_counter(filetypes)
    lead_zeros = zero_padder(5, count)  # Ensures leading zeros
    files = os.listdir('.')
    if argfilename is True:
        files = sorted(files)
    elif argmoddate is True:
        files = sorted(files, key=os.path.getmtime)
    else:
        files = sorted(files, key=os.path.getmtime)
    for file in files:
        if os.path.isfile(file):
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
                    files_renamed = files_renamed + 1
        else:
            continue
    print('Renamed', files_renamed, 'files.')
    return


if __name__ == '__main__':
    main()
