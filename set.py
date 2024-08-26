my_set = {"red", "green", "blue", "yellow"}
my_set.add("purple")
print(my_set)

primary_color= {"red", "blue", "yellow"}
intersection_set = my_set.intersection(primary_color)
union_set = my_set.union(primary_color)
difference_set = my_set.difference(primary_color)


print(intersection_set) 
print(union_set)
print(difference_set)


colors = {"red", "green", "blue", "yellow"}

is_green_in_colors = "green" in colors
print(f"Is 'green' in colors? {is_green_in_colors}")


is_orange_not_in_colors = "orange" not in colors
print(f"Is 'orange' not in colors? {is_orange_not_in_colors}")

