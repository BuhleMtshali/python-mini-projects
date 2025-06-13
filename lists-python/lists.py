#lists in python
example_lists = ["Mary", "John", "Dave", "Seth"];
print(example_lists);

#accessing elements within  a list
index_one = example_lists[0];
print(index_one); #prints the element at index one

#changing an item on a list
example_lists[0] = "Cindy"; #changed the first element in the array to Cindy
print(example_lists);

#adding an item to the list
example_lists.append("Michael"); #adds Michael to the end of the list
print(example_lists);

#inserting an item at a position of the list without removing that element
example_lists.insert(2, "Kate");
print(example_lists);

#removing an element by their value, like remove the element by their name
example_lists.remove("John");
print(example_lists);

#removing an element by their position Cindy has been removed from the list
del example_lists[0];
print(example_lists);

#finding the length of the list
print(len(example_lists));

#accessing the last element in a list
print(f" This is the last element in a list: {example_lists[-1]} ");

#looping through an array
for item in example_lists:
    print(f" My name is: {item}");

#looping through an array and using the title() method
looping_list = ["kate", "buhle", "zinhle", "linda"];
for name in looping_list:
    print(f"My name is {name.title()}");