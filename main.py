import os  # This line imports the 'os' module, which provides a way of using operating system dependent functionality.

if __name__ == "__main__":  # This block is executed when the script is run directly, not imported as a module.

    print("Welcome to RoboSpeaker created by Mohit")  # This line prints a welcome message for the user.

    while True:  # This loop continues indefinitely until it's broken.

        x = input("Enter what you want to listen from me:")  # This line prompts the user to enter a string and assigns it to the variable 'x'.

        if x == "stop":  # This conditional block checks if the user entered 'stop'.
            break  # If 'stop' is entered, the loop is broken and the program ends.

        command = f"say {x}"  # This line creates a command string that will be executed using the 'os' module.
        
        os.system(command)  # This line executes the command string using the 'os' module.