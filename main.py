#!/bin/python3

import requests
from requests.exceptions import HTTPError
import json


def healthcheck():
    healthcheck_url = "https://u3mpbqz6ki.execute-api.us-east-1.amazonaws.com/prod/healthcheck"

    try:
        # get healthcheck
        r = requests.get(healthcheck_url)
        r.raise_for_status()
        # print(f'HC Status code: {r.status_code}')
        # get content
        c = r.json()
        # parse content
        for key, value in c.items():
            print(key, ":", value)
            if value == 'ok':
                todo()
            else:
                print(f'Healthcheck was not ok: {value}')

    except Exception as e:
        print(f'Healthcheck failed: {e}')

def todo():
    todo_url = "https://u3mpbqz6ki.execute-api.us-east-1.amazonaws.com/prod/todo"
    test_json = json.dumps({'title': 'Game of Thrones season 8 was trash.'})

    # get request
    try:
        r = requests.get(todo_url)
        r.raise_for_status()
        # print(f'TODO Status code: {r.status_code}')
        c = r.json()
        print(f'{c}')
    except Exception as e:
        print(f'Todo GET request failed: {e}')

    # post request
    try:
        p = requests.post(todo_url, test_json)
        p.raise_for_status()
        print(p.text)
    except Exception as e:
        print(f'Todo POST request failed: {e}')

if __name__ == '__main__':
    healthcheck()
