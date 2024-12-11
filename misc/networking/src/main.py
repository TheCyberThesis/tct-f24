try:
    with open('flag.txt', 'r') as file:
        flag_content = file.read()
        print("Good job! Here is the flag :)")
        print(f">> {flag_content}")
except FileNotFoundError:
    print("flag file is not available. Please contact CTF organizers.")
except Exception as e:
    print(f"An error occurred: {e}")