def addTwoNumbers(l1, l2) :
    result = [] # Hasil yang akan di return 
    
    # l1 = [2,4,3], l2 = [5,6,4]
    for a, b in zip(l1, l2) : # Anggap awal a(l1) = 2 dan b(l2) = 5
        front_digit = 0
        rear_digit = 0
        
        # amount = (rear_digit > 0) ? a + (b + front_digit) : a + b
        amount = (a + b + front_digit) if front_digit >= 2 else a + b
        """
        Sebelum melakukan penjumlahan, lakukan filter terlebih dahulu, 
        dengan ketentuan sebagai berikut:
        1. Gunakan if untuk menentukan apakah jika front_digit lebih besar
        dari 0, maka akan dilakukan penjumlahan amount = a + b + front_digit
        2. Jika front_digit tidak lebih besar dari 0 (anggap aja masih 0), 
        makan akan dilakukan penjumlahan amount = a + b (front_digit tidak)
        """
        
        reserve_value = str(amount) 
        """
        1. Nilai dari penjumlahan disimpan pada reserve_value
        2. Setelah disipan, lakukan konversi tipe data pada reserve_value
        
        """
        
        if len(reserve_value) >= 2 :
            # Dikonversi dulu ke int, karena sebelumnya itu kan masih str
            front_digit = int(reserve_value[0]) # Mengambil nilai depan
            rear_digit = int(reserve_value[1]) # Mengambil nilai belakang
            result.append(rear_digit)
        else :
            front_digit = 0
            result.append(int(reserve_value))
    
    return result

example1 = [2, 4, 3]
example2 = [5, 6, 4]

print(addTwoNumbers(example1, example2))