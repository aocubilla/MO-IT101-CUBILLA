# MotorPH Payroll System 

import json

DATA_FILE = "employees.json"

class Employee:
    def __init__(self, emp_id, name, position, rate_per_hour):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.rate_per_hour = rate_per_hour

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "position": self.position,
            "rate_per_hour": self.rate_per_hour
        }

class PayrollSystem:
    def __init__(self):
        self.employees = {}
        self.load_data()

    def load_data(self):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                for emp_id, emp in data.items():
                    self.employees[emp_id] = Employee(
                        emp["emp_id"],
                        emp["name"],
                        emp["position"],
                        emp["rate_per_hour"]
                    )
        except:
            pass

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump({eid: emp.to_dict() for eid, emp in self.employees.items()}, f)

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        rate = float(input("Enter Hourly Rate: "))

        self.employees[emp_id] = Employee(emp_id, name, position, rate)
        self.save_data()
        print("Employee added!\n")

    def view_employees(self):
        if not self.employees:
            print("No employees.\n")
            return

        for emp in self.employees.values():
            print(emp.emp_id, emp.name, emp.position, emp.rate_per_hour)
        print()

    def compute_salary(self):
        emp_id = input("Enter Employee ID: ")
        if emp_id not in self.employees:
            print("Not found.\n")
            return

        hours = float(input("Hours worked: "))
        emp = self.employees[emp_id]

        gross = hours * emp.rate_per_hour
        tax = gross * 0.1
        net = gross - tax

        print("\nPayslip")
        print("Name:", emp.name)
        print("Gross:", gross)
        print("Tax:", tax)
        print("Net:", net, "\n")

    def menu(self):
        while True:
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Compute Salary")
            print("4. Exit")

            choice = input("Choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.compute_salary()
            elif choice == "4":
                break

if __name__ == "__main__":
    system = PayrollSystem()
    system.menu()
