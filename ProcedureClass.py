class Procedure:
    def __init__(self, name, date, practitioner, charge, patient_id):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge
        self.patient_id = patient_id

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_practitioner(self):
        return self.practitioner

    def get_charge(self):
        return self.charge

    def get_patient_id(self):
        return self.patient_id
