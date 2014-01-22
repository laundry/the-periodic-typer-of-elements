import os, sys, string

# TODO: put some elements up in here
elements = [(lambda x: x[0].upper() + x[1:])(x) for x in '> < + = _ - ~ @ # $ % ^ & * ( ) [ ] { } \\ | " \' , . ; ! ? H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Uut Fl Uup Lv Uus Uuo'.split(' ')]
elements.sort()
index = { x : [e for e in elements if e[0] == x.upper()] for x in list('abcdefghijklmnopqrstuvwxyz') }
vowels = list('aeiou')

# distance
def distance_phonetic(x, y):
    return 0

def distance_vowel(x, y):
    if x == y:
        return 0
    elif x in vowels and y in vowels:
        return 2
    else:
        return 4

def distance_hard(x, y):
    if x == y:
        return 0
    else:
        return 1

def distance(x, y):
    if True:
        x = x[0].lower()
        y = y[0].lower()
    return distance_vowel(x, y)

# transform
def transform_greedy(s):
    out = ''
    for word in s.split(' '):
        last = None
        for character in list(word.lower()):
            if character == last:
                last = None
                continue
            else:
                last = None
            if len(index[character]) > 0:
                out += index[character][0]
                if len(index[character][0]) > 1:
                    last = index[character][0][1]
            else:
                out += '_'
        out += ' '
    return out

def transform_dynamic(s):
    sequences = []
    E = range(len(elements))
    for word in s.split(' '):
        word = ' ' + word
        W = range(len(word))
        m = [[(999999, -1, -1, 'NOPE') for j in W] for i in E]
        # init
        for i in E:
            m[i][0] = (0, -1, i, 'START')
        # gogo
        for j in W[1:]:
            for i in E:
                # previous cheapest
                previous = min([m[ii][j-1] for ii in E])
                # previous cheapest + distance on current + tax
                new_score = previous[0] + distance(word[j], elements[i][0]) + 1
                # overwrite?
                if new_score < m[i][j][0]:
                    if len(elements[i]) == 1:
                        m[i][j] = (new_score, previous[2], i, elements[i])
                    # add to next (2 character elements)
                    else:
                        if len(elements[i]) > 1 and j < len(W)-1:
                            # empty string
                            m[i][j+1] = (new_score + distance(word[j+1], elements[i][1]), i, i, '')
                        # sickest hack (costs some to consume a 2 letter)
                        m[i][j] = (new_score+1, previous[2], i, elements[i])
        # walk the plank
        cheapest = min([m[i][-1] for i in E])
        sequence = []
        for j in W[1:]:
            sequence.append(cheapest[-1])
            cheapest = m[cheapest[1]][len(word)-j-1]
        sequence.append(cheapest[-1])
        # hello from the matrix
        if False:
            for i in E:
                for j in W:
                    print m[i][j],
                print
        sequence.reverse()
        sequences.append(''.join(sequence[1:]))
    return ' '.join(sequences)

def transform(s):
    #return transform_greedy(s)
    return transform_dynamic(s)

def main():
    for line in sys.stdin:
        print transform(line.strip())

if __name__ == '__main__':
    main()

