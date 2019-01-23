from flask_api import FlaskAPI
from flask_cors import CORS
from flask import request
import requests
import xmltodict

from get_weather_by_city_selenium import get_url_for_city

app = FlaskAPI(__name__)
CORS(app)


@app.route('/fetch_rss/<city>',  methods=['GET'])
def fetch_data(city):
	url = get_url_for_city(request.view_args['city'])
	if url is not None:
		weather_url = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/" + url.split("/")[-1]
		xml = requests.get(weather_url)
		data = xmltodict.parse(xml.content)
		title = data['rss']['channel']["title"] 
		items = [d["title"] for d in data['rss']['channel']["item"]] 
		data_list = []
		for item in items:
			print (item)
			data = {}
			data['day'] = item.split(":")[0]
			data['weather'] = item.split(":")[1].split(" ")[1]
			data['min'] = (" ").join(item.split(":")[2].split(" ")[1:3])
			if "Maximum" in item.split(":")[2]:
				data["max"] = item.split(":")[3]
			data_list.append(data)
		return data_list
	return "No Url Found"

if __name__ == "__main__":
    app.run(debug=True)