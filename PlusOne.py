digits = [1,2,3]

def plusOne(digits):
    connectedNumber = "".join(map(str, digits))
    connectedNumber = int(connectedNumber)
    connectedNumber = connectedNumber+1
    connectedNumber = str(connectedNumber)
    connectedNumber = list(connectedNumber)
    return connectedNumber

print(plusOne(digits))
