#!/usr/bin/env python3
"""
This script uses the GitHub API to print the location of a specific user.

Usage:
    ./2-user_location.py <GitHub API URL>

Arguments:
    <GitHub API URL>: The full URL to the GitHub user's API endpoint. Example:
                      https://api.github.com/users/holbertonschool

Outputs:
    - If the user exists and has a location set, the location is printed.
    - If the user does not exist, "Not found" is printed.
    - If the rate limit is exceeded (status code 403), the script prints
      "Reset in X min", where X is the number of minutes until the rate limit resets.

Notes:
    - The script gracefully handles API errors.
    - If the status code is 403, the "X-RateLimit-Reset" header is used to determine
      when the rate limit will be reset.
"""

import sys
import requests
import time


def main():
    """
    Main function to fetch and display the GitHub user's location or handle errors.

    This function checks the status code of the API request and appropriately
    handles cases like rate-limiting (status code 403), user not found (status code 404),
    and general successful requests (status code 200).
    """
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)

        if response.status_code == 200:
            user_data = response.json()
            location = user_data.get('location')
            if location:
                print(location)
            else:
                print("Location not available")
        elif response.status_code == 404:
            print("Not found")
        elif response.status_code == 403:
            reset_time = int(response.headers.get('X-RateLimit-Reset'))
            current_time = int(time.time())
            minutes_left = (reset_time - current_time) // 60
            print(f"Reset in {minutes_left} min")
        else:
            print(f"Error: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == '__main__':
    main()
