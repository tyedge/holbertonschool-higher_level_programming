#!/usr/bin/python3
"""This script script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == '__main__':
        import requests
        import sys

        url = 'http://0.0.0.0:5000/search_user'

        if len(sys.argv) < 2:
                q = {'q': ""}
        else:
                q = {'q': sys.argv[1]}

        ret = requests.post('http://0.0.0.0:5000/search_user', data=q)

        try:
                response = ret.json()

                if len(response) > 0:
                        print('[{}] {}'.format(response.get('id'),
                                               response.get('name')))
                else:
                        print("No result")
        except ValueError:
                print('Not a valid JSON')
