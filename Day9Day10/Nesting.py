# Nesting
capitals = {
  "France" : "Paris",
  "Germany" : "Berlin"
}

# Nesting a list in a Dictionary
travel_log = {
  "France":["Paris","Lille","Dijon"],
  "Germany":["Berlin","Hamburg","Stuttagart"],

}
# Nesting Dictionary in a Dictionary
travel_log = {
  "France":{"cities_visited": ["Paris","Lille","Dijon"], "total_vistis":12},
  "Germany":{"cities_visited": ["Berlin","Hamburg","Stuttagart"],"total_vistis":5},
}

# Nesting Dictionary in a List
travel_log = [
  {
      "country":"France",
      "cities_visited": ["Paris","Lille","Dijon"],
      "total_vistis":12
   },
  {
      "country":"Germany",
      "cities_visited": ["Berlin","Hamburg","Stuttagart"],
      "total_vistis":5
   },
]
# ________________________________________________________________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________________________________________________________________
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name,visits_number,cities_list):
    new_log ={}
    new_log["country"] = country_name
    new_log["visits"] = visits_number
    new_log["cities"] = cities_list
    travel_log.append(new_log)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)