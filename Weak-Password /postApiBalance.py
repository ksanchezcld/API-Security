import requests
import json

baseUrl = "http://192.147.115.3:8081"

path = "/balance"

def postApiBalance():
    headers = {"Content-Type": "application/json"}
    data = {"acct": 9999, "balance": 100000000, "token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdW1teSBCYW5rIiwiYWNjdCI6OTk5OSwic2NvcGUiOiJhY2NvdW50LXdyaXRlIiwiZXhwIjoxNTc1OTIxODEzLCJpYXQiOjE1NzU5MjEyMTN9.MDc7B68PgH0UAClTXRsacCoQTKeA3A3pSHGQuazKvzfVlXzLKj_EKeuBUcUdxxmfDJuMKd_5u06wyjbRK5VNB9uexKjG7tN0FvRBt2-7xEDY6TRbfKFdwC1BrR_nufD5wOq_k-7IvKbZgUnYtV_hLWEXO0eOyYbSrYta-oCfpd961C5nlKqo2P6wkJPSiCtJKrGas98edHrza15WiHJ4bA5MZbYuf6epEv48lSpsFeqZ0hAyIkDMLzFJKHsyHZKp1Agyi2Ige583F0Np392P3xffbBjAMlef2lIMpR_T9zZF8XPgKOVKm17lsaHIEFGDws7TNXKOItNxm4YWnXFN2w"}
    r = requests.post(baseUrl + path, json.dumps(data), headers=headers)
    print(r.json())

postApiBalance()