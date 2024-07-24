#UserInput for data input and validation by yournamehere

class UserInput:
    @staticmethod
    def getValue(prompt,dtype,floor = None,ceiling = None):
        goodval = False
        while not goodval:
            try:
                if dtype.lower() == "f":
                    v = float(input(prompt))
                else:
                    v = int(input(prompt))
                if floor != None and v < floor:
                    print("Your value of " + str(v) + " is below the floor of " + str(floor))
                    goodval = False
                elif ceiling != None and v > ceiling:
                    print("Your value of " + str(v) + " is above the ceiling of " + str(ceiling))
                    goodval = False
                else:
                    goodval = True
            except ValueError as ex:
                if dtype.lower() == "f":
                    print("Illegal input, not a float: " + str(ex))
                else:
                    print("Illegal input, not an integer: " + str(ex))
                goodval = False
        return v
    @staticmethod
    def getChoice(prompt: str, abbrev: bool):
        goodval = False
        while not goodval:
            v = input(prompt)
            if abbrev:
                v = v.upper()
                if len(v) == 3:
                    goodval = True
                else:
                    print("Abbreviation must be 3 characters.")
            else:
                goodval = True
        return v

