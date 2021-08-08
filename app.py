from flask import Flask, render_template,request,redirect,url_for
import requests as r
import math
import datetime

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        user = request.form['city_name']
        return redirect(url_for("user", usr=user))
    else:
        return render_template('login.html')

@app.route('/<usr>')
def user(usr):
    api_key="097b334776a97004ad759ceb8a082d3a"
    res=r.get(f'http://api.openweathermap.org/data/2.5/weather?q={usr}&appid={api_key}')
    response=res.json()
    if (response.get('cod')!=200):
        return '<h2> There is a error in the city name you entered! Try again!!</h2>'
    country=response['sys']['country']
    res=r.get(f"https://restcountries.eu/rest/v2/alpha/{country}").json()
    
    
    coun=res['name']
    wind=response['wind']['speed']

    description=response['weather'][0]['description']

    temp=response['main']['temp']
    temp=math.floor(temp-273.15)
    tempFeelsLike=response['main']['feels_like']
    tempFeelsLike=math.floor(tempFeelsLike-273.15)

    rise=response['sys']['sunrise']
    sunrise=datetime.datetime.fromtimestamp(rise)
    sunrise.strftime('%Y-%m-%d %H:%M:%S')

    sets=response['sys']['sunset']
    sunset=datetime.datetime.fromtimestamp(sets)
    sunset.strftime('%Y-%m-%d %H:%M:%S')


    return('<div class="cont"><h1>City-{}</h1><h2>Country-{}</h2><h2>The wind speed is {}</h2><h2>The description of weather is {} </h2><h2>Temp is {} centigrade</h2> <h2>Temp feels like {} centigrade</h2> <h2>Sunrise:{}</h2> <h2>Sunset:{}</h2></div>'.format(usr,coun,wind,description,temp,tempFeelsLike,sunrise,sunset),render_template("info.html"))



if __name__ == '__main__':
    app.run(debug=True)
