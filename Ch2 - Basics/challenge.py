def main():
    palBoolean = False
    answer = input("Enter string to test for palindrome: ")
    if answer =="exit":
        return
    else:
        if answer == answer[::-1]:
            palboolean = True
            # return palBoolean
        else:
            palboolean = False
        return palboolean
print( "Palindrome Test: ", main())
