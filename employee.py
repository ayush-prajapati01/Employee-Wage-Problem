'''

    @Author: Ayush Prajapati
    @Date: 1-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 1-07-2024 
    @Title : Python program to implement Employee wage Problem

'''

import random


class EmployeeWage:
    WAGE_PER_HOUR = 20
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
    WORKING_DAYS = 20
    MAX_WORKING_HOURS = 100

    @classmethod
    def check_attendance(cls):
        """
        Description: 
            This returns whether employee is present or absent
        Parameters:
            None
        Return:
            int: 0 (Absent), 1 (Present), 2 (Present - Part time)
        """
        return random.randint(0, 2)


    @classmethod
    def calculate_full_time_daily_wage(cls):
        """
        Description: 
            This function calculates full time daily wage of employee
        Parameters:
            None
        Return:
            int: daily full time wage
        """
        return cls.FULL_TIME_HOUR * cls.WAGE_PER_HOUR


    @classmethod
    def calculate_part_time_wage(cls):
        """
        Description: 
            This function calculates part time wage of employee
        Parameters:
            None
        Return:
            int: daily part time wage
        """
        return cls.PART_TIME_HOUR * cls.WAGE_PER_HOUR


    @classmethod
    def calculate_appropriate_daily_wage(cls, attendance):
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
            return cls.calculate_full_time_daily_wage()
        elif attendance == 2:
            return cls.calculate_part_time_wage()
        else:
            return 0


    @classmethod
    def calculate_monthly_wage(cls):
        """
        Description: 
            This function calculates the monthly wage of an employee
        Parameters:
            None
        Return:
            int: monthly wage
        """
        employee_monthly_wage = 0
        for _ in range(cls.WORKING_DAYS):
            employee_monthly_wage += cls.calculate_appropriate_daily_wage(cls.check_attendance())
        return employee_monthly_wage


    @classmethod
    def calculate_wage_by_hours_days(cls):
        """
        Description:
            This function calculates wages till a condition of total
            working hours or days is reached for a month.
        Parameters:
            None
        Return:
            int: wage based on hours and days worked, hours, days
        """
        wage_by_hours_or_days = 0
        hours = days = 0
        while hours <= cls.MAX_WORKING_HOURS and days < cls.WORKING_DAYS:
            attendance = cls.check_attendance()
            if attendance == 1:
                hours += cls.FULL_TIME_HOUR
            elif attendance == 2:
                hours += cls.PART_TIME_HOUR

            days += 1
            wage_by_hours_or_days += cls.calculate_appropriate_daily_wage(attendance)
            
            if hours >= cls.MAX_WORKING_HOURS or days >= cls.WORKING_DAYS:
                break

        return wage_by_hours_or_days, hours, days


def main():
    print("--- Welcome to Employee Wage Computation Program ---")
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
                attendance = EmployeeWage.check_attendance()
                daily_wage = EmployeeWage.calculate_appropriate_daily_wage(attendance)
                print(f"Daily Wage: {daily_wage}")
            
            case 2:
                monthly_wage = EmployeeWage.calculate_monthly_wage()
                print(f"Monthly Wage: {monthly_wage}")
            
            case 3:
                conditional_wage, hours_worked, days_worked = EmployeeWage.calculate_wage_by_hours_days()
                print(f"Conditional Wage: {conditional_wage}")
                print(f"Hours Worked by employee: {hours_worked}")
                print(f"Days Worked by employee: {days_worked}")
            
            case _:
                print("Invalid choice. Please enter 0, 1, 2, or 3.")


if __name__ == "__main__":
   main()
