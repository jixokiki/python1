class MyCompleksNumber:
    #Metodenya
    def __init__(self, real = 0, imag = 0):
        print("MyCompleksNumber constructor executing...")
        self.real_part = real
        self.imag_part = imag
    
    def displayCompleks(self):
        print("{0} + {1}j".format(self.real_part,self.imag_part))

# Membuat Object baru yang memakai metode class MyCompleksNumber
antrian1 = MyCompleksNumber(50,100)

#Calling displayCompleks() function
#menghasilkan Output 50 + 100j
antrian1.displayCompleks()

# Membuat objek baru yang lain tetapi masih memakai metode class MyCompleksNumber
antrian2 = MyCompleksNumber(100,200)
antrian2.atributBaru = 80
antrian2.displayCompleks()

#Output : (100,200,80)
print((antrian2.real_part, antrian2.imag_part, antrian2.atributBaru))

#klo langsung print antrian1 itu tidak akan bisa dan menghasilkan <__main__.MyCompleksNumber object at 0x1025cd4d0>, 
#karena antrian1 hanya variable atau tumbal untuk menyatakan class dari MyCompleksNumber
# print(antrian1) outuputnya : <__main__.MyCompleksNumber object at 0x1025cd4d0> 
print(antrian1.real_part, antrian1.imag_part) #output yang berhasil atau yang bisa dilakukan menggunakan print

#Delete Object atau menghapus variable calss atau atribut
del antrian1.real_part
#print(antrian1.real_part) #output : traceback yang menyatakan antrian1.real_part sudah tidak ada dimodul atau atribut, dan memberitahu yang ada hanya antrian1.imag_part
print(antrian1.imag_part)

#bila mendelete semua object 
del antrian1
print(antrian1.real_part,antrian1.imag_part) #output : antrian1 not define karena sudah not defined atau sudah hilang mau itu antrian1.real_part maupun antrian1.imag_part
