multiple_list = ['dave', 'ray', 'axon', 'phoebe', 'randal'];

name = 'Ray';

#checking if only 1 example exists
if name.lower() in multiple_list:
    print(f"Hey {name}");
else:
    print(f"hey stranger")