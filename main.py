#!/bin/python3

import requests
from requests.exceptions import HTTPError
import json

HEALTHCHECK = "https://u3mpbqz6ki.execute-api.us-east-1.amazonaws.com/prod/healthcheck"
TODO = "https://u3mpbqz6ki.execute-api.us-east-1.amazonaws.com/prod/todo"


def healthcheck():
    try:
        # get healthcheck
        r = requests.get(HEALTHCHECK)
        r.raise_for_status()
        # print('print status code')
        print(f'Status code: {r.status_code}')
        # parse content
        c = r.json()
        for key, value in c.items():
            print(key, ":", value)
            if value == 'ok':
                # todo()
                break
            else:
                print(f'Healthcheck was not ok: {value}')
    except Exception as e:
        print(f'Healthcheck failed: {e}')
        # raise



if __name__ == '__main__':
    healthcheck()