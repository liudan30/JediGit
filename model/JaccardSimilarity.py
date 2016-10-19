from sets import Set

def JaccardSimilarity(preference1, preference2): 
	s = Set(preference1)
	t = Set(preference2)
	unionSet = s.union(t)
	intersectionSet = s.intersection(t)
	return float(len(intersectionSet))/float(len(unionSet))

if __name__ == "__main__":
	print JaccardSimilarity([1,2,3], [2,3,4])
		
