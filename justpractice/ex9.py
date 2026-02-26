class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        # code here
        if operator == 1:
            print(a+b)
        elif operator == 2:
            print(b-a)
        elif operator == 3:
            print(a*b)
        else:
            print("Invalid Input")