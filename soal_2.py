def apakah_kabisat():
    tahun = int(input('masukan tahun: '))
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        print(f'Tahun {tahun} adalah Tahun Kabisat')
    else:
        return False
apakah_kabisat()
