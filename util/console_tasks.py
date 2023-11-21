import requests

API_BASE_URL = 'http://127.0.0.1:8000'
LOGIN_ENDPOINT = '/api/auth/jwt/create/'
TASKS_ENDPOINT = '/api/backlog-items/'


def get_jwt_token(username, password):
    try:
        response = requests.post(API_BASE_URL + LOGIN_ENDPOINT, data={
            'username': username,
            'password': password,
        })
    except requests.exceptions.ConnectionError as er:
        print(f'Filed to run POST request, error : {er} ')
        return None

    if response.status_code == 200:
        print('Token got!')
        return response.json()['access']
    else:
        print(f'Failed to get Token. status code = {response.status_code}')
        return None


def get_tasks(jwt_token):
    headers = {"Authorization": f"Bearer {jwt_token}"}
    response = requests.get(API_BASE_URL + TASKS_ENDPOINT, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to get Tasks. Status code {response.status_code}')
        return []


def main():
    username = input('Enter Username : ')
    password = input('Enter password : ')

    jwt_token = get_jwt_token(username, password)
    if jwt_token:
        tasks = get_tasks(jwt_token)
        print('Your tasks:')

        for task in tasks:
            print(task)


if __name__ == '__main__':
    main()
