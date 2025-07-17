# My solution
my_str= ' roman'
print(my_str.lower().strip()[::-1]==my_str.lower().strip())

palindrome_string= '  MaDam  '
print(palindrome_string.strip().lower()[::-1] == palindrome_string.strip().lower())


# Given Solution
s1 = 'Rats live on no evil star'
s1= s1.replace(' ','')
s1 = s1.lower()
print(f'Is \"{s1}\" palindrome? => {s1==s1[::-1]}')

s2 = ' Able was I ere I saw Elba '
s2 = s2.replace(' ','')
s2 = s2.lower()
print(f'Is \"{s2}\" palindrome? => {s2==s2[::-1]}')