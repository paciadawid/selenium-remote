for i in range(1, 11):
    print(i)

my_list = ["a", "b", "c"]

for element in my_list:
    print(element)


a = 0

while a < 10:
    print(f"a is {a}")
    a += 1


##############

for i in range(10, 100, 2):
    print(i)

for i in range(10, 100):
    if i % 2 == 0:
        print(i)

for i in range(100):
    if i % 2 == 0 and i >= 10:
        print(i)

a = 10

while a < 100:
    print(a)
    a += 2
