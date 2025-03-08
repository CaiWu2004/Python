#1

name = "Grace Hopper"
print(name[1])

value = name[len(name)-1]
print(value)

value2 = name[0:5]
print(value2)

#2

name = "alan turing"

front = name[0:4].capitalize()
back = name[5:len(name)].capitalize()

print(back)
print(front)

#3

S = "Computer Science"

CS = S[0:len(S):2]
print(CS)

CoSc = S[0:4]
CoSc2 = S[8:12]
print(CoSc + CoSc2)

#4

place = "Bletchley Park, England"

en = place[-7: len(place) ]
print(en)

backwards = place[0:9][::-1]

print(backwards)