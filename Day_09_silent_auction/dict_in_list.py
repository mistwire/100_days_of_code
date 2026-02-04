# KEY CONCEPT: Nested Data Structures - List of Dictionaries
# This travel_log combines two data types:
# - Outer: List (ordered collection)
# - Inner: Dictionary (key-value pairs for each entry)
# Why? Each country needs multiple related fields (name, visits, cities)

country = input("Add country name: ")
visits = int(input("Number of visits"))
list_of_cities = eval(input(["Sao Paulo", "Rio de Janeiro"]))  # Parse string into list

# NESTED STRUCTURE PATTERN:
# travel_log[0] returns a dict for France
# travel_log[0]["country"] returns "France"
# travel_log[0]["cities"][0] returns "Paris" (accessing list inside dict)
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
# Do NOT change the code above 👆

# FUNCTION PURPOSE: Build a new country dict and append to the list
# This demonstrates: 1) dict construction, 2) list.append(), 3) maintaining structure
def add_new_country(country_name, visits, list_of_cities):
  """Create a new country entry with same structure as existing entries."""
  new_info = {"country": country_name,
              "visits": visits,
              "cities": list_of_cities}
  travel_log.append(new_info)  # Add to list - now travel_log has 3 entries

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)

# NESTED ACCESS: travel_log[2] = new entry, ['country'] = the country name
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")

# TRIPLE NESTING: travel_log[2] (dict) → ['cities'] (list) → [0] (first city)
print(f"My favourite city was {travel_log[2]['cities'][0]}.")