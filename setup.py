import zipfile
from zipfile import ZipFile
import platform
import requests
import os


def download(url, filename):
    if path.exists(filename):
         print("File exists...")
         zipObj = ZipFile(filename)
         zipObj.extractall()
         print("Already ffmpeg downloaded and extracted..")
         print("Copy file to <Python Directory>/Scripts . That's all .. ")

    else:
         with open(filename, 'wb') as f:
                 response = requests.get(url, stream=True)            
                 total = response.headers.get('content-length')
                 if total is None:
                      f.write(response.iter_content)
                 else:
                      downloaded = 0
                      total = int(total)
                      for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                          downloaded += len(data)
                          f.write(data)
                          done = int(50*downloaded/total)
                          sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                          sys.stdout.flush()
         sys.stdout.write('\n')
         zipObj = ZipFile(filename)
         zipObj.extractall()



if '64bit' in platform.architecture():
	    url = "https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20200814-a762fd2-win64-static.zip"
	    filename = "64bitFfmpeg.zip"
	    print("Your system 64bit,File ll download after second . . . ")
	    download(url,filename)

else:
	    url = "https://ffmpeg.zeranoe.com/builds/win32/static/ffmpeg-20200816-5df9724-win32-static.zip"	
	    filename = "32bitFfmpeg.zip"
	    print("Your system 32bit,File ll download after second . . . ")   
	    download(url,filename)





