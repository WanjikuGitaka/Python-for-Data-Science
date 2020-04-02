# Creating an artist summary function
def artist_summary(artist):
    num_artworks = artist_freq[artist]
    template = "There are {num} artworks by {name} in the data set"
    output = template.format(name=artist, num=num_artworks)
    print(output)

artist_summary("Henri Matisse")
print(artist_summary)
# Formatting numbers inside strings
pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = "The population of {} is {:,.2f} million"
for country in pop_millions:
    name = country[0]
    pop = country[1]
    
    output = template.format(name, pop)
    print(output) 
# Summarizing gender artwork data
ender_freq = {}
for row in moma:
    gender = row[5]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else:
        gender_freq[gender] += 1
        
for gender, num in gender_freq.items():
    template = "There are {n:,} artworks by {g} artists"
    print(template.format(g=gender, n=num))
