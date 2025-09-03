"""
Dalam pemrograman Python, Operator umumnya digunakan untuk melakukan 
operasi pada nilai dan variabel. Operator adalah simbol standar yang 
digunakan untuk operasi logika dan aritmatika. Dalam artikel ini, 
kita akan membahas berbagai jenis operator Python.
"""
# Operator Aritmatika
# Variables
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)

# Operator Perbandingan
"""
Dalam Python, operator Perbandingan Relasional membandingkan nilai. 
Operator ini menghasilkan nilai Benar atau Salah sesuai kondisi.

CONTOH :
"""

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Operator Logika
a = True
b = False
print(a and b)
print(a or b)
print(not a)

# Operator Bitwise
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

# Operator Assignment 
"""
Operator Penugasan Python digunakan untuk menetapkan nilai ke variabel. 
Operator ini digunakan untuk menetapkan nilai di sisi kanan ekspresi ke 
operan di sisi kiri.
"""
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

# Operator Ternary
"""
Dalam Python, operator ternary, juga dikenal sebagai ekspresi kondisional, adalah operator yang mengevaluasi 
sesuatu berdasarkan kondisi yang benar atau salah. Operator ini ditambahkan ke Python pada versi 2.5.
"""

a, b = 10, 20
min = a if a < b else b

print(min)