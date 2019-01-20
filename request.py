import requests
import json


def dwf_request(form):
    data = {
        'score': form['score'],
        'kldm': form['kldm']
    }
    response = requests.post('http://query.zk789.net/Home/GetDWF', data=data)
    result = json.loads(response.text)['data']
    return result[0]
