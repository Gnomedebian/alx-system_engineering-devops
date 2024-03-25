#!/usr/bin/python3
"""
give employee ID, returns infos about todo list progress
and exports it in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_response = requests.get(url + "users/{}".format(user_id))
        user_response.raise_for_status()
        user = user_response.json()
        username = user.get("username")

        todos_response = requests.get(url + "todos", param={"userId": user_id})
        todos_response.raise_for_status()
        todos = todos_response.json()

        with open("{}.json".format(user_id), "w") as jsonfile:
            json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)

        print("Data exported successfully to {}.json".format(user_id))

    except requests.exceptions.HTTPError as err:
        print("HTTP Error:", err)
        sys.exit(1)

    except json.JSONDecodeError as err:
        print("JSON Decoding Error:", err)
        sys.exit(1)

    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)
