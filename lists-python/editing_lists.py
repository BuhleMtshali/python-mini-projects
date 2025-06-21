#to check if user exist we use "in"
exists_list = ["john", "mike", "dave"];

name_exists = "dave" in exists_list;

print(f"Check if user exists: {name_exists}")


#to check if they dont exist in the current we use "not";
banned_user = ["andrew", "levi", "sivvy"];
user = "levi";
if user not in banned_user:
    banned_user.append(user)
    print(f"{user.title()} you cannot post"); 
else:
    print(f"{user.title()} you're welcome to post");
print(f"Users who can post: {banned_user}");