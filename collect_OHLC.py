import requests
import json
import time

def collect(pair, interval):
    print(f'\nCollecting at {int(time.time() // 60)}')
    resp = requests.get(f'https://api.kraken.com/0/public/OHLC?pair={pair}&interval={interval}').json()
    last = resp.get('result').get('last')
    data = resp.get('result').get(pair)
    print(f'\nNext collect at {(last + (720 * interval * 60)) // 60}')
    return data, last

def dump(data, pair, interval):
    try:
        with open(f'{pair}{interval}.json', 'r') as read:
            readout = json.load(read).get(pair)
            data = readout + data
            out = {pair:data}
    except FileNotFoundError: 
        with open(f'{pair}{interval}.json', 'w') as write:
            out = {pair:data}
            json.dump(out, write)
        with open(f'{pair}{interval}.json', 'r') as read:
            readout = json.load(read).get(pair)
            data = readout + data
            out = {pair:data}
    with open(f'{pair}{interval}.json', 'w') as write:
        json.dump(out, write)
        print(f'\nSaved data to {pair}{interval}.json')

def main():
    data = []
    pair = input('Collect data for which pair? ').upper()
    interval = 1
    resp, last = collect(pair, interval)
    for ohlc in resp:
        data.append(ohlc)
    time.sleep(interval * 719 * 60)
    
    while True:
        try:
            if int(time.time() // 60) == (last + (720 * interval * 60)) // 60:
                resp, last = collect(pair, interval)
                for ohlc in resp:
                    data.append(ohlc)
                time.sleep(interval * 719 * 60)
        except KeyboardInterrupt:
            dump(data, pair, interval)
            break

if __name__ == '__main__':
    main()

