class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


# Patient class inheriting from Person
class Patient(Person):
    def __init__(self, name, age, gender, medical_history):
        super().__init__(name, age, gender)
        self.medical_history = medical_history

    def update_info(self, name=None, age=None, gender=None, medical_history=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if gender:
            self.gender = gender
        if medical_history:
            self.medical_history = medical_history
        print(f"Patient {self.name}'s information updated successfully.")

    def display_info(self):
        super().display_info()
        print(f"Medical History: {self.medical_history}")


# Doctor class inheriting from Person
class Doctor(Person):
    def __init__(self, name, age, gender, specialty):
        super().__init__(name, age, gender)
        self.specialty = specialty

    def display_info(self):
        super().display_info()
        print(f"Specialty: {self.specialty}")


# Appointment class for managing appointments
class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def display_info(self):
        print("Appointment Details:")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        self.patient.display_info()
        self.doctor.display_info()


# MedicalCenter class for overall management
class MedicalCenter:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.patients = {}
        self.doctors = {}
        self.appointments = []

    def add_patient(self):
        try:
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            gender = input("Enter patient's gender: ")
            medical_history = input("Enter patient's medical history: ")
            if name in self.patients:
                print(f"Patient {name} already exists.")
            else:
                patient = Patient(name, age, gender, medical_history)
                self.patients[name] = patient
                print(f"{patient.name} added to the patient database.")
        except ValueError:
            print("Invalid input for age. Please enter a valid number.")

    def add_doctor(self):
        try:
            name = input("Enter doctor's name: ")
            age = int(input("Enter doctor's age: "))
            gender = input("Enter doctor's gender: ")
            specialty = input("Enter doctor's specialty: ")
            if name in self.doctors:
                print(f"Doctor {name} already exists.")
            else:
                doctor = Doctor(name, age, gender, specialty)
                self.doctors[name] = doctor
                print(f"{doctor.name} added to the doctor database.")
        except ValueError:
            print("Invalid input for age. Please enter a valid number.")

    def update_patient_info(self):
        patient_name = input("Enter the patient's name to update: ")
        if patient_name in self.patients:
            name = input("Enter new name (leave blank to keep unchanged): ")
            age = input("Enter new age (leave blank to keep unchanged): ")
            gender = input("Enter new gender (leave blank to keep unchanged): ")
            medical_history = input("Enter new medical history (leave blank to keep unchanged): ")
            age = int(age) if age else None
            self.patients[patient_name].update_info(name, age, gender, medical_history)
        else:
            print(f"Patient {patient_name} not found in the database.")

    def schedule_appointment(self):
        patient_name = input("Enter patient's name: ")
        doctor_name = input("Enter doctor's name: ")
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM AM/PM): ")

        if patient_name in self.patients and doctor_name in self.doctors:
            appointment = Appointment(self.patients[patient_name], self.doctors[doctor_name], date, time)
            self.appointments.append(appointment)
            print(f"Appointment scheduled successfully for {patient_name} with {doctor_name} on {date} at {time}.")
        else:
            print("Invalid patient or doctor name.")

    def cancel_appointment(self):
        patient_name = input("Enter patient's name: ")
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM AM/PM): ")

        for appointment in self.appointments:
            if appointment.patient.name == patient_name and appointment.date == date and appointment.time == time:
                self.appointments.remove(appointment)
                print(f"Appointment for {patient_name} on {date} at {time} cancelled successfully.")
                return
        print(f"Appointment for {patient_name} on {date} at {time} not found.")

    def display_patient_info(self):
        patient_name = input("Enter patient's name to display: ")
        if patient_name in self.patients:
            self.patients[patient_name].display_info()
        else:
            print(f"Patient {patient_name} not found in the database.")

    def display_doctor_info(self):
        doctor_name = input("Enter doctor's name to display: ")
        if doctor_name in self.doctors:
            self.doctors[doctor_name].display_info()
        else:
            print(f"Doctor {doctor_name} not found in the database.")

    def display_appointments(self):
        if self.appointments:
            print("Upcoming Appointments:")
            for appointment in self.appointments:
                appointment.display_info()
                print()
        else:
            print("No upcoming appointments.")

    def display_appointments_for_patient(self):
        patient_name = input("Enter patient's name to display appointments: ")
        appointments_found = False
        for appointment in self.appointments:
            if appointment.patient.name == patient_name:
                if not appointments_found:
                    print(f"Upcoming Appointments for {patient_name}:")
                    appointments_found = True
                appointment.display_info()
                print()
        if not appointments_found:
            print(f"No upcoming appointments for {patient_name}.")

    def display_all_patients(self):
        if self.patients:
            print("All Patients:")
            for patient in self.patients.values():
                patient.display_info()
                print()
        else:
            print("No patients in the database.")

    def display_all_doctors(self):
        if self.doctors:
            print("All Doctors:")
            for doctor in self.doctors.values():
                doctor.display_info()
                print()
        else:
            print("No doctors in the database.")

def main():
    medical_center = MedicalCenter("Dhaka Medical Center", "Uttara")

    while True:
        print("\n--- Medical Center Management System ---")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Update Patient Information")
        print("4. Schedule Appointment")
        print("5. Cancel Appointment")
        print("6. Display Patient Information")
        print("7. Display Doctor Information")
        print("8. Display All Patients")
        print("9. Display All Doctors")
        print("10. Display All Appointments")
        print("11. Display Appointments for Patient")
        print("12. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            medical_center.add_patient()
        elif choice == '2':
            medical_center.add_doctor()
        elif choice == '3':
            medical_center.update_patient_info()
        elif choice == '4':
            medical_center.schedule_appointment()
        elif choice == '5':
            medical_center.cancel_appointment()
        elif choice == '6':
            medical_center.display_patient_info()
        elif choice == '7':
            medical_center.display_doctor_info()
        elif choice == '8':
            medical_center.display_all_patients()
        elif choice == '9':
            medical_center.display_all_doctors()
        elif choice == '10':
            medical_center.display_appointments()
        elif choice == '11':
            medical_center.display_appointments_for_patient()
        elif choice == '12':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
