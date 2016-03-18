import md5

ZEROES = 6

def part1(start):
    i = 0
    while True:
        hash_val = get_hash("%s%s" % (start, i))
        if hash_val[:ZEROES] == '0' * ZEROES:
            return i
        i += 1

def get_hash(string):
    m = md5.new(string)
    return m.hexdigest()

input_value = 'iwrupvqb'

print part1(input_value)
