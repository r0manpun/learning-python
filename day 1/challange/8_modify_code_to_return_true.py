a = 0.1
b = 0.3
print(a* 3 ==b) # => False

# Solution
import  math
print(math.isclose(a * 3, b)) # => True