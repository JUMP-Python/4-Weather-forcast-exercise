#Must pip install regex
from WeatherRequests import WeatherRequests
import unittest
from datetime import datetime
import regex as re

class WeatherRequestsTest(unittest.TestCase) :
    def setUp(self) :
        #Coordinates for Cognixia headquarters
       latitude, longitude = 40.648854381567084, -74.58341504623498

       #Get the current weather and save it as a object variable
       self.weather = WeatherRequests(latitude, longitude)


    #Make sure there is a connection being made
    def test_connection(self) :
        self.assertEqual(self.weather.response.status_code, 200, 'Connection was not successful')

    #Make sure 3 days are included in the
    def test_output(self) :
        weather = self.weather.printWeather()
        beginning = fr'This Afternoon: .*'

        weekdays = {0:'Monday', 1:"Tuesday", 2:'Wednesday', 3:'Thursday',4:'Friday', 5:'Saturday', 6:"Sunday"}
        end_int = datetime.today().weekday()
        end_int = weekdays[end_int+2]
        ending = fr'{end_int} Night.*'

        self.assertTrue((bool(re.match(beginning, weather[0])) & bool(re.match(ending, weather[-1]))))

if __name__ == "__main__" :
    unittest.main()