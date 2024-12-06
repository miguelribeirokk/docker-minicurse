import requests
import time

while True:
        data = requests.get('https://cointradermonitor.com/api/pbb/v1/ticker').json()
        print(f"Last price: {data['last']}, volume: {data['volume24h']} \n")

        f = open(r"data/arquivo.txt", "a")
        f.write(f"Last price: {data['last']}, volume: {data['volume24h']} \n")
        f.close()

        time.sleep(2)