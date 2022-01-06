def isPalindrome(str):
    if newStr == newStr[::-1]:
        return True
    return False


while(True):
    inStr = input(
        "Enter string to test for palindrome or 'exit': ").lower()
    if inStr == "exit":
        break
    newStr = ""
    for ch in inStr:
        if ch.isalnum():
            newStr += ch
    print("Palindrome test:", isPalindrome(newStr))
