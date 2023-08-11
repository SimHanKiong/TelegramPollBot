import json
import requests

base_url = 'https://api.telegram.org/bot6058334295:AAGGjs89mcyHLjIrFzxRZKhZ4twQKowLx8U/sendPoll'

parameters = {
  'chat_id': '-920155043',
  'question': 'Dinz',
  'options': json.dumps(['6.30 pm', '7 pm', '7.30 pm']),
  'is_anonymous': False,
  'allows_multiple_answers': True
}

requests.get(base_url, data = parameters)
