#!/bin/python3

import requests
from requests.exceptions import HTTPError
import json
import sys


def status(err):
    err_message = str(err)
    code = err_message[0:3]
    if code == 400:
        sys.exit(1)
    else:  # includes 500
        sys.exit(2)


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
            # print(key, ":", value)
            if value == 'ok':
                print(f'HEALTHCHECK request succeeded: {value}')
                todo()
            else:
                print(f'Healthcheck was not ok: {value}')
                sys.exit(2)
    except requests.exceptions.HTTPError as e:
        # print(f'Healthcheck failed: {e}')
        status(e)
    else:
        print('An unknown error occured during HEALTHCHECK request')
        sys.exit(2)

def todo():
    todo_url = "https://u3mpbqz6ki.execute-api.us-east-1.amazonaws.com/prod/todo"
    test_json = json.dumps({'title': 'I will never get over how bad the final season of Game of Thrones was.'})

    # get request
    try:
        r = requests.get(todo_url)
        r.raise_for_status()
        # print(f'TODO Status code: {r.status_code}')
        c = r.json()
        print(f'TODO-GET request succeeded: {c}')
        # post request
        try:
            p = requests.post(todo_url, test_json)
            p.raise_for_status()
            print(f'TODO-POST request succeeded: {p.text}')
            sys.exit(0)
        except requests.exceptions.HTTPError as e:
            print(f'Todo POST request failed: {e}')
            status(e)
        else:
            print('An unknown error occured during TODO-POST request')
            sys.exit(2)
    except requests.exceptions.HTTPError as e:
        print(f'Todo GET request failed: {e}')
        status(e)
    else:
        print('An unknown error occured during TODO-GET request')
        sys.exit(2)


if __name__ == '__main__':
    healthcheck()
