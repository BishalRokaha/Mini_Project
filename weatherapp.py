import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
city=input("Enter the name of the city you you want. ")
url=f"https://api.weatherapi.com/v1/current.json?key=8c5ee8df80224a2f98240009240704&q={city}"

r=requests.get(url)
# print(r.text)
weathdict=json.loads(r.text)
temp=weathdict["current"]["temp_c"]
speak.Speak(f"The current weather in {city} is {temp} degrees celcius.")
print(temp)