# Write a program that supports customer service in an 
# office. Use the queue. Each new customer receives a 
# ticket with an automatically assigned consecutive number 
# and is added to the end of the queue. The next customer 
# to be served is taken from the beginning of the queue.

import queue

customers = queue.Queue()
ticket_number = 1

while True:
    print("1. New customer")
    print("2. Serve next customer")
    print("0. Quit")
    menu = input("Select an option: ")

    if menu == '1':
        customers.put(ticket_number)
        print(f"Ticket number {ticket_number} issued.")
        ticket_number += 1

    elif menu == '2':
        if not customers.empty():
            next_customer = customers.get()
            print(f"Number {next_customer} is next.")
        else:
            print("The queue is empty.")

    elif menu == '0':
        break
