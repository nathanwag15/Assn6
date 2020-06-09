#Nathan Wagstaff assn 6 cs1400
#task 2

#user inputs
name = input("Enter the employee's name: ")
weeklyHours = eval(input("Enter the number of hours worked in a week: "))
hourlyPay = eval(input("Enter hourly pay rate: " ))
federalTax = eval(input("Enter federal tax withholding rate (ex. 0.12): "))
stateTax = eval(input("Enter state tax withholding rate (ex. 0.06): "))

#formulas

grossPay = hourlyPay * weeklyHours
federalW = grossPay * federalTax
stateW = grossPay * stateTax
totalDeduction = federalW + stateW
netPay = grossPay - totalDeduction

#tax percentages
federalTax = federalTax * 100
stateTax = stateTax * 100
federalTax = round(federalTax, 1)
stateTax = round(stateTax, 1)

#results
print("\n",
      format(name, ">25").upper(), "pay information".upper(), "\n",
      "\n",  format("Pay", ">25"), "\n",
      format("Hours Worked:", ">32"), format(weeklyHours, ">12.0f"), "\n",
    format("Pay Rate: $", ">34"), format(hourlyPay, ">10.2f"), "\n",
      format("Gross Pay: $", ">34"), format(grossPay, ">10.2f"), "\n",
      "\n",
      format("Deductions", ">30"), "\n",
      format(f"Federal Withholding ({federalTax}%): $", ">34"), format(federalW, ">10.2f"), "\n",
      format(f"State Withholding ({stateTax}%): $", ">34"), format(stateW, ">10.2f"), "\n",
      format("Total Deduction: $", ">34"), format(totalDeduction, ">10.2f"), "\n",
      "\n",
      format("Net Pay: $", ">34"), format(netPay, "10.2f"))