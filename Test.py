list1 = [1, 2, 0, 6, 5, 6, 14, 8, 9, 10]
counter = 0

for num in range(1, len(list1)-1):  # числа
    if list1[num] > list1[num-1] and list1[num] > list1[num+1]:# num в квадратных скобках становится индектом 1, число которого 2
        # 1и, это число 2 > 1-1 = 0и, а 0и = 1 and 1+1 =2и, а 2и = 0
        # 2и, это число 0 > 2-1 = 1и, а 1и = 2 and 2+1 =3и, а 3и = 4
        # 3и, это число 4 > 3-1 = 2и, а 2и = 0 and 3+1 =4и, а 4и = 5
        counter += 1
print("Кількість елементів ", counter)



list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 5
#1list1 = list1[:k] + list1[k+1:]
#2b = list1[k]
#2list1.remove(b)
#3del list1[k]
print(list1)




You will be given a sequence of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return:

true if all of the following continents / geographic zones will be represented by at least one developer: 'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.
false otherwise.
For example, given the following input array:

list1 =  [
  { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
  { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
  { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
  ]