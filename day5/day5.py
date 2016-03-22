import re
from sets import Set

lines = list(open('./input.txt').readlines())

vowels = re.compile('[aeiou]', re.IGNORECASE)

def is_nice1(string):
    return has_three_vowels(string) and has_double_letter(string) and has_no_disallowed_substrings(string)

def has_three_vowels(string):
    return len(re.sub(r'[^aeiou]', r'', string)) >= 3

def has_double_letter(string):
    for i in range(0, len(string) - 1):
        if string[i] == string[i+1]:
            return True
    return False

def has_no_disallowed_substrings(string):
    if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
        return False
    return True


def is_nice2(string):
    return has_two_pairs(string) and has_repeating_letter(string)

def has_two_pairs(string):
    counts = {}
    triples = Set()
    for i in range(0, len(string) - 1):
        if (string[i] + string[i+1]) in counts:
            counts[string[i] + string[i+1]] += 1
        else:
            counts[string[i] + string[i+1]] = 1

        if len(string) > i+2 and string[i] == string[i+1] and string[i+1] == string[i+2]:
            triples.add(string[i] + string[i+1])


    for item in triples:
        if item in counts:
            del counts[item]
    counts = Set(counts.values())
    if 1 in counts:
        counts.remove(1)
    return len(counts) > 0

def has_repeating_letter(string):
    for i in range(0, len(string) - 2):
        if string[i] == string[i+2]:
            return True
    return False

print len([line for line in lines if is_nice1(line)])
print len([line for line in lines if is_nice2(line)])

print is_nice2('qjhvhtzxzqqjkmpb')
print is_nice2('aaa')
print is_nice2('xxyxx')
print is_nice2('uurcxstgmygtbstg')
print is_nice2('ieodomkazucvgmuy')
