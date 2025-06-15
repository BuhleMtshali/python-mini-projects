#example of slicing
slicing_example = ["john", "dave", "john", "mikaela", "stella", "lizzy"];

#finding the list first
print(f"Length of the List: {len(slicing_example)}")

#slicing the list
print(f"Sliced list: {slicing_example[2:6]}") #returns items from index 2 to 5

#slicing by omiting the end value
print(f"Slicing from second value onwards: {slicing_example[3:]}") #prints from mikaela to the end