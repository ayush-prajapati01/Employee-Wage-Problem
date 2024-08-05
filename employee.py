'''

    @Author: Ayush Prajapati
    @Date: 01-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 03-07-2024 
    @Title : Python program to implement Employee wage Problem

'''


import random


class EmployeeWage:
    """
    Description: 
        This class is used for Employee Wage
    Parameters:
        company_name, employee_name, wage_per_hour, working_days, max_working_hours
    Return:
        None
    """

    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4

    def __init__(self, company_name, employee_name, wage_per_hour, working_days, max_working_hours):
        self.company_name = company_name
        self.employee_name = employee_name
        self.WAGE_PER_HOUR = wage_per_hour
        self.WORKING_DAYS = working_days
        self.MAX_WORKING_HOURS = max_working_hours
        self.total_wage = 0


    def check_attendance(self):
        """
        Description: 
            This returns whether employee is present or absent
        Parameters:
            None
        Return:
            int: 0 (Absent), 1 (Present), 2 (Present - Part time)
        """
        return random.randint(0, 2)

    def calculate_full_time_daily_wage(self):
        """
        Description: 
            This function calculates full time daily wage of employee
        Parameters:
            None
        Return:
            int: daily full time wage
        """
        return self.FULL_TIME_HOUR * self.WAGE_PER_HOUR


    def calculate_part_time_wage(self):
        """
        Description: 
            This function calculates part time wage of employee
        Parameters:
            None
        Return:
            int: daily part time wage
        """
        return self.PART_TIME_HOUR * self.WAGE_PER_HOUR


    def calculate_appropriate_daily_wage(self, attendance):
        """
        Description: 
            This function calculates appropriate wage of employee
        Parameters:
            attendance: Employee is present, part time or absent
        Return:
            int: daily wage
        """
        if attendance == 0:
            return 0
        elif attendance == 1:
            return self.calculate_full_time_daily_wage()
        elif attendance == 2:
            return self.calculate_part_time_wage()
        else:
            return 0

    def calculate_monthly_wage(self):
        """
        Description: 
            This function calculates the monthly wage of an employee
        Parameters:
            None
        Return:
            int: monthly wage
        """
        employee_monthly_wage = 0
        for _ in range(self.WORKING_DAYS):
            employee_monthly_wage += self.calculate_appropriate_daily_wage(self.check_attendance())
        return employee_monthly_wage


    def calculate_wage_by_hours_days(self):
        """
        Description:
            This function calculates wages till a condition of total
            working hours or days is reached for a month.
        Parameters:
            None
        Return:
            int: wage based on hours and days worked, hours, days
            list: daily wage list
        """
        wage_by_hours_or_days = 0
        hours = days = 0
        daily_wage_list = []
        while hours <= self.MAX_WORKING_HOURS and days < self.WORKING_DAYS:
            attendance = self.check_attendance()
            if attendance == 1:
                hours += self.FULL_TIME_HOUR
            elif attendance == 2:
                hours += self.PART_TIME_HOUR

            days += 1
            daily_wage_list.append(self.calculate_appropriate_daily_wage(attendance))
            wage_by_hours_or_days += self.calculate_appropriate_daily_wage(attendance)

            if hours >= self.MAX_WORKING_HOURS or days >= self.WORKING_DAYS:
                break

        self.total_wage = wage_by_hours_or_days
        return wage_by_hours_or_days, hours, days, daily_wage_list


