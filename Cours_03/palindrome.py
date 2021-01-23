def palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])


print(palindrome("mon nom"))
print(palindrome("engagelejeuquejelegagne"))
print(palindrome("aletapeepatela"))
print(palindrome("un radar nu"))
print(palindrome("tulastropecrasecesarceportsalut"))
