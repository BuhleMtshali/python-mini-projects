list_example = ["ray", "josh", "mikaela", "janine", "rose", "mandy"];

#modifying an element by its position
list_example[0] = "rachel";
print(f"Modified list: {list_example}");

#adding an element to array
added_list = list_example.append("zakery");
print(f"Appended list: {list_example}");

#sorting an element in ascending order
list_example.sort();
print(f"Sorted list: {list_example}");

#sorting a list in descending order
list_example.sort(reverse=True);
print(f"Descending Order: {list_example}");