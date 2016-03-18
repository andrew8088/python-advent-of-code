from sets import Set

instructions = list(open('./input.txt').read())

def part1 (insts):
    houses = Set()
    V = 0
    H = 0
    houses.add('%s-%s' % (V,H))

    for inst in insts:
        if inst == '^': V += 1
        if inst == 'v': V -= 1
        if inst == '>': H += 1
        if inst == '<': H -= 1
        houses.add('%s-%s' % (V,H))

    return houses

def part2 (insts):
    sHouses = Set()
    rHouses = Set()
    sV = 0
    sH = 0
    rV = 0
    rH = 0

    sHouses.add('%s-%s' % (sV,sH))
    rHouses.add('%s-%s' % (rV,rH))

    for idx, inst in enumerate(insts):
        if idx % 2 == 0:
            #santa
            if inst == '^': sV += 1
            if inst == 'v': sV -= 1
            if inst == '>': sH += 1
            if inst == '<': sH -= 1
            sHouses.add('%s-%s' % (sV,sH))
        else:
            #robo-santa
            if inst == '^': rV += 1
            if inst == 'v': rV -= 1
            if inst == '>': rH += 1
            if inst == '<': rH -= 1
            rHouses.add('%s-%s' % (rV,rH))

    return sHouses.union(rHouses)

#print len(part1(instructions))
print len(part2(instructions))
