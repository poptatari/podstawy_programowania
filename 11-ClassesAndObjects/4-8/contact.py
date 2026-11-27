class Contact:
    def __init__(self, name: str, email: str, telephone: str):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"{self.name:<15} {self.email:<20} {self.telephone}"