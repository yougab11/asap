from app import validate_data

#test validate;
# really know idea what to test exactly but going by this it should call the function a few time and return pass or fail
data = {"first_name": "Jose", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "MX"}
data1 = {"first_name": "Joses", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "MX"}
data2 = {"first_name": "Jose", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "ZH"}
data3 = {"first_name": "test", "last_name": "tester", "dob": "01/01/1991", "country": "US"}

#call function multiple times
test1 = validate_data(data)
test2 = validate_data(data1)
test3 = validate_data(data2)
test4  =validate_data(data3)

#print out results
print("Test 1 pass fail " + str(test1 == True))
print("Test 2 pass fail " + str(test2 == False))
print("Test 3 pass fail " + str(test3 == False))
print("Test 4 pass fail " + str(test4 == True))
