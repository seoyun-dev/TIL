def alignRight(x0, x1, val):
 print "%3d ~ %3d : %10g" % (x0, x1, val)
 
def alignLeft(x0, x1, val):
 print "%-3d ~ %-3d : %-10g" % (x0, x1, val)

alignLeft(123, 456, 789.012)
alignLeft(12, 34, 56.789)
alignLeft(1, 234, 5.6789)

print ""
print "---------------------------"
print ""

alignRight(123, 456, 789.012)
alignRight(12, 34, 56.789)
alignRight(1, 234, 5.6789)
