from exif import Image
from os import path
from datetime import datetime

# import os

def main():
	folder_path = '' # input path to files
	os.chdir(folder_path)
	files = os.listdir(folder_path)
	print(files)
	files = exif_file_sorter(files)
	print(files)

def exif_file_sorter(files):
	return sorted(files, key=get_exif_timestamp)

def get_exif_timestamp(file):
	timestamp = exif_datetime(file)
	if timestamp is not None:
		return timestamp
	else:
		return path.getmtime(file)

def exif_datetime(file):
	try:
		with open(file, 'rb') as image_file:
			image_date_str = Image(image_file).datetime_original
			image_date = datetime.strptime(image_date_str, '%Y:%m:%d %H:%M:%S')
			return datetime.timestamp(image_date)
	except:
		return None

if __name__ == '__main__':
    main()