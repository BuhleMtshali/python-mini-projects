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

#sorting based on custom rule 
list_example.sort(key=len);  #sorts it based on the length of the words
print(f"Sorting with custom rule: {list_example}");

#returning a new sorted list without mordifying the original
copy_sorted_list = sorted(list_example); #returns a list in alphabetical order
print(f"New Sorted list: {copy_sorted_list}");

#reverse sorted list
copy_reverse_list = sorted(list_example, reverse=True);
print(f"Reversed  Copy: {copy_reverse_list}");

#reversing a list in random order
list_example.reverse();
print(f"Reverse String in Random order: {list_example}");