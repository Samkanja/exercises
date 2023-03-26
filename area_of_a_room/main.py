
def area_of_room(lenght, width):
    return f'The area of the room {length * width}'

length, width = map(int, input('length and width: ').split())

print(area_of_room(length,width))