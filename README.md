# This bot tweets your internet speed from [SpeedTest](https://www.speedtest.net)


## Usage

1. Download chromedriver and replace the driver path inside internetspeed.py and tweet.py
```python
driver_path = ''
```

2. Replace username and password with your twitter username and password in main.py
```python
tweet = TwitterBot(tweet=f'This Tweet is from a Python Bot\n Pings:{PINGS}, DOWN/{DWL_SPD}mbps, UP/{UPL_SPD}mbps',
                   username='', passowrd='')
```

3. Run the program (main.py).
