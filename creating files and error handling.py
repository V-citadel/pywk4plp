# Step 1: Create a new file
vincefile = open("trialfile.txt", "w")
# Step 2: Write some data into the file
vincefile.write("I am going to be the best software dev in Kenya.")

vincefile.close()

print("File created successfully.")

# Step 3: Read the file that was just created
with open("trialfile.txt", "r") as newvincefile:
    content = newvincefile.read()

# Modify the content to uppercase
modified_content = content.upper()
print("Modified Content:")
print(modified_content)

# Error handling with a loop
# Prompt the user for their name
name = input("Please enter your name: ")

# Use a loop to handle file name input and errors
while True:
    file_name = input(f"Hello {name}, please enter the name of the file that you are looking for!: ")

    try:
        # Attempt to open the specified file
        with open(file_name, "r") as file_to_read:
            content = file_to_read.read()
            print("\nFile found! Here's the content:")
            print(content)

        # Exit the loop if the file was successfully opened
        break

    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"\nThe file '{file_name}' doesn't exist. Please check and try again.")