def employee_wage_menu(employee_wage):
    """
    Description:
        This function displays main menu for employee wage program
    Parameters:
        object: EmployeeWage class object
    Return:
        None
    """
    print(f"\nWelcome to {employee_wage.company_name}, Employee: {employee_wage.employee_name}")
    print("\nChoose an option:")
    print("0. Press 0 to exit")
    print("1. Calculate Monthly Wage")
    print("2. Calculate Conditional Monthly Wage")
    choice = int(input("Enter your choice (0, 1, 2): "))

    match choice:
        case 0:
            print(f"Exiting for {employee_wage.employee_name} ....")
  
        # case 1:
        #     attendance = employee_wage.check_attendance()
        #     daily_wage = employee_wage.calculate_appropriate_daily_wage(attendance)
        #     print(f"Daily Wage: {daily_wage}")

        case 1:
            monthly_wage = employee_wage.calculate_monthly_wage()
            print(f"Monthly Wage: {monthly_wage}")

        case 2:
            conditional_wage, hours_worked, days_worked, daily_wage_list = employee_wage.calculate_wage_by_hours_days()
            print(f"Conditional Wage: {conditional_wage}")
            print(f"Hours Worked by employee: {hours_worked}")
            print(f"Days Worked by employee: {days_worked}")
            print(f"Daily Wage List of employee: {daily_wage_list}")

        case _:
            print("Invalid choice. Please enter 0, 1 or 2.")


class EmpWageBuilder:
    def __init__(self):
        self.companies = {}

    def add_company_employee(self, company_name, employee_name, wage_per_hour, working_days, max_working_hours):
        employee_wage = EmployeeWage(company_name, employee_name, wage_per_hour, working_days, max_working_hours)
        if company_name not in self.companies:
            self.companies[company_name] = []
        self.companies[company_name].append(employee_wage)

    def display_company_wages(self):
        for company_name, employees in self.companies.items():
            print(f"Company: {company_name}")
            for employee_wage in employees:
                print(f"Employee: {employee_wage.employee_name}, Total Wage: {employee_wage.total_wage}")

    def delete_company_employee(self, company_name, employee_name):
        if company_name in self.companies:
            employees = self.companies[company_name]
            for i, employee_wage in enumerate(employees):
                if employee_wage.employee_name == employee_name:
                    del employees[i]
                    print(f"Employee {employee_name} removed from {company_name}.")
                    return
            print(f"Employee {employee_name} not found in {company_name}.")
        else:
            print(f"Company {company_name} not found.")


def main():
    print("--- Welcome to Employee Wage Computation Program ---")

    emp_wage_builder = EmpWageBuilder()

    while True:
        print("\nChoose an option:")
        print("0. Press 0 to exit")
        print("1. Add Employee")
        print("2. Calculate Employee Wage")
        print("3. Display Total Wage")
        print("4. Display All Employees")
        print("5. Delete an Employee")
        menu_choice = int(input("Enter your choice (0, 1, 2, 3, 4): "))

        match menu_choice:
            case 0:
                print("Thank you using our Software\nExiting.....")
                break
            
            case 1:
                employee_exists = False
                company_name = input("Enter the name of the company: ")
                employee_name = input(f"Enter the {company_name} Employee name: ")
                wage_per_hour = int(input("Enter wage per hour: "))
                working_days = int(input("Enter monthly working days: "))
                max_working_hours = int(input("Enter monthly working hours: "))
                for company_name, employees in emp_wage_builder.companies.items():
                    for employee_wage in employees:
                        if (employee_wage.employee_name == employee_name) and (employee_wage.company_name == company_name):
                            employee_exists = True
                            break
                
                if not employee_exists:
                    emp_wage_builder.add_company_employee(company_name, employee_name, 
                                                        wage_per_hour, working_days, max_working_hours) 
                else:
                    print(f"Employee {employee_name} is already present in company {company_name}")  
            
            case 2:
                company_name = input("Enter the name of the company: ")
                employee_name = input(f"Enter the {company_name} Employee name: ")
                # Display the menu for each employee of each company
                for company_name, employees in emp_wage_builder.companies.items():
                    for employee_wage in employees:
                        if (employee_wage.employee_name == employee_name) and (employee_wage.company_name == company_name):
                            employee_wage_menu(employee_wage)

            case 3:
                # Display total wages for all companies and their employees
                emp_wage_builder.display_company_wages()

            case 4:
                for company_name, employees in emp_wage_builder.companies.items():
                    for employee_wage in employees:
                        print(f"{company_name}: {employee_wage.employee_name}")  

            case 5:
                company_name = input("Enter the name of the company: ")
                employee_name = input(f"Enter the {company_name} Employee name: ")
                emp_wage_builder.delete_company_employee(company_name, employee_name)



if __name__ == "__main__":
    main()
