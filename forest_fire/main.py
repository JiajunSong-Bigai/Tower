from pyswip import Prolog

# Initialize Prolog
prolog = Prolog()

# Consult the Prolog file
prolog.consult("facts.pl")
prolog.consult("rules.pl")

# Define queries
queries = [
    "fire_spread_area(current, SpreadArea)",
    "fire_size(Size)",
    "take_action(current)",
]

facts = [
    "weather(rain)",
    "wind_direction(north)",
    "north_adjacent(current, village)",
    "east_adjacent(current, lake)",
    "south_adjacent(current, river)",
    "west_adjacent(current, forest)",
]

# Execute queries and print results
for query in queries:
    print(f"Query: {query}", end=" => ")
    result = list(prolog.query(query))
    if result:
        print(result)
    else:
        print("false")
