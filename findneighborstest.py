from geopy.geocoders import Nominatim
from math import cos, asin, sqrt
class User:
    def __init__(self,name,location):
        self.name = name
        self.location = location
    def __init__(self,name,latiude , longitude):
        self.name = name
        self.location = Location(latiude,longitude)
        
        
        
class Location:
    def __init__(self,latiude , longitude):
        self.latiude = latiude
        self.longitude = longitude
    def __str__(self):
        return str(self.latiude) + " " +  str(self.longitude)
class Address:
    def __init__(self,address):
        def __get_location__(address):
            geolocator = Nominatim()
            location = geolocator.geocode(address)
            self.location = Location(location.latitude, location.longitude)
            
        self.address = address
       
        __get_location__(address)
    def __str__(self):
        return self.address + " "+  str(self.location)
def kilometers_miles(KM):
    return KM *   0.62137
def distance(lat1, lon1, lat2, lon2):
    R = 12742 # radius of the earth
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return kilometers_miles(12742 * asin(sqrt(a)))
def find_neighbors(user,radius,neighbors):
    pass
def find_lower_max_bounds(center,distance=5,tolerance= .1,step=.01):
    def kilometers_miles(KM):
        return KM *   0.62137
    def find_distance(lat1, lon1, lat2, lon2):
        R = 12742 # radius of the earth
        p = 0.017453292519943295
        a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
        return kilometers_miles(12742 * asin(sqrt(a)))
    def find_higher_bound(center,distance=5,tolerance= .1,step=.01):
        higher_bound = distance+distance * tolerance
        result = 0
        cal_distance = higher_bound
        counter = 1
        while  cal_distance <= higher_bound:
            result = center.latiude + step * counter
            cal_distance = find_distance(center.latiude, center.longitude, result, center.longitude)
            counter = counter + 1
        latiude = result  
        result = 0
        counter = 1
        cal_distance = higher_bound
        while   cal_distance <= higher_bound :
            result = center.longitude + step * counter
            cal_distance = find_distance(center.latiude, center.longitude, center.latiude, result)
            counter = counter + 1
        longitude = result
        return latiude,longitude
        
    def find_lower_bound(center,distance=5,tolerance= .1,step=.01):
        lower_bound = distance-distance * tolerance
        result = 0
        cal_distance = lower_bound
        counter = 1
        while  cal_distance <= lower_bound:
            result = center.latiude - step * counter
            cal_distance = find_distance(center.latiude, center.longitude, result, center.longitude)
            counter = counter + 1
        latiude = result  
        result = 0
        counter = 1
        cal_distance = lower_bound
        while   cal_distance <= lower_bound :
            result = center.longitude - step * counter
            cal_distance = find_distance(center.latiude, center.longitude, center.latiude, result)
            counter = counter + 1
        longitude = result
        return latiude,longitude
    low_lat,low_long=find_lower_bound(center,distance=distance,tolerance=tolerance,step=step)
    high_lat,high_long=find_higher_bound(center,distance=distance,tolerance=tolerance,step=step)
    

        
home = Address("12722 Pokagon St, IN")
print(home)
print(find_lower_max_bounds(home.location))
#print(distance(home.location.latiude,home.location.longitude,home.location.latiude+.1,home.location.longitude))
#print(distance(home.location.latiude,home.location.longitude,home.location.latiude+.1,home.location.longitude+.1))
        
        
