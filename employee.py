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


print("--- Welcome to Employee Wage Computation Program ---")


def check_attendance():
    """
    Description: 
        This returns whether employee is present or absent
    Parameters:
        None
    Return:
        boolean: True for present, False for absent
    """
    if random.randint(0,1) == 1:
        # Employee Present if choice equal to 1
        return True                 
    else:
        return False
    

def calculate_daily_wage():
    daily_wage = 0
    if check_attendance():
        daily_wage = FULL_TIME_HOUR * WAGE_PER_HOUR
        print(f"The employee is present full time, Daily wage is : {daily_wage}")
    else:
        print(f"The employee is absent, Daily wage is : {daily_wage}")


if __name__ == "__main__":
    calculate_daily_wage()







