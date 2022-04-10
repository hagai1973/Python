

travel_log = [
              {
                  "country":"france",
                  "cities_vistied": ["Paris","Lille","Dijon"],
                  "total_time": 5
                  },
              {
                  "country":"germany",
                  "cities_vistied": ["Berlin","Humburg","Stuttgart"],
                  "total_time": 6
                },
             ]


country = "Russia"
visited_cities = ["Moscow", "Saint Petersuburg"]
visit_number = 2

def add_new_country(country_name, visted_cities, visit_number):
    travel_log.append({"country": country, "cities_visited": visited_cities, "total_time": visit_number} ) 
    # return travel_log


add_new_country(country, visited_cities, visit_number)

print(travel_log)