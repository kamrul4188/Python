# As conditional logic,We are going to use if statement

saarc = ["Bangladesh", "Afghanistan",  "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]

country = input ("Enter the name of the country: ")

if country in  saarc:
    print country,"is a member of SAARC"
else:
    print country, "is not member of SAARC"

print "Program Terminated...."
