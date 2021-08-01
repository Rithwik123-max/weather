from flask import Flask, render_template,request,redirect,url_for
import requests as r
import math
import datetime

app = Flask(__name__)

# @app.route("/",methods=['POST','GET'])
# def hello_world():
#     if request.method=="POST" and 'city_name' in request.form:
#         city_name=request.form.get("city_name")
#     return render_template('login.html')
    #     api_key="097b334776a97004ad759ceb8a082d3a"
    # # city_name="warangal"
    #     response=r.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}').json()
    #     wind=response['wind']['speed']

    #     description=response['weather'][0]['description']

    #     temp=response['main']['temp']
    #     temp=math.floor(temp-273.15)

    #     tempFeelsLike=response['main']['feels_like']
    #     tempFeelsLike=math.floor(tempFeelsLike-273.15)
    # return('<h1>City-{}</h1><h2>The wind speed is {}</h2><h2>The description of weather is {} </h2><h2>Temp is {} centigrade</h2> <h2>Temp feels like {} centigrade</h2>'.format(city_name,wind,description,temp,tempFeelsLike))
    

    # return render_template('login.html')
    
# @app.route('/login',methods=["POST","GET"])
# def login():
#     if request.method=="POST" and 'city_name' in request.form:
#         city_name=request.form.get("city_name")
#         return render_template('index.html')
# #     if request.method=="POST":
# #         city_name=request.form.get("city_name")
# #         return "<h1>city_name</h1>"
#     # else:
#     #     return redirect(url_for('weather'),city_name=city_name)
#     # return redirect(url_for('weather'),city_name=city_name)
    
#     #     return(render_template('login.html'))
    
# @app.route('/result',methods=["POST","GET"])
# def weather():
    
    # api_key="097b334776a97004ad759ceb8a082d3a"
    # # city_name="warangal"
    # response=r.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}').json()
    # wind=response['wind']['speed']

    # description=response['weather'][0]['description']

    # temp=response['main']['temp']
    # temp=math.floor(temp-273.15)

    # tempFeelsLike=response['main']['feels_like']
    # tempFeelsLike=math.floor(tempFeelsLike-273.15)
    # return('<h1>City-{}</h1><h2>The wind speed is {}</h2><h2>The description of weather is {} </h2><h2>Temp is {} centigrade</h2> <h2>Temp feels like {} centigrade</h2>'.format(city_name,wind,description,temp,tempFeelsLike))
    

@app.route('/',methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        user = request.form['city_name']
        return redirect(url_for("user", usr=user))
    else:
        return render_template('login.html')

@app.route('/<usr>')
def user(usr):
    # return f"<h1> {usr} </h1>"
    api_key="097b334776a97004ad759ceb8a082d3a"
    # city_name="warangal"
    response=r.get(f'http://api.openweathermap.org/data/2.5/weather?q={usr}&appid={api_key}').json()
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
    return('<h1>City-{}</h1><h2>Country-{}</h2><h2>The wind speed is {}</h2><h2>The description of weather is {} </h2><h2>Temp is {} centigrade</h2> <h2>Temp feels like {} centigrade</h2> <h2>Sunrise:{}</h2> <h2>Sunset:{}</h2>'.format(usr,coun,wind,description,temp,tempFeelsLike,sunrise,sunset))



if __name__ == '__main__':
    app.run(debug=True)