def tedit():
    import os
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    CLEAR = '\l'
    
    while True:
        file_name = input("Enter a file name to create or edit, 'l' to list text files, or 'q' to quit: ")
        if file_name == 'q':
            break
        elif file_name == 'l':
            print(YELLOW + "Text files in current directory:" + RESET)
            for filename in os.listdir():
                if filename.endswith(".txt"):
                    print(GREEN + filename + RESET)
            print("-" * 20)
            continue

        if not file_name.endswith(".txt"):
            file_name += ".txt"

        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                file_contents = file.read()
        else:
            file_contents = ""

        while True:
            print(BLUE + "File Contents:" + RESET)
            print(file_contents)
            print("-" * 20)
            print(CYAN + "1. Edit file" + RESET)
            print(CYAN + "2. Save and exit" + RESET)
            choice = input("Enter choice: ")

            if choice == "1":
                file_contents = input("Enter file contents: ")
            elif choice == "2":
                with open(file_name, 'w') as file:
                    file.write(file_contents)
                break
            else:
                print(RED + "Invalid choice. Try again." + RESET)

    print("Exiting text editor...")
