
from random import *

seed()


for i in range(0,20):
    combination=randint(1,6)
    #combination=4

    if combination==1:
        num_lines = sum(1 for line in open("concrete_noun.txt"))
        result=open("concrete_noun.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        result+=" of the "
        num_lines = sum(1 for line in open("title.txt"))
        result+=open("title.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        print(result)
        
    elif combination==2:
        num_lines = sum(1 for line in open("title.txt"))
        result=open("title.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        result+="\'s "
        num_lines = sum(1 for line in open("concrete_noun.txt"))
        result+=open("concrete_noun.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        print(result)

    elif combination==3:
        num_lines = sum(1 for line in open("adjective.txt"))
        result=open("adjective.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        result+=" "
        num_lines = sum(1 for line in open("concrete_noun.txt"))
        result+=open("concrete_noun.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        print(result)

    elif combination==4:
        num_lines = sum(1 for line in open("concrete_noun.txt"))
        result=open("concrete_noun.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        result+=" of "
        num_lines = sum(1 for line in open("abstract_noun.txt"))
        result+=open("abstract_noun.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        print(result)
    
    elif combination==5:
        num_lines = sum(1 for line in open("adjective.txt"))
        result=open("adjective.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        result+=" "
        num_lines = sum(1 for line in open("concrete_noun.txt"))
        result+=open("concrete_noun.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        result+=" of "
        num_lines = sum(1 for line in open("abstract_noun.txt"))
        result+=open("abstract_noun.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        print(result)
    
    elif combination==6:
        num_lines = sum(1 for line in open("adjective.txt"))
        result=open("adjective.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        result+=" "
        num_lines = sum(1 for line in open("concrete_noun.txt"))
        result+=open("concrete_noun.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        result+=" of the "
        num_lines = sum(1 for line in open("title.txt"))
        result+=open("title.txt").readlines()[randint(0, num_lines-1)].splitlines()[0]
        print(result)
