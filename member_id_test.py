import requests
dictToSend = {"first_name": "Jose", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "MX"}
res = requests.post('http://localhost:5000/member_id', json=dictToSend)
if res.ok:
    print(res.json())
