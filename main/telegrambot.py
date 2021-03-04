import requests

api_url = 'https://api.telegram.org/bot'
API_TOKEN = '1593270625:AAGIEt6dQVoYvSydjyJ5Nx7bV6zYM8v2CBI'
main_url = api_url + API_TOKEN + '/'
chat_id = 372082477

def send_message(text):
    method = 'sendMessage'
    params = f'?chat_id={chat_id}&text={text}'
    request_url = main_url + method + params
    response = requests.get(request_url).json()
    return response