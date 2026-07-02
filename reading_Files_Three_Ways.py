# Way - 1: read entire file as one string
with open("story.txt","r") as f:
    content = f.read()
    print(content)

# way - 2: read into a list of lines
with open("Story.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())


# Way 3: Loop line by line (best for large files - memory efficient)
with open("story.txt", "r") as f:
    for line in f:
        print(line .strip())
        