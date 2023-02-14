def fourthrootN(x,debug=False,specialCases=True):
	from numpy import nan
	if specialCases:
		if x==0:
			return 0.
		elif x<0:
			return nan
	assert x>0.
	s=1.
	kmax=100
	tol=1.0e-14
	for k in range(kmax):
		if debug:
			print("At iteration number %s, s= %20.15f" %(k,s))
			s0=s
			s=0.25*(3*s+x/(s**3))
			delta_s=s-s0
		if(abs(delta_s/x))<tol:
			break
	if debug:
		print("After %s iterations,  s=%20.15f" %(k+1,s))
	return s

	
	
