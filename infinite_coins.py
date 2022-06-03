class Set:
    def __init__(self):
        self.set = []
    """
    The function below will:
        -receive the input
        -compute the quotient of the inputed value by 25
        -iterate through these values doing
            -compute the quotient of the diference of the inputed value by 10
            -iterate the same way with those values taking 5 instead of 10 
                -iterate through those last values
                    -appending to 'set' a list containing the current value of each iteration with the remainder
        -print 'set'
    """
    def makeChange(self, n):
        quo25 = n // 25
        for i in range(quo25 + 1):
            quo10 = (n - i * 25) // 10
            for j in range(quo10 + 1):
                quo5 = (n - i * 25 - j * 10) // 5
                for k in range(quo5 + 1):
                    l = (n - i * 25 - j * 10 - k * 5)
                    self.set.append([i, j, k, l])
        print(self.set)


s = Set()
n = int(input("Please enter a number:"))
print(s.makeChange(n))