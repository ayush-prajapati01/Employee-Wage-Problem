'''

    @Author: Ayush Prajapati
    @Date: 1-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 1-07-2024 
    @Title : Python program to implement Employee wage Problem

'''

import random


class EmployeeWage:
    """
    Description: 
        This class is used for Employee Wage
    Parameters:
        wage_per_hour, working_days, max_working_hours
    Return:
        None
    """

    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4


    def __init__(self, company_name, wage_per_hour, working_days, max_working_hours):
        self.company_name = company_name
        self.WAGE_PER_HOUR = wage_per_hour
        self.WORKING_DAYS = working_days
        self.MAX_WORKING_HOURS = max_working_hours


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

        return wage_by_hours_or_days, hours, days, daily_wage_list


def employee_wage_menu(company_name):
    """
    Description:
        This function displays main menu for employee wage program
    Parameters:
        object: EmployeeWage class object
    Return:
        None
    """
    print(f"\nWelcome to {company_name.company_name}")
    while True:
        print("\nChoose an option:")
        print("0. Press 0 to exit")
        print("1. Calculate Daily Wage")
        print("2. Calculate Monthly Wage")
        print("3. Calculate Wage by Hours and Days Condition")
        choice = int(input("Enter your choice (0, 1, 2, 3): "))

        match choice:
            case 0:
                print("\nThank you for using Employee Wage Problem!!!\nExiting....")
                break
        
            case 1:
                attendance = company_name.check_attendance()
                daily_wage = company_name.calculate_appropriate_daily_wage(attendance)
                print(f"Daily Wage: {daily_wage}")
            
            case 2:
                monthly_wage = company_name.calculate_monthly_wage()
                print(f"Monthly Wage: {monthly_wage}")
            
            case 3:
                conditional_wage, hours_worked, days_worked, daily_wage_list = company_name.calculate_wage_by_hours_days()
                print(f"Conditional Wage: {conditional_wage}")
                print(f"Hours Worked by employee: {hours_worked}")
                print(f"Days Worked by employee: {days_worked}")
                print(f"Daily Wage List of employee: {daily_wage_list}")
            
            case _:
                print("Invalid choice. Please enter 0, 1, 2, or 3.")


def main():
    print("--- Welcome to Employee Wage Computation Program ---")

    # Creating Objects
    company1 = EmployeeWage('TCS', 20, 20, 100)
    # Display the menu for the user
    employee_wage_menu(company1)

    Infosys = EmployeeWage('Infosys', 30, 30, 150)
    employee_wage_menu(Infosys)


if __name__ == "__main__":
   main()
