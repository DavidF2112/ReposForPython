def check_text(text):
    for i in range(len(text)):
        if text[i] == "admin":
            print("HELLO WORLD!")
        else:
            print("Error")


enter_text = input("Enter some text: ").lower()
check_text(enter_text)