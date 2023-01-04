#must pip install requests
#Weather api: https://www.weather.gov/documentation/services-web-api
import requests

class WeatherRequests :

    #Will receive a longituted and latitude to request the information from the website
    def __init__(self, lat, long) :
        self.long = long
        self.lat = lat
        self.response = None #Weather request

    #This should return the forcast for the next 3 days in a LIST
    #The forecast should be day temperature, night temperature, and the precipitation prediction   
    def printWeather(self) :
        pass
        #Expected return output example:
        '''
        ['This Afternoon: Rain likely after 1pm. Mostly cloudy. High near 63, with temperatures falling to around 57 in the afternoon. South wind around 6 mph. Chance of precipitation is 70%. New rainfall amounts between a tenth and quarter of an inch possible.',
        'Tonight: Rain likely. Cloudy. Low around 49, with temperatures rising to around 52 overnight. Southwest wind around 7 mph. Chance of precipitation is 70%. New rainfall amounts between a quarter and half of an inch possible.',
        'Thursday: A slight chance of rain before 7am. Mostly cloudy. High near 53, with temperatures falling to around 48 in the afternoon. Northeast wind around 6 mph. Chance of precipitation is 20%.',
        'Thursday Night: A slight chance of rain after 1am. Mostly cloudy, with a low around 41. North wind around 3 mph. Chance of precipitation is 20%. New rainfall amounts less than a tenth of an inch possible.',
        'Friday: A chance of rain. Mostly cloudy. High near 48, with temperatures falling to around 45 in the afternoon. West wind 3 to 9 mph. Chance of precipitation is 30%. New rainfall amounts between a tenth and quarter of an inch possible.']
        'Friday Night: A slight chance of rain before 7pm. Partly cloudy, with a low around 35.
        '''
