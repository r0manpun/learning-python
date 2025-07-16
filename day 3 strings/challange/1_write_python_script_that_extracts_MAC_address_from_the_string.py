
my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# Extracts the MAC address from the string using split method
split_string=my_str.split()
print(split_string[-1]) # Extracts the last element which is the MAC address
n = len(split_string)
print(split_string[n-1])

# Another way to extract the MAC address using slicing
mac = my_str[len(my_str) - 17:]
print(mac)

# Another way to extract the MAC address using slicing
mac = my_str[-1:-18:-1]
mac= mac[::-1] #reverse string
print(mac)
