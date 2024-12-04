from collections import Counter

test_list1 = [4, 6, 8, 9, 10]
test_list2 = [4, 6, 6, 5, 8, 10, 4, 9, 8, 10, 1]


print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

res = dict(Counter(test_list2))

res = {key: val for key, val in res.items() if key in test_list1}

for key in test_list1:

	res.setdefault(key, 0)


print("Lists elements Frequency : " + str(res))
