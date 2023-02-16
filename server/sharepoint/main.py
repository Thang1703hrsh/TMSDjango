# Google drive backup

# Upload files to google drive
# List files in google drive
# Download files from google drive

# pip install pydrive

import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1cb1vIJsedV5Hpl_ZZFaJV3ageK-rFmKC'


# Upload files
directory = "/home/tranthang/Desktop/djangoTMS/data_complete"


# for f in os.listdir(directory):
# 	filename = os.path.join(directory, f)
# 	gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
# 	gfile.SetContentFile(filename)
# 	gfile.Upload()

# file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
# print(file_list)
 
 
# for x in range(len(file_list)):
#     if file_list[x]['title'] == file_name:
#         file_id = file_list[x]['id']

# file1 = drive.CreateFile({'id':file_id})
# file1.SetContentFile('file_name')
# file1.Upload()
file_list = drive.ListFile({'q':"'1cb1vIJsedV5Hpl_ZZFaJV3ageK-rFmKC'  in parents and  trashed=False"}).GetList()


for f in os.listdir(directory):
	filename = os.path.join(directory, f)
	
	if len(file_list) == 0 :
		gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
		gfile.SetContentFile(filename)
		gfile.Upload()
	else:
		for x in range(len(file_list)):
			print(file_list[x]['title'])
			if file_list[x]['title'] == filename:
				file_id = file_list[x]['id']
				file_id.Delete()
				f = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
				f.SetContentFile(filename)
				f.Upload()
			else:
				f = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
				f.SetContentFile(filename)
				f.Upload()
    
    
	# gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
	# gfile.SetContentFile(filename)
	# gfile.Upload()
 
 
 