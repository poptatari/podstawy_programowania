all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

# Find elements present in one set but not the other.
absent_students = all_students - attended_students # Difference
print(absent_students)