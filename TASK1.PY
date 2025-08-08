def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Optional: ignore case and spaces
    if s == s[::-1]:
        print(True)
    else:
        print(False)
is_palindrome("A man a plan a canal Panama")
is_palindrome("hello") 