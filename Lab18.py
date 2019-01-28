#!/usr/bin/python

############
#FUNCTION NAME: mapMe()
#Inputs: None
#Returns a tuple containing GPS coordinates of Latitude and Longitude
##############
def mapMe():
    #This is Geo-Coordinates for Chicago
    latitude = ('41.881832 degrees North')
    longitude = ('-87.6298 de-+grees West')

    #line 15 works because Python packs it into a tuple
    #line 16 works because you are returning it in a tuple!

    print ()
    print('return latitude, longitude')
    return latitude, longitude

    #print('return (latitude, longitude)')
    #return (latitude, longitude)

    #Line 19 works becuse it is a list! Its also consitered 'one thing'!
   # return [latitude,longitude]

print('The Geo-coordinates for chicago are:')
myLocation = mapMe() # Here, we are assigning the return value of the function mapMe to my location

print("what does mapMe return??? A list or a tuple?")
print("... A list is fomratted with square brackets [1,2,3,].")
print("... A tuple is formatted with parentheses (1,2,3)'")
print()

print("myLocation is:",myLocation)
print("")
print("\t" +'My latitude is: ' + str(myLocation[0]))
print ("\t" +'My longitude is: ' + str(myLocation[1]))