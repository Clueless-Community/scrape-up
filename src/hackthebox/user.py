import requests

def get_user_profile(profile_number):
    url = f"https://www.hackthebox.com/api/v4/profile/{profile_number}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        # Add any other headers if needed
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        profile_data = response.json().get('profile')  # Access 'profile' key in the response
        return profile_data
    else:
        return None

def main():
    profile_number = input("Enter your Hack The Box profile number: ")

    user_data = get_user_profile(profile_number)

    if user_data:
        print("\nProfile Information:")
        print(f"Username: {user_data['name']}")
        print(f"Rank: {user_data['rank']}")
        print(f"Points: {user_data['points']}")
        print(f"Respects: {user_data['respects']}")
        print(f"System Owns: {user_data['system_owns']}")
        print(f"User Owns: {user_data['user_owns']}")
        print(f"Ranking: {user_data['ranking']}")
        # Add more fields as needed
    else:
        print("Failed to fetch user profile information. Please check the profile number and try again.")

if __name__ == "__main__":
    main()



