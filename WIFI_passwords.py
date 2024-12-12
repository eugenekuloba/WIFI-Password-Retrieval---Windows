import subprocess

try:
    # Retrieve all Wi-Fi profiles
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], stderr=subprocess.DEVNULL)
    data = data.decode('utf-8', errors='replace').split('\n')  # Replace invalid characters
    
    # Extract Wi-Fi profile names
    profiles = [profile.split(":")[1][1:-1] for profile in data if "All User Profile" in profile]
    
    print("{:<20} {:}".format("WiFi Names", "Passwords"))
    print("-" * 35)
    
    for profile in profiles:
        try:
            # Retrieve details for each profile
            profile_data = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'],
                stderr=subprocess.DEVNULL
            )
            profile_data = profile_data.decode('utf-8', errors='replace').split('\n')  # Replace invalid characters
            
            # Extract password
            passwords = [line.split(":")[1][1:-1] for line in profile_data if "Key Content" in line]
            password = passwords[0] if passwords else "No password found"
            
            # Print profile and password
            print("{:<20} {:}".format(profile, password))
        
        except subprocess.CalledProcessError:
            print(f"Could not retrieve details for profile: {profile}")
except Exception as e:
    print(f"An error occurred: {e}")
