# While loop - repeats as long as the condition is true.
count = 1
while count <= 5:
    print(count)
    count += 1
# while with user input
while True:
    answer = input("Type 'quit' to stop: ")
    if answer == "quit":
        break
    print("You typed: ", answer)
# while with flag 
"""
A while loop with a flag uses a variable(called flag) to control
when the loop should stop.
The flag is usually a Boolean(true or false)
"""
game_running = True
lives = 3
while game_running:
    lives -= 1
    if lives == 0:
        game_running = False
print("Game over!")
