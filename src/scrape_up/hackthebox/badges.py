import requests

def get_user_badges(profile_number):
    api_url = f"https://www.hackthebox.com/api/v4/profile/badges/{profile_number}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        badges = data.get("badges", [])
        return badges
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
    badges = get_user_badges(profile_number)

    if badges:
        for badge in badges:
            print(f"Badge ID: {badge['id']}")
            print(f"Name: {badge['name']}")
            print(f"Description: {badge['description_en']}")
            print(f"Color: {badge['color']}")
            print(f"Icon: {badge['icon']}")
            print("-" * 40)
    else:
        print("No badges found for the given profile number.")

if __name__ == "__main__":
    main()
