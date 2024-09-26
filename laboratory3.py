def loan_eligibility():
    # Get customer details
    monthly_salary = float(input("Enter your monthly salary: "))
    loan_amount = float(input("Enter the loan amount you are requesting: "))
    
    # Check eligibility
    if monthly_salary >= 30000:
        if loan_amount <= 10 * monthly_salary:
            print("You are eligible for the loan.")
            
            # Get repayment details
            months = int(input("Enter the number of months you would like to repay the loan: "))
            
            # Calculate interest and total amount
            interest_rate = 0.10  # 10% interest
            total_amount = loan_amount * (1 + interest_rate)
            monthly_payment = total_amount / months
            
            print(f"Loan approved with 10% interest.")
            print(f"Total amount to be repaid: {total_amount:.2f}")
            print(f"Monthly payment over {months} months: {monthly_payment:.2f}")
        else:
            print("You are not eligible for the loan because the requested amount exceeds 10 times your salary.")
    else:
        print("You are not eligible for the loan because your salary is below 30,000.")

# Run the function
loan_eligibility()
