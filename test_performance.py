import requests
import time

URL = "https://url-shortener-02nx.onrender.com/2"  
# replace with your actual short URL

def measure():
    start = time.time()
    res = requests.get(URL)
    end = time.time()
    return end - start

times = []

for i in range(20):
    t = measure()
    times.append(t)
    print(f"Request {i+1}: {t:.4f} sec")

avg = sum(times) / len(times)
print("\nAverage response time:", avg)