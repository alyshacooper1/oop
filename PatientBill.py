import PatientClass as pc
import ProcedureClass as prd

patient1 = pc.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", True)

procedure1 = prd.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
procedure2 = prd.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
procedure3 = prd.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)

procedures = [procedure1, procedure2, procedure3]

total_charge = 0

print('*** Patient Bill ***')
print(f"Name: {patient1.get_name()}")
print(f"Address: {patient1.get_address()}")
print(f"Phone: {patient1.get_phone()}")


for procedure in procedures:
    patient_id = procedure.get_patient_id()
    if patient_id == patient1.get_ID():
        total_charge += procedure.get_charge()
        print()
        print(f"Procedure: {procedure.get_name()}")
        print(f"Date: {procedure.get_date()}")
        print(f"Practitioner: {procedure.get_practitioner()}")
        print(f"Charge: ${procedure.get_charge():.2f}")
        print()

if patient1.is_veteran():
    total_charge *= 0.6  # 40% discount for veterans

print(f"Total Charges: ${total_charge:.2f}")
