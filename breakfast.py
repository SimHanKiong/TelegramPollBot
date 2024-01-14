import json
import requests

base_url = 'https://api.telegram.org/bot6058334295:AAGGjs89mcyHLjIrFzxRZKhZ4twQKowLx8U/sendPoll'

parameters = {
  'chat_id': '-780533831',
  'question': 'Breakfast',
  'options': json.dumps(['8 am', '8.30 am', '9 am', '9.30 am', '10 am']),
  'is_anonymous': False,
  'allows_multiple_answers': True
}

requests.get(base_url, data = parameters)
