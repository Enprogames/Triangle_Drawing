import math

def square(radicand):
    perfect_squares = []
    gcf = 0
    for i in range(1, 17):
        perfect_squares.append(i**2)
    for i in range(16):
        if (radicand % perfect_squares[i]) == 0:
            gcf = perfect_squares[i]
    return (u"{}\u221A{}").format(int(math.sqrt(gcf)), int(radicand / gcf))

def cube(radicand):
    perfect_cubes = []
    gcf = 0
    for i in range(1, 7):
        perfect_cubes.append(i**3)
    for i in range(6):
        if (radicand % perfect_cubes[i]) == 0:
            gcf = perfect_cubes[i]
    return (u"{}\u221A{}").format(round(math.pow(gcf, 1/3)), int(radicand / gcf))

def tetra(radicand):
    perfect_tesseracts = []
    gcf = 0
    for i in range(1, 5):
        perfect_tesseracts.append(i**4)
    for i in range(4):
        if (radicand % perfect_tesseracts[i]) == 0:
            gcf = perfect_tesseracts[i]
    return (u"{}\u221A{}").format(round(math.pow(gcf, 1/4)), int(radicand / gcf))

def penta(radicand):
    perfect_hypercubes = []
    gcf = 0
    for i in range(1, 4):
        perfect_hypercubes.append(i**5)
    for i in range(3):
        if (radicand % perfect_hypercubes[i]) == 0:
            gcf = perfect_hypercubes[i]
    return (u"{}\u221A{}").format(round(math.pow(gcf, 1/5)), int(radicand / gcf))

def whole_to_mixed(index, radicand):
    if index == 2:
        return square(radicand)
    elif index == 3:
        return cube(radicand)
    elif index == 4:
        return tetra(radicand)
    elif index == 5:
        return penta(radicand)

#index = int(input("Please enter an index for the whole radical: "))
#radical = int(input("Enter a number inside of a whole radical e.g. 5: "))

#print(round(math.pow(32, 1/5))

print(whole_to_mixed(2, 19860))

#print((u"{}\u221A{}").format(int(math.sqrt(squaregcf)), int(radical / squaregcf)))

print("Program Ended")
