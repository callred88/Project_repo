import random


destinations = ["Gulf Shores", "Branson", "Hot Springs", "New Orleans"]
restaurants = ["Red Lobster", "Olive Garden", "Outback Steakhouse", "Windy City Grill"]
mode_of_transportation = ["Car", "Train", "Plane", "Helicopter"]
entertainment = ["Movies", "Bowling", "Water Park", "Museum"]

day_trip_dictionary = {
    "destination" : "",
    "entertainment" : "",
    "transportation" : "",
    "restaurant" : ""
}



def day_trip_welcome():
    print("Welcome to our trip planner!")
    print("---------")
    print("Let's get started.")
    print("---------")
def day_trip_destination():
    user_is_happy = False
    while user_is_happy == False:
     random_destination = random.choice(destinations)
     user_input = input(f"Would you like to go to {random_destination}?" )
     if user_input == "yes":
        user_is_happy = True
        day_trip_dictionary["destination"] = random_destination
def day_trip_entertainment():
    user_is_happy = False
    while user_is_happy == False:
     random_entertainment = random.choice(entertainment)
     user_input = input(f"Would you like to go to {random_entertainment}?" )
     if user_input == "yes":
        user_is_happy = True
        day_trip_dictionary["entertainment"] = random_entertainment
def day_trip_transportation():
    user_is_happy = False
    while user_is_happy == False:
     random_transportation = random.choice(mode_of_transportation)
     user_input = input(f"Would you like to go to {random_transportation}?" )
     if user_input == "yes":
        user_is_happy = True
        day_trip_dictionary["transportation"] = random_transportation
def day_trip_restaurant():
    user_is_happy = False
    while user_is_happy == False:
     random_restaurant = random.choice(restaurants)
     user_input = input(f"Would you like to go to {random_restaurant}?" )
     if user_input == "yes":
        user_is_happy = True
        day_trip_dictionary["restaurant"] = random_restaurant

def day_trip_check():
    print("--------------------")
    destination = day_trip_dictionary.get("destination")
    transportation = day_trip_dictionary.get("transportation")
    entertainment_choice = day_trip_dictionary.get("entertainment")
    restaurant = day_trip_dictionary.get("restaurant")
    print (f"You are going to {destination} by way of {transportation} and you will enjoy the {entertainment_choice} after eating at {restaurant}.")
    print("--------------------")
    user_is_happy = False
    if user_is_happy == False:
     user_input = input(f"Are you sure you happy with the trip planned?" )
     if user_input == "yes":
        user_is_happy = True
        print ("Have a great day on your trip!"  )
     day_trip_destination()  
     day_trip_entertainment()
     day_trip_transportation()
     day_trip_restaurant()

day_trip_welcome()
day_trip_destination()
day_trip_entertainment()
day_trip_transportation()
day_trip_restaurant()
day_trip_check()

