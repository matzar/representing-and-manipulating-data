from operator import itemgetter
stats = {'a':(1000, 2000), 'b':(3000, 200), 'c':(100, 100), 'd':(100, 100), 'e':(100, 2000), 'f':(1000, 2000)}
st_keys = stats.keys()
st_values = stats.values()



# st_values[st_keys.index(ind)]


max_pair = max(stats.items(), key=lambda i : i[1][1])
print(max_pair[0], max_pair[1][1])

