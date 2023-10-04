import requests

def get_user_activity(profile_number):
    api_url = f"https://www.hackthebox.com/api/v4/profile/activity/{profile_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",  
        "Accept": "application/json",
    
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        activity_list = data["profile"]["activity"]
        return activity_list
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
    return None

def main():
    profile_number = input("Enter the profile number: ")
    activity = get_user_activity(profile_number)

    if activity:
        for item in activity:
            print(f"Date: {item['date']}")
            print(f"Object Type: {item['object_type']}")
            print(f"Type: {item['type']}")
            print(f"Points: {item['points']}")
            print(f"Machine Name: {item['name']}")
            print("-" * 40)
    else:
        print("Failed to fetch user activity data.")

if __name__ == "__main__":
    main()

