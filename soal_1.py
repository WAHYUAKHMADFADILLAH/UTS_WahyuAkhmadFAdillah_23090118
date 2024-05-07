print('start')
a = int(input("masukan bilanga pertama : "))
b = int(input("masukan bilanga kedua : "))
def jumlah(a,b):
    return a+b
def kurang(a,b):
    return a-b
def mod(a,b):
    return a%b
def hasil():
    print("hasil jumlah : ",jumlah(a,b))
    print("hasil kurang : ",kurang(a,b))
    print("hasil modulus : ",mod(a,b))
    print("end")
hasil()