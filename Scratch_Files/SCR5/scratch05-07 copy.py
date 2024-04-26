# Define the genberator function
# with the start argument defaulting to 99

def bottles_song(start = 99):
    # Set the the initial number of bottles to the start argument
    bottles = start
    #Loop through until bottles are gone
    while bottles > 0:
        # Display the song
        print(str(bottles) + " bottles of beer in te wall.")
        print(str(bottles) + " bottles of beer.")
        print("Take one down, pass it around,")
        # Subtract a bottle
        bottles -= 1
        print(str(bottles) + " bottles of beer on the wall.\n")
        # Yield to the calling function
        yield
        # Pick backup here when we return
    return True

# Loop through the generTOR
for i in bottles_song():
    pass