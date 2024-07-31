'''

    @Author: Ayush Prajapati
    @Date: 31-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 31-07-2024 
    @Title : Python program to implement Employee wage Problem
    
'''


import random


WAGE_PER_HOUR = 20
FULL_TIME_HOUR = 8
PART_TIME_HOUR = 4
WORKING_DAYS = 20


print("--- Welcome to Employee Wage Computation Program ---")


def check_attendance():
    """
    Description: 
        This returns whether employee is present or absent
    Parameters:
        None
    Return:
        int: 0(Absent), 1(Present), 2(Present- Part time)
    """
    return random.randint(0,2)


def calculate_daily_wage():
    """
    Description: 
        This function calculates full time daily wage of employee
    Parameters:
        None
    Return:
        int: daily full time wage
    """
    daily_wage = FULL_TIME_HOUR * WAGE_PER_HOUR
    return daily_wage


def calculate_part_time_wage():
    """
    Description: 
        This function calculates part time wage of employee
    Parameters:
        None
    Return:
        int: daily part time wage
    """
    part_time_wage = PART_TIME_HOUR * WAGE_PER_HOUR
    return part_time_wage


def calculate_appropriate_daily_wage(attendance):
    """
    Description: 
        This function calculates appropriate wage of employee
    Parameters:
        attendance: Employee is present, part time or absent
    Return:
        int: daily wage
    """
    employee_daily_wage = 0
    match attendance:
        case 0:
            return employee_daily_wage
        
        case 1:
            employee_daily_wage = calculate_daily_wage()
            return employee_daily_wage
        
        case 2:
            employee_daily_wage = calculate_part_time_wage()
            return employee_daily_wage

        case default:
            return employee_daily_wage


def calculate_monthly_wage():
    """
    Description: 
        This function calculates part time wage of employee
    Parameters:
        None
    Return:
        int: daily part time wage
    """
    employee_monthly_wage = 0
    for _ in range(WORKING_DAYS):
        employee_monthly_wage += calculate_appropriate_daily_wage(check_attendance())
    
    return employee_monthly_wage


def main():
    print(f"\nEmployee Monthly Wage is: {calculate_monthly_wage()}")


if __name__ == "__main__":
   main()







