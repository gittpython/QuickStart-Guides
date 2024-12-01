# Define the bottle_song function 
# with the start argument defaulting to 99
# page 107

def bottles_song(start = 99):
    # Set the the initial number of bottles to the start argument
    bottles = start
    #Loop through until bottles are gone
    while bottles > 0:
        # Display the song
        this_verse = []
        this_verse.append(str(bottles) + " bottles of beer on the wall. ")
        this_verse.append(str(bottles) + " bottles of beer. ")
        this_verse.append("Take one down, pass it aroud, ")
        # Subtract a bottle
        bottles -= 1
        this_verse.append(str(bottles) + " bottles of beer on the wall. ")
        # Yield to the calling function
        yield "".join(this_verse)
        # Pick back up here when we return
    return True
    
'''        print(str(bottles) + " bottles of beer in te wall.")
        print(str(bottles) + " bottles of beer.")
        print("Take one down, pass it around,")
        # Subtract a bottle
        bottles -= 1
        print(str(bottles) + " bottles of beer on the wall.\n")
        # Yield to the calling function
        yield
        # Pick backup here when we return
    return True '''

# Loop through the generTOR
for v in bottles_song():
    print(v)