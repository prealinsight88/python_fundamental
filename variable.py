# Variable 'x' stores the integer value 10
x = 10

# Variable 'name' stores the string "christ"
name = "christ"  

print(x)
print(name)

"""
Agar program berjalan tanpa error, penamaan variabel harus mengikuti aturan berikut:
    1. variabel hanya boleh berisi huruf, angka, dan garis bawah (_).
    2. Nama variabel tidak boleh diawali angka.
    3. Nama variabel bersifat case-sensitive.
    4. Hindari memakai keyword Python sebagai nama variabel.
""" 
age = 21
_name = "Chris"
total_score = 90

#Assigning Values to Variables Basic Assignment
x = 5
y = 3.14
z = "Hi"

"""
Python menggunakan dynamic typing, artinya satu variabel yang sama
bisa menyimpan nilai dengan tipe data berbeda selama program berjalan.
Berbeda dengan bahasa pemrograman lain seperti Java atau C, di mana tipe 
data harus ditentukan sejak awal dan tidak bisa berubah, Python secara otomatis 
mengenali tipe data dari nilai yang diberikan ke variabel.
"""

data = 10
print(data, type(data))   # Output: 10 <class 'int'>

data = "Sepuluh"
print(data, type(data))   # Output: Sepuluh <class 'str'>

data = 3.14
print(data, type(data))   # Output: 3.14 <class 'float'>
"""
Type casting adalah proses mengubah tipe data suatu nilai menjadi tipe data lain.
Python menyediakan fungsi bawaan (built-in functions) untuk melakukan konversi ini.

Fungsi Casting Dasar di Python
int() → Mengubah nilai yang cocok menjadi bilangan bulat (integer).
Contoh :
"""
x = int(3.7)       # Hasil: 3
y = int("10")      # Hasil: 10

"""
float() → Mengubah nilai menjadi bilangan desimal (floating point).
Contoh :
"""
x = float(3)       # Hasil: 3.0
y = float("7.5")   # Hasil: 7.5
"""
str() → Mengubah nilai apa pun menjadi string (teks).
Contoh :
"""

x = str(25)        # Hasil: "25"
y = str(3.14)      # Hasil: "3.14"

# CONTOH LENGKAP 
# Konversi ke integer
angka_desimal = 4.9
angka_bulat = int(angka_desimal)
print(angka_bulat)      # Output: 4

# Konversi ke float
angka_string = "8"
angka_float = float(angka_string)
print(angka_float)      # Output: 8.0

# Konversi ke string
nilai = 100
nilai_str = str(nilai)
print(nilai_str)        # Output: "100"
print(type(nilai_str))  # Output: <class 'str'>