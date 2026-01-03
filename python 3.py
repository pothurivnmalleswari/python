def move_hyphen(s):
    if s is None:
        return None
    hyphens = s.count('-')
    result='-'*hyphens
    for ch in s:
        if ch!='-':
            reult+=ch
        return result

#Test
s = input("enter string:")
print("Original:",s)
print("Modified:",move_hyphen(s))
