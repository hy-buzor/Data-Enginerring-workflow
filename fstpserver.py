# #you import os since its going to be a os operation and shutil module that will help us move the files

# import os
# import shutil


# #define the source folder files are stored and dest folder we will move files to.


# source_folder = input('C:/Users/user/Desktop/source_folder')
# destination_folder = input('C:/Users/user/Desktop/destination_folder')

# #define the file extension we want to copy
# extension = input('.csv')

# #loop through the folders, subfolders and files in the source folder


# for folders, subfolders, filenames in os.walk(source_folder):
#    #pick only the files to loop through 
#    for filename in filenames:

#      #check if the file matches the extension the{} is a bucket to store the files if it meets the extension 
#          if filename.endswith('{}'.format(extension)):
#      #code to copy the files 
#              shutil.copy(os.path.join(folders, filename), destination_folder)
#     #code to move the files 
# shutil.move(os.path.join(folders, filename), destination_folder)


# import os
# import shutil

# # Define the source folder where files are stored and the destination folder where we will move files to
# source_folder = 'C:/Users/user/Desktop/source folder'
# destination_folder = 'C:/Users/user/Desktop/destination folder'

# # Define the file extension we want to copy
# extension = '.csv'

# # Loop through the folders, subfolders, and files in the source folder
# for folders, subfolders, filenames in os.walk(source_folder):
#     # Pick only the files to loop through 
#     for filename in filenames:
#         # Check if the file matches the extension
#         if filename.endswith(extension):
#             # Code to copy the files 
#             shutil.copy(os.path.join(folders, filename), destination_folder)
#             # Code to move the files 
#             shutil.move(os.path.join(folders, filename), destination_folder)


# import os
# import shutil

# Define the source folder where files are stored and the destination folder where we will move files to
# source_folder = "C:/Users/user/Desktop/source_folder"
# destination_folder = "C:/Users/user/Desktop/destination_folder"
# destination_2 = "C:/Users/user/Desktop/destinayion_2"

# # Define the file extension we want to move
# extension = ".xlsx"

# # Loop through the folders, subfolders, and files in the source folder
# for folders, subfolders, filenames in os.walk(source_folder):
#     # Pick only the files to loop through 
#     for filename in filenames:
#         # Check if the file matches the extension
#         if filename.endswith('{}'.format(extension)): 
#             # Code to move the files
#             shutil.move(os.path.join(folders, filename), destination_folder) 

# import os
# import shutil

# # Define the source folder where files are stored and the destination folder where we will move files to
# source_folder = 'C:/Users/user/Desktop/source_folder'
# destination_folder = 'C:/Users/user/Desktop/destination_folder'

# # Define the file extension we want to move
# extension = '.csv'

# # Loop through the folders, subfolders, and files in the source folder
# for folders, subfolders, filenames in os.walk(source_folder):
#     # Pick only the files to loop through 
#     for filename in filenames:
#         # Check if the file matches the extension
#         if filename.endswith(extension):
#             source_file = os.path.join(folders, filename)
#             destination_file = os.path.join(destination_folder, filename)
#             print(f"Moving {source_file} to {destination_file}")
#             # Code to move the files
#             shutil.move(source_file, destination_file)



# import paramiko
# import os
# import shutil

# # create ssh client 
# ssh_client = paramiko.SSHClient()

# # remote server credentials
# host = "demo.wftpserver.com"
# username = "demo"
# password = "demo"
# port = 2222

# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname=host,port=port,username=username,password=password)

# print('connection established successfully')
# ftp = ssh_client.open_sftp()
# files = ftp.get( "/upload/dummy2.xlsx","C:\Users\user\Desktop\destination_folder\dummy2.xlsx")
# # files = ftp.listdir("upload")
# # for file in files:
# #     print(file)
# #     files = ftp.get(file,"C:/Users/adebb/destination_folder")

# print("Listing all the files and Directory: ",files)
# ssh_client.close()




# import paramiko
# import os
# import shutil

# # create ssh client 
# ssh_client = paramiko.SSHClient()

# # remote server credentials
# host = "demo.wftpserver.com"
# username = "demo"
# password = "demo"
# port = 2222

# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname=host, port=port, username=username, password=password)

# print('Connection established successfully')
# ftp = ssh_client.open_sftp()
# ftp.get("/upload/dummy2.xlsx", "C:\\Users\\user\\Desktop\\destination_folder\\dummy2.xlsx")
# # files = ftp.listdir("upload")
# # for file in files:
# #     print(file)
# #     files = ftp.get(file,"C:/Users/adebb/destination_folder")

# print("File downloaded successfully")
# ftp.close()
# ssh_client.close()


# files = ftp.listdir("upload")
# filepath = "/upload/"
# destpath = "C:\\Users\\adebb\\destination_folder\\"
# for file in files:
#     ftp.get(filepath + file, destpath + file)
#     print(file)




    #To get file from server to your local machine 

import os
import shutil
import paramiko
ssh_client = paramiko.SSHClient()
host = "demo.wftpserver.com"
username = "demo"
password = "demo"
port = 2222

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname=host,port=port,username=username,password=password)

print('connection established successfully') 

ftp = ssh_client.open_sftp()

files = ftp.listdir("download")
print(files)

for i, file in enumerate(files):
    if file.endswith('.pdf'):
        ftp.get(f'/download/{file}', f'C:/Users/user/Desktop/destination_folder/{file}')

        print(f'Moved {file}')

    

print("Listing all the files and Directory: ",files)

ssh_client.close()
