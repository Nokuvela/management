#Task 2: Comprehensions (lists and sets).
#The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:
codes =[14,15,16,17,18,19,20]
#§ Create a normal and comprehensive list that will display the codes.
normal_code=[code for code in codes]
print("normal_code:",normal_code)
#§ Create a normal and comprehensive list that will add the codes together for auditing purpose.
total=sum([code for code in codes])
print("The total code is:",total)

#§ Create a normal and comprehensive list that will display only codes that are tracked by odd
#numbers.

odd =[code for code in codes if code %2 !=0]
print("the odd number of codes:",odd)
#§ Create a set to display the list of codes.
set =set(codes)
print("The set code :",set)