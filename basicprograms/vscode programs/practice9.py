people = [{'name': "xxx", 'house':'gryffindor'}, {'name': 'yyy', 'house':'slytherin'}, {'name': 'zzz', 'house': 'octa'}]

people.sort(key= lambda a: a["house"])

print(people)