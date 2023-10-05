class Patient:
    def __init__(self, ID, name, address, phone, veteran_status):
        self.ID = ID
        self.name = name
        self.address = address
        self.phone = phone
        self.veteran_status = veteran_status

    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def is_veteran(self):
        return self.veteran_status
