keylist = input("D:\\New folder (2)", "r")

keyword = []
identifiers = []
operators = []
logical = []
numbers = []
others = []


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


file = open('input.txt', 'r')
for i in file:
    for line in i.split():
        if line == ('==') or line == ('>=') or line == ('<==') or line == ('>') or line == ('<'):
            if line not in logical:
                logical.append(line)

        elif line == ('+') or line == ('-') or line == ('='):
            if line not in operators:
                operators.append(line)

        elif line.isalpha() == True:
            if line not in identifiers:
                identifiers.append(line)

        elif is_integer(line) == True:
            if line not in numbers:
                numbers.append(line)

        elif line in keylist:
            if line not in keyword:
                keyword.append(line)

        else:
            if line not in others:
                others.append(line)

print("Keywords:", '%s' % ', '.join(map(str, keyword)))
print("Identifiers:", '%s' % ', '.join(map(str, identifiers)))
print("Math Operators:", '%s' % ', '.join(map(str, operators)))
print("Logical Operators:", '%s' % ', '.join(map(str, logical)))
print("Numbers:", '%s' % ', '.join(map(str, numbers)))
print("Others:", '%s' % ' '.join(map(str, others)))
