s = "cs101 is wonderful"

print s.capitalize()
print s.upper()
print s.isalpha()
print s.isdigit()
print s.startswith("cs")
print s.endswith("cs")
print s.find("101")
print s.find("101", 5, 10)

k = "abc"
print k.isalpha()

n = "  123  "
print n.isdigit()
n = n.strip()
print n.isdigit()

print s.replace("101", "209")
print s
print s.split()
print s

m = "apple,orange,pear"
print m.split(",")

l = ["***", "###", "@@@"]
print s.join(l)
print s
print l

