#https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true

def bonAppetit(bill, k, b):
    # Write your code here
    incorrect = sum(bill) // 2
    correct = (sum(bill) - bill[k]) // 2
    if b == correct:
        print("Bon Appetit")
    elif b == incorrect:
        print(incorrect - correct)