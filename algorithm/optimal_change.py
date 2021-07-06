# 거스름돈
def optimal_change(item_cost, amount_paid):
    #declare template string which will be the first half of expected output string
    result_string_template = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is " ##1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
    #declare empty string which will 
    result_string_to_be_added = ""
    change = amount_paid -item_cost
    print(change)
    moneys = [
        {"$20":20}, 
        {"$10":10} ,
        {"$5" :5}, 
        {"$1" :1}, 
        {"quarter": 0.25}, 
        {"dime": 0.1}, 
        {"nickle": 0.05}, 
        {"penny": 0.01}]
    for money_obj in moneys:
        for key in money_obj:
            money_amt = money_obj[key]
            while change >= money_amt:
                money_count = int(change // money_amt)
                change = round(change - (money_amt * money_count),2)
                
                print(change)
                result_string_to_be_added += f"{money_count} {key} bill,"
    print(result_string_to_be_added)

optimal_change(25.395, 100)