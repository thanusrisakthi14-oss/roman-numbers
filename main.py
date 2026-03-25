class Roman:
    def __init__(self, num):
        self.num = num
        
    def convert(self):
        if self.num == 1:
            return "I"
        elif self.num == 2:
            return "II"
        elif self.num == 3:
            return "III"
        elif self.num == 4:
            return "IV"
        elif self.num == 5:
            return "V"
        else:
            return "Number too big"


n = int(input("Enter number: "))
obj = Roman(n)
print(obj.convert())