import re

pattern = r'^(?!(..+)\1+$).+'
regex = re.compile(pattern)

count = 1

while True:
	count += 1
	test_str = '1' * count
	if regex.match(test_str):
		print(count)