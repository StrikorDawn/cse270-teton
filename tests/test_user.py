import pytest
import requests
import requests_mock

# Function to mock the server responses
def test_users_endpoint_unauthorized():
    with requests_mock.Mocker() as m:
        # Define the mock behavior for the first test
        url = "http://127.0.1:8000/users"
        m.get(url, json={}, status_code=401)  # Simulate 401 with empty JSON response

        # Define the parameters
        params = {"username": "admin", "password": "admin"}
        
        # Make a GET request to the mock server
        response = requests.get(url, params=params)
        
        # Assert that the response code is 401
        assert response.status_code == 401, f"Expected 401, got {response.status_code}"
        
        # Assert that the response body is an empty JSON object
        assert response.json() == {}, f"Expected empty response, got {response.text}"

def test_users_endpoint_authorized():
    with requests_mock.Mocker() as m:
        # Define the mock behavior for the second test
        url = "http://127.0.1:8000/users"
        m.get(url, json={}, status_code=200)  # Simulate 200 with empty JSON response

        # Define the parameters
        params = {"username": "admin", "password": "qwerty"}
        
        # Make a GET request to the mock server
        response = requests.get(url, params=params)
        
        # Assert that the response code is 200
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Assert that the response body is an empty JSON object
        assert response.json() == {}, f"Expected empty response, got {response.text}"
