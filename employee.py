'''

    @Author: Ayush Prajapati
    @Date: 01-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 05-07-2024 
    @Title : Python program to implement Employee wage Problem

'''


import random


class EmployeeWage:
    """
    Description: 
        This class is used for Employee Wage
    Parameters:
        employee_name, wage_per_hour, working_days, max_working_hours
    Return:
        None
    """
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4

    def __init__(self, employee_name, wage_per_hour, working_days, max_working_hours):
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
        self.hours = hours
        return wage_by_hours_or_days, hours, days, daily_wage_list




class Company:
    """
    Description:
        This class is used to manage a company and its employees
    Parameters:
        company_name
    Return:
        None
    """
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, employee_name, wage_per_hour, working_days, max_working_hours):
        """
        Description: 
            This function used to add employee
        Parameters:
            employee_name, wage_per_hour, working_days, max_working_hours
        Return:
            None
        """
        employee_wage = EmployeeWage(employee_name, wage_per_hour, working_days, max_working_hours)
        self.employees.append(employee_wage)

    def get_employee(self, employee_name):
        """
        Description: 
            This function used to get employee
        Parameters:
            employee_name
        Return:
            None
        """
        for employee in self.employees:
            if employee.employee_name == employee_name:
                return employee
        return None


    def display_employees(self):
        """
        Description: 
            This function used to display employee
        Parameters: None
        Return:
            None
        """
        for employee in self.employees:
            print(f"Employee: {employee.employee_name}, Total Wage: {employee.total_wage}")
    

    def update_employee(self, old_employee_name, new_employee_name):
        """
        Description: 
            This function used to update employee
        Parameters: old_employee_name, new_employee_name
        Return:
            None
        """
        for i, employee in enumerate(self.employees):
            if employee.employee_name == old_employee_name:
                employee.employee_name = new_employee_name
                print(f"Employee {old_employee_name} updated to {new_employee_name}.")
                return
        print(f"Employee {old_employee_name} not found in {self.company_name}.")


    def delete_employee(self, employee_name):
        """
        Description: 
            This function used to delete employee
        Parameters: employee_name
        Return:
            None
        """
        for i, employee in enumerate(self.employees):
            if employee.employee_name == employee_name:
                del self.employees[i]
                print(f"Employee {employee_name} removed from {self.company_name}.")
                return
        print(f"Employee {employee_name} not found in {self.company_name}.")
    

    def calculate_total_wage_hours(self):
        """
        Description: 
            This function used to calculate total wage and hours worked of company
        Parameters: 
        Return:
            int: company_total_wage, company_total_hours
        """
        company_total_wage = company_total_hours = 0
        for employee in self.employees:
            company_total_wage += employee.total_wage
            company_total_hours += employee.hours
        return company_total_wage, company_total_hours


class EmpWageBuilder:
    """
    Description:
        This class is used to build employee wages for multiple companies
    Parameters:
        None
    Return:
        None
    """
    def __init__(self):
        self.companies = {}


    def add_company(self, company_name):
        """
        Description: 
            This function used to add company
        Parameters: company_name
        Return:
            None
        """
        if company_name not in self.companies:
            self.companies[company_name] = Company(company_name)
            print(f"Company {company_name} added.")
        else:
            print(f"Company {company_name} already exists.")
        

    def add_company_employee(self, company_name, employee_name, wage_per_hour, working_days, max_working_hours):
        """
        Description: 
            This function used to add employee to a company
        Parameters: company_name, employee_name, wage_per_hour, working_days, max_working_hours
        Return:
            None
        """
        if company_name in self.companies:
            company = self.companies[company_name]
            company.add_employee(employee_name, wage_per_hour, working_days, max_working_hours)
            print(f"Employee {employee_name} added to company {company_name}.")
        else:
            print(f"Company {company_name} not found. Please add the company first.")


    def display_company_wages(self):
        """
        Description: 
            This function used to display wages of company
        Parameters: None
        Return:
            None
        """
        for company_name, company in self.companies.items():
            print(f"Company: {company_name}")
            company.display_employees()


    def display_total_company_wages_hours(self):
        """
        Description: 
            This function used to display total wages and hours of company
        Parameters: None
        Return:
            None
        """
        for company_name, company in self.companies.items():
            company_total_wage, company_total_hours = company.calculate_total_wage_hours()
            print(f"Total wage for company {company_name}: {company_total_wage}")
            print(f"Total hours for company {company_name}: {company_total_hours}")


    def update_company_employee(self, company_name, old_employee_name, new_employee_name):
        """
        Description: 
            This function used to update name of the employee in the company
        Parameters: company_name, old_employee_name, new_employee_name)
        Return:
            None
        """
        if company_name in self.companies:
            company = self.companies[company_name]
            company.update_employee(old_employee_name, new_employee_name)
        else:
            print(f"Company {company_name} not found.")


    def delete_company_employee(self, company_name, employee_name):
        """
        Description: 
            This function used to update name of the employee in the company
        Parameters: company_name, old_employee_name, new_employee_name)
        Return:
            None
        """
        if company_name in self.companies:
            company = self.companies[company_name]
            company.delete_employee(employee_name)
        else:
            print(f"Company {company_name} not found.")


    def list_companies(self):
        """
        Description: 
            This function used to list all companies
        Parameters: None
        Return:
            None
        """
        if not self.companies:
            print("No companies added yet.")
        for company_name in self.companies:
            print(f"Company: {company_name}")


    def delete_company(self, company_name):
        """
        Description: 
            This function used delete a company
        Parameters: company_name
        Return:
            None
        """
        if company_name in self.companies:
            del self.companies[company_name]
            print(f"Company {company_name} deleted.")
        else:
            print(f"Company {company_name} not found.")
    


