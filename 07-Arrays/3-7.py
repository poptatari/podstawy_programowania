# Create a program that prints the longest name.

arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

longest_name = ''

for el in arr:
    if len(el) > len(longest_name):
        longest_name = el

print(f'Names: {" ".join(arr)}')
print(f'Longest name: {longest_name}')