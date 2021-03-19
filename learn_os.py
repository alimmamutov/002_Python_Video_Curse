import os


# OS NAME
print(os.name)

# current directory
print(os.getcwd())

# create new path
new_path = os.path.join(os.getcwd(), 'new_f')

# create new folder at new path
os.mkdir(new_path)
