# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

def myAtoi(self, str: str) -> int:
    intMax = 2**31-1
    intMin = -2**31
    data = str.strip();
    numbers = "0123456789-+"
    number = "0123456789"
    minPlus = "-+"
    
    sub = 0
    
    if len(data)>0:
        if data[0] not in numbers:
            return sub
    else:
        return sub

    if data[0] in minPlus and len(data) == 1:
            return sub
    
    if data[0] in minPlus and len(data) > 1 and data[1] not in number:
        return sub        

    
    for i in range(1,len(data)-1):
        if data[i] not in number:
            data = data[0:i]
            break
    
    if data[len(data)-1] not in number:
        data = data[0:-1]
    sub = int(data)
    
    return min(intMax, max(intMin, sub))