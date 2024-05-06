import zmq

context = zmq.Context()

print("Connecting to Program server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    socket.send_string(username)
    response = socket.recv().decode('utf-8')

    if response == "Enter password":
        socket.send_string(password)
        response = socket.recv().decode('utf-8')

        if response == "Login successful!":
            print(response)
        else:
            print("Login failed")
            login()

    else:
        print("Login failed")
        login()


def show_recommendations():
    socket.send_string("1")

    recommendations = socket.recv().decode('utf-8')

    print("Here are your recommendations!")
    print(recommendations)


def show_safety_tips():
    socket.send_string("2")

    safety_tips = socket.recv().decode('utf-8')

    print("Here are the best practices!")
    print(safety_tips)


def show_passwords():
    socket.send_string("3")

    passwords = socket.recv_pyobj()

    print("Here are your passwords!")
    print(passwords)


if __name__ == "__main__":

    while True:
        login()

        while True:
            print("What would you like to do now?")
            print("Type 1 to see password recommendations.")
            print("Type 2 to see password best practices.")
            print("Type 3 to see your full list of passwords.")
            print("Type X at anytime to exit/logout of the program.")

            user = input("Type choice here: ")

            if user.lower() == "x":
                break

            if user == "1":
                show_recommendations()
                continue
            elif user == "2":
                show_safety_tips()
                continue
            elif user == "3":
                show_passwords()
                continue

        if user.lower() == "x":
            break
