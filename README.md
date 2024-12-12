# README: Wi-Fi Password Retrieval Script

## Overview
This Python script retrieves the names and passwords of Wi-Fi profiles saved on a Windows machine. It uses the `netsh` command-line utility, which is built into Windows, to extract this information. The script is intended for educational and administrative purposes only.

## Prerequisites
- **Operating System**: Windows
- **Python Version**: Python 3.6 or later
- **Privileges**: Administrator privileges are required to run the `netsh` commands successfully.

## How It Works
1. The script executes the `netsh wlan show profiles` command to list all saved Wi-Fi profiles on the machine.
2. For each profile, it retrieves the profile details using `netsh wlan show profile <profile> key=clear`.
3. The script extracts the Wi-Fi password from the output under the "Key Content" field.
4. It displays the Wi-Fi names and their corresponding passwords in a table-like format.

## Installation
1. Ensure Python is installed on your system.
2. Save the script as `WIFI_passwords.py`.

## Usage
1. Open a command prompt as an administrator.
2. Navigate to the directory where the script is saved.
3. Run the script using the following command:
   ```
   python WIFI_passwords.py
   ```
4. The output will display saved Wi-Fi profiles and their passwords.

## Handling Errors
- **Decoding Errors**: If you encounter a decoding error (e.g., `invalid continuation byte`), the script replaces problematic characters with a placeholder (�) to ensure execution continues.
- **Missing Passwords**: For profiles without stored passwords, the script displays "No password found".
- **Permission Errors**: Ensure you run the script as an administrator.

## Security Considerations
- **Privacy**: Use this script responsibly. Ensure you have permission to access the Wi-Fi profiles on the machine.
- **Logging**: Avoid logging sensitive information such as Wi-Fi passwords.

## Enhancements
You can extend the script by:
- Writing the output to a file for further analysis.
- Adding filters to display specific Wi-Fi profiles.
- Supporting different output formats (e.g., JSON or CSV).

## License
This script is provided "as is" for educational purposes. The author is not responsible for any misuse of this script.

## Author
Developed by Eugene Kuloba.

