import zlib

def kolmogorov_complexity(s):
    return len(zlib.compress(s.encode('utf-8')))

# Test the function
s = "This is a test string"
print(kolmogorov_complexity(s))
