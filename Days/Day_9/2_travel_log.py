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
}
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(countryx, visitsx, citiesx):
    # travel_log.append({})
    # new_pos = len(travel_log) - 1
    # i = 0
    # for key in travel_log[0]:
    #     if i == 0:
    #         travel_log[new_pos][key] = countryx
    #         i += 1
    #     elif i == 1:
    #         travel_log[new_pos][key] = visitsx
    #         i += 1   
    #     elif i == 2:
    #         travel_log[new_pos][key] = citiesx
    #         i += 1
    
    new_country = {}
    new_country["country"] = countryx
    new_country["visit"] = visitsx
    new_country["cities"] = citiesx
    travel_log.append(new_country)
    
    
    
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("India", 111, ["Kerala", "Bombay"])
for i in travel_log:
    print(i)