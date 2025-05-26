import requests
import json

# def testCase1():
    

#     url = "http://127.0.0.1:8000/api/foods/1/"

#     payload = {}
#     files={}
#     headers = {}

#     response = requests.request("GET", url, headers=headers, data=payload, files=files)

#     print(response.text)
#     assert response.status_code == 200, "Expected status code 200, got {}".format(response.status_code)

def testCase2():
    

    url = "http://127.0.0.1:8000/api/foods/"

    payload = json.dumps({
    "name": "veg roll",
    "price": "100"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text) 

    assert response.status_code == 201, "Expected status code 201, got {}".format(response.status_code)   


def testCase3():
    url = "http://127.0.0.1:8000/api/foods/"

    payload = json.dumps({
    "price": "100"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text) 

    assert response.status_code == 400, "Expected status code 400, got {}".format(response.status_code)
