print("Jay Jagannath")

a=400
a='400'
print(id(a))

name = 'Priyanka \N{GRINNING FACE}'  # literal
age_string = str(40)  # using str constructor
print(name)

# Constructor in parens
age = 23   # integer literal (int)
cost = 5.5   # float literal (float)
loc = 1+0j   # complex literal (complex)

# List literal
names = [name, 'simlin', 'sraddha','surya']
characters = list('aeiou')  # constructor

# Constructor is different than literal
characters = list('aeiou')  # constructor
print(characters)

print(['aeiou'])

# Tuple literal
person = ('Siya', 22, '123-432-0943', '123 North Street')
person2 = tuple(['Nabin', 43, '213-123-0987', '789 West Ave'])
print(person ,person2 )

#dictionary
type={'name':'string', 'age':'int'}
ages=dict(zip(['Simlin', 'Surya'], [23, 22]))
print(ages)