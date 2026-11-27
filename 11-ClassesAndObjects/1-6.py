class Phone:
    def __init__(self, brand):
        self.brand = brand
        self.is_locked = True
        self.message_history = []

    def unlock(self):
        self.is_locked = False

    def send_message(self):
        if self.is_locked:
            print('The phone is locked.')
        else:
            message = input('Type a message: ')
            self.message_history.append(message)
            print('Message sent!')

    def get_message_history(self):
        print(f'Messages sent from {self.brand}:')
        for message in self.message_history:
            print(message)

def main():
    phone = Phone('Samsung')
    phone.unlock()
    phone.send_message()
    phone.get_message_history()

if __name__ =="__main__":
    main()