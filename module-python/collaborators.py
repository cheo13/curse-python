def read_collaborators(file_name):
    try:
        with open(file_name, 'r') as file:
            collaborators = file.readlines()
            collaborators = [collaborator.strip() for collaborator in collaborators]
        return collaborators
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return []

def display_collaborators(collaborators, count=5):
    for i, collaborator in enumerate(collaborators[:count], 1):
        print(f"{i}. {collaborator}")

def add_collaborator(file_name, collaborator):
    collaborators = read_collaborators(file_name)
    if len(collaborators) >= 15:
        print("Cannot add more collaborators, the limit is 15.")
        return

    if collaborator not in collaborators:
        with open(file_name, 'a') as file:
            file.write(collaborator + '\n')
        print(f"Collaborator {collaborator} added.")
    else:
        print(f"The collaborator {collaborator} is already in the list.")

def main():
    file_name = 'archivos\collaborators.txt'
    
    # Read existing collaborators
    collaborators = read_collaborators(file_name)
    
    # Display collaborators
    display_count = input("How many collaborators do you want to display? (Press Enter to show the first 5): ")
    if display_count.isdigit():
        display_count = int(display_count)
    else:
        display_count = 5

    display_collaborators(collaborators, display_count)

    # Add a new collaborator
    new_collaborator = input("Enter the name of the new collaborator (or press Enter to skip): ").strip()
    if new_collaborator:
        add_collaborator(file_name, new_collaborator)
    
    # Display the updated list
    print("\nUpdated list of collaborators:")
    updated_collaborators = read_collaborators(file_name)
    display_collaborators(updated_collaborators, len(updated_collaborators))

if __name__ == "__main__":
    main()
