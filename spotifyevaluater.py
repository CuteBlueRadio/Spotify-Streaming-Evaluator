import json

print('Loading data. . . . .')
data = open('StreamingHistory0.json', 'r')
data2 = open('StreamingHistory1.json', 'r')
content = json.load(data)
content2 = json.load(data2)

timeplayed = 0
artistlist = []
playedamount = 0

for song in content + content2:
    artistname = song['artistName']
    if artistname not in artistlist:
        artistlist.append(artistname)

def evaluate(band, timeplayed, artistlist, playedamount):
    for song in content + content2:
        if song['artistName'] == band:
            timeplayed = timeplayed + int(song['msPlayed'])
            playedamount = playedamount + 1

    print(f"""--------------------------------------
You've listened to {band} {timeplayed/3600000} hours
You've listened to {band} {playedamount} times""")

def loop():
    band = input('What band would you like to evaluate? ')
    evaluate(band, timeplayed, artistlist, playedamount)
    loop()
loop()