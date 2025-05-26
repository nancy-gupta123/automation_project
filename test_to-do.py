import requests
import json

# Test Case 1: Fetch a single food item by ID
# def testCase1():
#     url = "http://127.0.0.1:8000/api/foods/1/"
#     response = requests.get(url)
    
#     print("Test Case 1 Response:", response.text)
#     assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

# Test Case 2: Create a food item with valid data
def testCase2():
    url = "http://127.0.0.1:8000/api/foods/"

    payload = json.dumps({
        "name": "veg roll",
        "price": "100"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)

    print("Test Case 2 Response:", response.text)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"

# Test Case 3: Try to create a food item with missing 'name' field
def testCase3():
    url = "http://127.0.0.1:8000/api/foods/"

    payload = json.dumps({
        "price": "100"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)

    print("Test Case 3 Response:", response.text)
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"

# Run test cases
if __name__ == "__main__":
    testCase1()
    testCase2()
    testCase3()
