from random import seed, choice, randint

seed()

dictionary = {}
list_of_sources=["concrete_noun","title","adjective","abstract_noun"]
for source in list_of_sources:
    with open ("{}.txt".format(source)) as f:
        dictionary[source] = f.readlines()

patterns = open("patterns.txt").readlines()

for i in range(0,20):
    values = {key: choice(dictionary[key]).strip() for key in dictionary}
    pattern = choice(patterns)
    print(pattern.format(**values).strip())
