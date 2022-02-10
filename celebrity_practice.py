# there are 3 people, the one in the position 2 is the celebrity. The celebrity don't know anyone but everyone knows her/him. 
# based on the celebrity definition, we know that it is only posible to have one celebrity on the list
people_list = [0,1,2]

# the know matrix shows to whom knows the person.
known_matrix = [[0 ,0 ,1],
                [1, 0, 1],
                [0, 0, 0]]

def know(a, b):
    tmp_a = people_list.index(a)
    tmp_b = people_list.index(b)
    if known_matrix[tmp_a][tmp_b] == 1:
        return True
    else:
        return False

# need to find the one that knows all but one (himself)

def findCelebrity(list):
    list_len = len(list)
    knowed_list = []
    unknowed_list = []
    for i in list:
        c = 0
        d = 0
        for j in list:
            if know(j, i):
                c = c + 1
            if know(i, j):
                d = d + 1
        knowed_list.append(c)
        unknowed_list.append(d)
    top_knowed_list = [z for z, x in enumerate(knowed_list) if x == (list_len - 1)]
    top_unknowed_list = [z for z, x in enumerate(unknowed_list) if x == 0]

    result = set(top_knowed_list) & set(top_unknowed_list)

    print(result)

findCelebrity(people_list)