import numpy as np 
import pandas as pd 




def loan_amortization(principal, annual_rate , years):
    monthly_rate = annual_rate/100/12
    months = years *12
    monthly_payment =  round ((monthly_rate*principal) /(1-(1+monthly_rate)**-months),2)
    
    schedule =[]
    remaining_balance = principal
    
    for i in range (1, months+1):
        interest_payment = round(remaining_balance*monthly_rate,2)
        principal_payment = round(monthly_payment -interest_payment, 2)
        remaining_balance -= round(principal_payment,2)
        
        schedule.append([i,monthly_payment,principal_payment,interest_payment,remaining_balance])
        
        if remaining_balance <0 :
            remaining_balance =0
        
    df = pd.DataFrame(schedule, columns = ["Month","Monthly Payment","Principal Paid","Interest Paid","Remaining Balance"])
    return df

Example of data;
loan_amount = 100000
interest_rate = 5
loan_term = 3

amortization_table = loan_amortization(loan_amount, interest_rate, loan_term)
print(amortization_table.head(12))
