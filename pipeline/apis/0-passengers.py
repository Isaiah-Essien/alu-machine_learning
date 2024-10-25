#!/usr/bin/env python3
'''This script collects data from the swapiapi'''


import requests


def availableShips(passengerCount):
    """
    Method that returns the list of ships
    that can hold a given number of passengers.

    Args:
        passengerCount (int): number of passengers
        to be transported

    Returns:
        list: List of ship names that can hold
        the given number of passengers
    """
    url_link = 'https://swapi-api.alx-tools.com/api/starships/'
    list_ships = []

    while url_link:
        response = requests.get(url_link)

        # Handle error incase request fails
        if response.status_code != 200:
            print(f"Failed to retrieve data:
                  {response.status_code}")
            break

        data = response.json()

        for ship in data['results']:
            # Skip ships with invalid passenger values
            if ship["passengers"] not in [
                "n/a", "unknown", "0", "none"]:
                try:
                    ship["passengers"] = ship[
                        "passengers"].replace(",", "")
                    if int(ship['passengers']) >= passengerCount:
                        list_ships.append(ship['name'])
                except ValueError:
                    # Handle unexpected non-numeric passenger values
                    pass

        # Move to the next page if available
        url_link = data['next']

    return list_ships
