import random, string

for i in range(20):
    filename = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(6, 30))) + '.html'
    contents = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(2000))
    f = open(filename, 'w')
    f.write(contents)
    f.close()