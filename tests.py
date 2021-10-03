from app import validate

#test validate;
# really know idea what to test exactly but going by this it should call the function a few time and return pass or fail
data = {"first_name": "Jose", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "MX"}
data1 = {"first_name": "Jose", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "MX"}
data2 = {"first_name": "Jose", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "MX"}
data3 = {"first_name": "Jose", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "MX"}

#call function multiple times
test1 = validate(data)
test2 = validate(data1)
test3 = validate(data2)
test4  =validate(data3)

#print out results
print("Test 1 pass fail " + test1 == True)
print("Test 2 pass fail " + test2 == True)
print("Test 3 pass fail " + test3 == False)
print("Test 4 pass fail " + test4 == True)