def employee_wage_menu(employee_wage):
    """
    Description:
        This function displays main menu for employee wage program
    Parameters:
        object: EmployeeWage class object
    Return:
        None
    """
    print(f"\nWelcome Employee: {employee_wage.employee_name}")
    print("\nChoose an option:")
    print("0. Press 0 to exit to main menu")
    print("1. Calculate Monthly Wage")
    print("2. Calculate Conditional Monthly Wage")
    choice = int(input("Enter your choice (0, 1, 2): "))

    match choice:
        case 0:
            print(f"Exiting for {employee_wage.employee_name} ....")
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


def main():
    print("--- Welcome to Employee Wage Computation Program ---")

    emp_wage_builder = EmpWageBuilder()

    while True:
        print("\nChoose an option:")
        print("0. Press 0 to exit")
        print("1. Add Company")
        print("2. Delete Company")
        print("3. List Companies")
        print("4. Add Employee to a Company")
        print("5. Calculate Employee Wage")
        print("6. Display Total Wage")
        print("7. Display All Employees")
        print("8. Delete an Employee")
        print("9. Update an Employee")
        menu_choice = int(input("Enter your choice (0, 1, 2, 3, 4, 5, 6, 7, 8, 9): "))

        match menu_choice:
            case 0:
                print("Thank you using our Software\nExiting.....")
                break
            
            case 1:
                company_name = input("Enter the name of the company: ")
                emp_wage_builder.add_company(company_name)
            
            case 2:
                company_name = input("Enter the name of the company to delete: ")
                emp_wage_builder.delete_company(company_name)
            
            case 3:
                emp_wage_builder.list_companies()
            
            case 4:
                company_name = input("Enter the name of the company: ")
                employee_name = input(f"Enter the {company_name} Employee name: ")
                wage_per_hour = int(input("Enter wage per hour: "))
                working_days = int(input("Enter monthly working days: "))
                max_working_hours = int(input("Enter monthly working hours: "))
                emp_wage_builder.add_company_employee(company_name, employee_name, wage_per_hour, working_days, max_working_hours)
            
            case 5:
                company_name = input("Enter the name of the company: ")
                employee_name = input(f"Enter the {company_name} Employee name: ")
                company = emp_wage_builder.companies.get(company_name)
                if company:
                    employee_wage = company.get_employee(employee_name)
                    if employee_wage:
                        employee_wage_menu(employee_wage)
                    else:
                        print(f"Employee {employee_name} not found in {company_name}.")
                else:
                    print(f"Company {company_name} not found.")

            case 6:
                emp_wage_builder.display_company_wages()
                emp_wage_builder.display_total_company_wages_hours()

            case 7:
                for company_name, company in emp_wage_builder.companies.items():
                    for employee_wage in company.employees:
                        print(f"{company_name}: {employee_wage.employee_name}")

            case 8:
                company_name = input("Enter the name of the company: ")
                employee_name = input(f"Enter the {company_name} Employee name: ")
                emp_wage_builder.delete_company_employee(company_name, employee_name)

            case 9:
                company_name = input("Enter the name of the company: ")
                old_employee_name = input(f"Enter the {company_name} old Employee name: ")
                new_employee_name = input(f"Enter the {company_name} new Employee name: ")
                emp_wage_builder.update_company_employee(company_name, old_employee_name, new_employee_name)
            
            case _:
                print("Please enter a number from 0 to 9 only......")


if __name__ == "__main__":
    main()
