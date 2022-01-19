"""
# CodeSignal

After recently joining Instacart's beta testing developer group, 
you decide to experiment with their new API. You know that the API returns item-specific 
display-ready strings like 10.0% higher than in-store or 5.0% lower than in-store 
that inform users when the price of an item is different from the one in-store. 
But you want to extend this functionality by giving people a better sense of 
how much more they will be paying for their entire shopping cart.

Your app lets a user decide the total amount x they are willing to pay via Instacart 
over in-store prices. This you call their price sensitivity.

Your job is to determine whether a given customer will be willing to pay 
for the given items in their cart based on their stated price sensitivity x.

Example

For
prices = [110, 95, 70],

notes = ["10.0% higher than in-store", 
         "5.0% lower than in-store", 
         "Same as in-store"]
and x = 5, the output should be
solution(prices, notes, x) = true.

In-store prices of the first and the second items are 100, 
and the price of the third item is 70, 
which means the customer is overpaying 10 - 5 + 0 = 5, 
which they are willing to do based on their price sensitivity.

For
prices = [48, 165],

notes = ["20.00% lower than in-store", 
         "10.00% higher than in-store"]
and x = 2, the output should be
solution(prices, notes, x) = false.

The in-store price of the first item is 60, and the second item is 150. 
The overpayment equals 15 - 12 = 3, which is too much for the customer to be willing to pay.


"""
def truncate_float(n, places):
    return int(n * (10 ** places)) / 10 ** places

def get_percentage(note):
    percentage = 0
    notes_split = note.split("% ")
    float_val = float(notes_split[0])
    if notes_split[1][0] =="l":
        return percentage - float_val
    else:
        return percentage + float_val

def get_overpayment(percentage, price):
    store_val = ( (100.0+(percentage)) / 100)
    original_price = round(float(price) / store_val)
    return abs(float(price) - (original_price))
    
def solution(prices, notes, x):
    value = 0
    for i in range(len(prices)):
        if notes[i][0].isnumeric():
            notes_split = notes[i].split("% ")
            percentage = get_percentage(notes[i])
            over_payment = get_overpayment(percentage,prices[i])
            if percentage == 0.001:
                return False
            if notes_split[1][0] =="l" and percentage >= -100:
                value -= over_payment
                print(value)
            else:
                value += over_payment
                print(value)

    if round(value,2) <= x:
        return True
    return False
            


prices= [110, 95, 70]
notes=["10.0% higher than in-store", 
 "5.0% lower than in-store", 
 "Same as in-store"]
x= 5

print(solution(prices, notes, x))