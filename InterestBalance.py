balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12
MLP = balance / 12
MUP = (balance * ((1 + monthlyInterestRate) ** 12))/12.0
b = balance
while abs(b) > 1:
    b = balance
    lowestPayment = 0.5 * (MLP + MUP)
    for i in range(1,13):
        b = b - lowestPayment
        b = b + annualInterestRate/12 * b
    if b <= 0:
        MUP = lowestPayment  
    if b > 0:   
        MLP = lowestPayment
        
        
print("Lowest Payment:",round(lowestPayment,2))

