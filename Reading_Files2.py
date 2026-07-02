# ------------------------------------
# Method 1: read()
# ------------------------------------
print("===== Method 1: read() =====")

with open("story.txt", "r") as f:
    content = f.read()
    print(content)

print("Type:", type(content))
print("-" * 40)


# ------------------------------------
# Method 2: readlines()
# ------------------------------------
print("===== Method 2: readlines() =====")

with open("story.txt", "r") as f:
    lines = f.readlines()

print(lines)
print("Type:", type(lines))
print("Number of lines:", len(lines))

print("\nPrinting each line:")

for line in lines:
    print(line.strip())

print("-" * 40)


# ------------------------------------
# Method 3: Loop through file
# ------------------------------------
print("===== Method 3: for line in file =====")

with open("story.txt", "r") as f:
    for line in f:
        print(line.strip())

print("-" * 40)