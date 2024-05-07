def pbmi():
    bb = float(input('Masukkan berat badan anda (kg): '))
    tb = float(input('Masukkan tinggi badan anda (cm): '))
    
    bmi = bb / (tb ** 2)  # Perhitungan BMI yang benar
    
    print('Nilai BMI anda:', bmi)  # Menampilkan nilai BMI
    
    if bmi < 18.5:
        print('Berat badan anda kurang')
    elif bmi <= 24.9:
        print('Berat badan anda normal')        
    elif bmi <= 29.9:
        print('Berat badan anda kelebihan')
    else:
        print('Anda Obesitas')

pbmi()
