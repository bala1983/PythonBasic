dict1 = {
  'apple': ['malum', 'pomum', 'popula'],
  'fruit': ['baca', 'bacca', 'popum'],
  'punishment': ['malum', 'multa']
}
new_dict1 = {}

for key, value in dict1.items():
    for i in value:
        if i not in new_dict1:
            new_dict1[i] = [key]
        else:
            new_dict1[i].append(key)
print(new_dict1)
