import requests
import getpass

BASE_URL = "http://127.0.0.1:8000"

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

# Login and obtain token
login_response = requests.post(
    f"{BASE_URL}/api/token/",
    data={
        "username": username,
        "password": password,
    }
)

if login_response.status_code != 200:
    print("Login failed:", login_response.text)
    exit()

token = login_response.json()["token"]

# Set authentication header
headers = {
    "Authorization": f"Token {token}"
}

# Create a bookmark
bookmark_data = {
    "title": "Python Tutorial",
    "url": "https://www.python.org/",
    "tags": "Python, Programming"
}

response = requests.post(
    f"{BASE_URL}/api/bookmarks/",
    json=bookmark_data,
    headers=headers
)

print("Create Status:", response.status_code)
print("Response:", response.json())

second_bookmark_data = {
    "title": "Django Documentation",
    "url": "https://www.djangoproject.com/",
    "tags": "Python, Backend"
}

second_response = requests.post(
    f"{BASE_URL}/api/bookmarks/",
    json=second_bookmark_data,
    headers=headers
)

print("\nSecond Create Status:", second_response.status_code)
print("Second Bookmark:", second_response.json())


# Get all bookmarks
response = requests.get(
    f"{BASE_URL}/api/bookmarks/",
    headers=headers
)

print("\nList Status:", response.status_code)
print("Bookmarks:", response.json())

# Get bookmarks filtered by tag
response = requests.get(
    f"{BASE_URL}/api/bookmarks/",
    params={"tag": "Python"},
    headers=headers
)

print("\nFiltered Status:", response.status_code)
print("Filtered Bookmarks:", response.json())

# Try creating a duplicate bookmark
response = requests.post(
    f"{BASE_URL}/api/bookmarks/",
    json=bookmark_data,
    headers=headers
)

print("\nDuplicate Status:", response.status_code)
print("Duplicate Error:", response.json())

# Try creating a bookmark with an invalid URL
invalid_data = {
    "title": "Invalid Website",
    "url": "www.google.com",
    "tags": "Testing"
}

response = requests.post(
    f"{BASE_URL}/api/bookmarks/",
    json=invalid_data,
    headers=headers
)

print("\nInvalid URL Status:", response.status_code)
print("Invalid URL Error:", response.json())

# Try accessing bookmarks without a token
response = requests.get(
    f"{BASE_URL}/api/bookmarks/"
)

print("\nUnauthorized Status:", response.status_code)
print("Unauthorized Response:", response.json())

# Get bookmark statistics
response = requests.get(
    f"{BASE_URL}/api/bookmarks/stats/",
    headers=headers
)

print("\nStats Status:", response.status_code)
print("Bookmark Statistics:", response.json())


# Update an existing bookmark
bookmark_id = 1

update_data = {
    "title": "Updated Python Tutorial",
    "tags": "Python, Backend"
}

response = requests.patch(
    f"{BASE_URL}/api/bookmarks/{bookmark_id}/",
    json=update_data,
    headers=headers
)

print("\nPATCH Status:", response.status_code)
print("Updated Bookmark:", response.json())


# Delete an existing bookmark
response = requests.delete(
    f"{BASE_URL}/api/bookmarks/{bookmark_id}/",
    headers=headers
)

print("\nDELETE Status:", response.status_code)

# Verify bookmarks after deletion
response = requests.get(
    f"{BASE_URL}/api/bookmarks/",
    headers=headers
)

print("\nRemaining Bookmarks:", response.json())