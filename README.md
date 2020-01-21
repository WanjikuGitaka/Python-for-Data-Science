# Python-for-Data-Science
Learning and training!!!
# Creating an artist summary function
def artist_summary(artist):
    num_artworks = artist_freq[artist]
    template = "There are {num} artworks by {name} in the data set"
    output = template.format(name=artist, num=num_artworks)
    print(output)

artist_summary("Henri Matisse")
print(artist_summary)
