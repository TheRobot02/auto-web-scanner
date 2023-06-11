#------------[Imports]------------#
from urllib.parse import urlparse
import requests
import os
from datetime import datetime

#------------[fariables]------------#
file_extensions = ['csv', 'doc', 'docx', 'pdf', 'xls', 'xlsx', 'csv','png','jpg', 'txt', 'zip' ,'rar']
dt_string = "%Y %m %d"
date = f"{datetime.now().strftime(dt_string)}"

#------------[download files]------------#
def download_files(download_list, download_start_dir, origin_url):
    print("\nstarting download files...")
    for download_link in download_list:
        response = requests.get(f"{origin_url}{download_link}")
        if response.status_code == 200:
            file_extension, file_name = grep_file_info(download_link)
            download_dir = f"{download_start_dir}/{date}/{file_extension}"
            filepath = f"{download_dir}/{file_name}"
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
            with open(filepath, 'wb') as file:
                file.write(response.content)
                print(f"File downloaded successfully and saved as {file_name}")
        else:
            print("Failed to download the file")

#------------[grep file info from link]------------#
def grep_file_info(download_link):

    file_extension = download_link.split('.')[-1]
    file_name = download_link.split('/')[-1]
    return file_extension, file_name


