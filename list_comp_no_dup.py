x = set([random.randrange(10) for a in range(5)])
y = set([random.randrange(20) for b in range(10)])
final_list = [a for a in x for b in y if a == b]

print(x)
print(y)
print('start of final_list:\n', final_list)
