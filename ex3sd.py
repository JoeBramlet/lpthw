#find some thing to calculate 

storage = 150.00
months = 12

annual_fees = storage * months
print(annual_fees)                                          #raw number
print ('This is how you format money: F"${variable:.2f}"') 
print(f"${annual_fees:.2f}")                                #formated as money
