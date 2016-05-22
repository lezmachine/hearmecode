# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.


from random import randint


bread = (randint(2, 100))
peanut_butter = (randint(1, 100))
jelly = (randint(1, 100))

print "Starting with {0} slices of bread, {1} servings of PB, and {2} servings of jelly.\n".format(bread, peanut_butter, jelly)


count = 0

while bread >= 2 and jelly >0 and peanut_butter>0:
	bread = bread - 2
	peanut_butter = peanut_butter - 1
	jelly = jelly - 1
	
	count = count + 1
	
	print "...Making sandwich... #", count
	print "I now have enough BREAD left for {0}, PB for {1}, and JELLY for {2} sandwiches.\n".format(bread/2, peanut_butter, jelly)

	if bread <= 1:
		print "YOU RAN OUT OF BREAD.\n"
	elif peanut_butter < 1:
		print "YOU RAN OUT OF PB.\n"
	elif jelly < 1:
		print "YOU RAN OUT OF JELLY.\n"

print """***SANDWICH MISSION COMPLETE!***\nYOU MADE {0} DAMNED SANDWICHES.\nThe word "sandwich" starts to look weird after a while.""".format(count)
