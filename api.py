import requests

def get_video_url(tweet_url):

    url = "https://twitter-x-media-download.p.rapidapi.com/media/privatefx"

    payload = { "url": tweet_url }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "4a2cae52e9mshd8c855f97d1132bp1aad0ajsn3ae8a6aa9c5a",
        "X-RapidAPI-Host": "twitter-x-media-download.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        # Extract video URL
        video_url = data['tweet']['media']['all'][0]['url']
        return video_url
    else:
        return None