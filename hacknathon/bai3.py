def is_Palindrome(a):
    if a[::-1] == a:
         print('This is a palindrome.')
    else :
        print('This is not a palindrome.')
is_Palindrome('anna')
is_Palindrome('annb')

def c2(a):
    if (''.join(list(reversed(a)))) == a:
        print('This is a palindrome.')
    else :
        print('This is not a palindrome.')
c2('anna')