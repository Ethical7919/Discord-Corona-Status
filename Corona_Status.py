import time, requests

while True:
    corona_api = "https://coronavirus-19-api.herokuapp.com/countries/world"
    corona_status = requests.get(corona_api)
    json = corona_status.json()
    TodayCases = json["todayCases"]
    TodayDeaths = json["todayDeaths"]
    content = {
      "custom_status": {"text": f"Covid Today Cases: {TodayCases}, Today death: {TodayDeaths}"}
    }

    x = requests.patch("https://ptb.discordapp.com/api/v9/users/@me/settings", headers={"authorization": "YOUR_TOKEN_HERE"}, json=content)
    time.sleep(5)