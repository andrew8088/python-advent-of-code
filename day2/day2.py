f = open('./input.txt');
contents = f.readlines();

L = 0
W = 1
H = 2

def calcPaper(line):
    sides = [int(x) for x in line.split('x')]
    side1 = sides[L] * sides[W]
    side2 = sides[W] * sides[H]
    side3 = sides[H] * sides[L]

    return (2 * side1) +(2 * side2) + (2 * side3) + min(side1, side2, side3)

def calcRibbon(line):
    sides = sorted([int(x) for x in line.split('x')])
    return (2 * sides[0]) + (2 * sides[1]) + (sides[0] * sides[1] * sides[2])

#print sum([calcPaper(line.strip()) for line in contents])
print sum([calcRibbon(line.strip()) for line in contents])
