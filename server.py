import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

stored_username = "djf"
stored_password = "1234"

password_list = {
    "netflix" : "4321",
    "youtube" : "helloworld",
    "google" : "sillypassword"
}

while True:
    username = socket.recv().decode('utf-8')
    print(f"Received Username: {username}")

    time.sleep(1)

    if username != stored_username:
        socket.send(b"Incorrect username")
        continue

    socket.send(b"Enter password")
    password = socket.recv().decode('utf-8')
    print(f"Received Password: {password}")

    time.sleep(1)

    if password != stored_password:
        socket.send(b"Incorrect password")
        continue

    socket.send(b"Login successful!")

    while True:
        user = socket.recv().decode('utf-8')

        if user == "1":
            num_letters = sum(c.isalpha() for c in password)
            num_digits = sum(c.isdigit() for c in password)
            num_symbols = len(password) - num_letters - num_digits
            length_password = len(password)

            message = b""
            if num_letters < 3:
                message += b"Your password has too few letters. "
            if num_digits < 3:
                message += b"Your password has too few numbers. "
            if num_symbols < 1:
                message += (b"Your password has no symbols! Add one or more "
                            b"symbols to increase security. ")
            if length_password < 5:
                message += (b"Your password is very short! Add more symbols, "
                            b"letters, or numbers to increase strength. ")

            if not message:
                message = b"Password strength is acceptable."

            socket.send(message)
            continue

        if user == "2":
            message = (b"It is best practice to create a password with multiple letters, symbols"
                       b"and digits. The longer your password is, the better your security will be.")

            socket.send(message)
            continue

        if user == "3":
            socket.send_pyobj(password_list)
            continue
