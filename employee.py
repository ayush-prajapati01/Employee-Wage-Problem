'''

    @Author: Ayush Prajapati
    @Date: 31-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 31-07-2024 
    @Title : Python program to implement Employee wage Problem
    
'''


import random


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


if check_attendance():
    print("The employee is present")
else:
    print("The employee is absent")


if __name__ == "__main__":
    check_attendance()







