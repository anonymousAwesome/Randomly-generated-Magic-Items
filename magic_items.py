from random import seed, choice, randint

seed()

dictionary = {}
dictionary["concrete_noun"] = open("concrete_noun.txt").readlines()
dictionary["title"]         = open("title.txt").readlines()
dictionary["adjective"]     = open("adjective.txt").readlines()
dictionary["abstract_noun"] = open("abstract_noun.txt").readlines()

patterns = open("patterns.txt").readlines()

for i in range(0,20):
    values = {key: choice(dictionary[key]).strip() for key in dictionary}
    pattern = choice(patterns)
    print(pattern.format(**values).strip())
