counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for country in counties_dict:
    print(country) 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

