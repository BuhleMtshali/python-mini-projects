multiple_list = ['dave', 'ray', 'axon', 'phoebe', 'randal'];

name = 'zano';

#checking if only 1 example exists
if name.lower() in multiple_list:
    print(f"Hey {name}");
if name not in multiple_list:
    print(f"Lets regisister {name}")
