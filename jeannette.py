import array

# Integers: Generate/input egg counts for different days
egg_counts = [34, 28, 42, 37, 31, 40, 35]  # Example data for a week

total_eggs = sum(egg_counts)
average_eggs = total_eggs / len(egg_counts)
min_eggs = min(egg_counts)
max_eggs = max(egg_counts)

# Strings: Formatted report with f-strings
report = (
    f"Poultry Egg Count Report\n"
    f"--------------------------\n"
    f"Total Eggs Collected: {total_eggs}\n"
    f"Average Eggs per Day: {average_eggs:.2f}\n"
    f"Minimum Eggs in a Day: {min_eggs}\n"
    f"Maximum Eggs in a Day: {max_eggs}\n"
)
print(report)
print(f"Summary: {len(egg_counts)} days, total {total_eggs} eggs, avg {average_eggs:.2f}/day")

# Booleans: Threshold check with compound condition
THRESHOLD = 36
if average_eggs > THRESHOLD and max_eggs > 40:
    print("Status: Above Standard 🥚🐔")
elif average_eggs > THRESHOLD or max_eggs > 40:
    print("Status: Near Standard")
else:
    print("Status: Below Standard")

# Lists: Manage egg count records
print("\nOriginal egg counts:", egg_counts)

# Add a new day's count
egg_counts.append(38)
print("After adding new day's count:", egg_counts)

# Remove days with below 30 eggs
egg_counts = [count for count in egg_counts if count >= 30]
print("After removing days with <30 eggs:", egg_counts)

# Sort and display
egg_counts.sort()
print("Sorted egg counts:", egg_counts)

# Arrays: Use array module for a fixed-size subset (first 5 days)
egg_array = array.array('i', egg_counts[:5])
array_sum = sum(egg_array)
print(f"\nArray of first 5 egg counts: {egg_array.tolist()}")
print(f"Sum of array: {array_sum}")
print(f"Sum matches list sum? {array_sum == sum(egg_counts[:5])}")

# Dictionaries: List of egg records for each day
egg_records = [
    {"id": 1, "name": "Monday", "value": 34},
    {"id": 2, "name": "Tuesday", "value": 28},
    {"id": 3, "name": "Wednesday", "value": 42},
    {"id": 4, "name": "Thursday", "value": 37},
    {"id": 5, "name": "Friday", "value": 31},
]

# Update Wednesday's count
for record in egg_records:
    if record["name"] == "Wednesday":
        record["value"] = 44  # update value

# Delete Tuesday's record
egg_records = [rec for rec in egg_records if rec["name"] != "Tuesday"]

# Compute total eggs from records
total_from_dicts = sum(rec["value"] for rec in egg_records)

print("\nEgg Records after update and delete:")
for rec in egg_records:
    print(f"Day: {rec['name']}, Eggs: {rec['value']}")

print(f"Total eggs from records: {total_from_dicts}")
