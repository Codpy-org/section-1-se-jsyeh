import webbrowser, sys 

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
ERROR_COUNT = 0

def input_math():
    global B1, ERROR_COUNT, UndefinedVar
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == "1": 
                open_video()
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                ERROR_COUNT += 1 
    except:
        ERROR_COUNT -= 1
        pass 

def open_video():
    webbrowser.open(X1)

input_math()
