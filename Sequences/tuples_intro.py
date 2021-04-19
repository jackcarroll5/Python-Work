# t = "a", "b", "c"
# print(t)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
            ("Bad Company", "Bad Company", 1974),
            ("Nightflight", "Budgie", 1981),
            ("Hozier", "Hozier", 2013),
            ("Ride the Lightning", "Metallica", 1986),
            ]

# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# hozier = "Hozier", "Hozier", 2013
# metallica = "Ride the Lightning", "Metallica", 1986

print(len(albums))

# for name, artist, year in albums:
for album in albums:
    name, artist, year = album
    # print("Album: {}, Artist: {}, Year: {}"
    #       .format(album[0], album[1], album[2]))
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# metallica[0] = "Master of Puppets"

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)

# print()
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# print()
#
# name, length, width, height, price = table
# print(length * width)

