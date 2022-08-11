from django.shortcuts import render
import json
import requests

api_key = '93a39b8dab542bedbaacddb0174268a7'

def index(request):
	if request.method == 'POST':
		city = request.POST['city']

		# source contain JSON data from API

		source = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
			# 'https://api.openweathermap.org/data/2.5/weather?q ='
			# 		+ city + '&appid = 93a39b8dab542bedbaacddb0174268a7').read()

		list_of_data = source.json()

		data = {
			"country_code": str(list_of_data['sys']['country']),
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']),
			"temp": str(list_of_data['main']['temp']),
			"pressure": str(list_of_data['main']['pressure']),
			"humidity": str(list_of_data['main']['humidity']),
            "weather":str(list_of_data['weather'][0]['description'])
		}
		print(data)
	else:
		data ={}
	return render(request, "main/index.html", data)





# import requests

# api_key = '30d4741c779ba94c470ca1f63045390a'

# user_input = input("Enter city: ")

# weather_data = requests.get(
#     f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# if weather_data.json()['cod'] == '404':
#     print("No City Found")
# else:
#     weather = weather_data.json()['weather'][0]['main']
#     temp = round(weather_data.json()['main']['temp'])

#     print(f"The weather in {user_input} is: {weather}")
#     print(f"The temperature in {user_input} is: {temp}ºF")