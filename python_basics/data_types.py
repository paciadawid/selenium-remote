a_int = 1  # integer, max value not bounded
a_float = 0.0  # max value not bounded

a_str = "test"  # can be also written as 'test', char doesn't exist - string is a list of chars
print(a_str[0])

a_bool = False  # 0, "", [], {}, (), None, e.g. -1 is True
print(bool(-1))

a_list = [1, "test", [1, 2]]
print(a_list[1])
# print(a_list[3])
print(a_list[-2])

a_dict = {
    "key": "value",
    "key2": "value2"
}
print(a_dict["key"])

a_tuple = (1, "test", [1, 2])  # immutable - not editable


cat = {
    "name": "pajton",
    "length": 1.2,
    "num_of_paws": 4,
    "if_hungry": True,
    "colours": ("white", "black", "grey"),
    "toys": ["ball", "mouse"]
}


print("My cat's name is {}".format(cat["name"]))
print(f"My cat's name is {cat['name']}")
