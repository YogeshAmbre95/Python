#################################################
#  01.07.2022
#################################################
# TOPICS TO BE COVERED
# 👉 BUILT-IN DATA TYPE OF PYTHON: STRINGS
# 👉 SLICING
# 👉 BUILT-IN METHODS THAT YOU CAN USE ON STRINGS.
# 👉 .foramt and f-string for printing
#################################################

#################################################
#  STRINGS
#################################################

# what is a string
# ''
# ""
# # '''

# string1 = 'Hello World'
# print(type(string1))

# '''

# INDEX POSITION 	0	1	2	3	4	5	6	7	8	9	10
# CHARACTER	    H	e	l	l	o		W	o	r	l	d

# '''

# print(string1)

# # Accessing each character in string

# print(string1[0])
# print(string1[1])
# print(string1[2])
# print(string1[3])
# print(string1[4])

# # SLICING IN STRING
# print('*******SLICING IN STRING**********')
# # print(string1[start : End(not include)]) syntax , always n-1 is the END

# '''

# INDEX POSITION 	0	1	2	3	4	5	6	7	8	9	10
# CHARACTER	    H	e	l	l	o		W	o	r	l	d

# '''

# print(string1[1:])
# print(string1[:])
# print(string1[1:4])
# print(string1[:11])

# print('*************HOMEWORK*********************')

# string2 = 'I LOVE PYTHON'

# '''
# INDEX POSITION  	0	1	2	3	4	5	6	7	8	9	10	11	12  13

# CHARACTER	        I	    L   O	V	E		P	Y	T	H	O	 N

# '''
# # USE SLICING TO GET THE BELOW OUTPUTS

# # "I"

# # "LOVE"

# # "PYTHON"

# # "VE PY"

# # "I LO"

# # "HON"

# # "I LOVE PYTHON"

# print(string2)

# print(string2[0:1])

# print(string2[2:6])

# print(string2[7:13])

# print(string2[4:9])

# print(string2[0:4])

# print(string2[10:13])

# print(string2[0:13])


# str = input('enter your name')
# print(str)

print("The sum of"{a} "and" {b} "is" {c=a+b}.format(a=100, b=200, c=a+b))
