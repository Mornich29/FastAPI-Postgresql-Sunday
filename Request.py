import requests
import names

import concurrent.futures
import requests
import names

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

def post_request(x):
    first_name = str(names.get_first_name())
    last_name = str(names.get_last_name())
    json_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': first_name + '.' +last_name[0:4] + str(x) +'@something.com',
    }
    response = requests.post('http://localhost:8000/api/contacts/', headers=headers, json=json_data)
    return response

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(post_request, x) for x in range(100)]
    concurrent.futures.wait(results)
    responses = [result.result() for result in results]

