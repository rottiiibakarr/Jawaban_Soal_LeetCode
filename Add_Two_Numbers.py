def addTwoNumbers(l1, l2):
    result = [] 
    front_digit = 0 # Menetapkan variabel di luar perulangan agar nilai tidak reset
    
    i = 0 # Gunakan indeks manual
    
    # Looping akan terus berjalan selama salah satu list masih memiliki isi
    # l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    while i < len(l1) or i < len(l2):
        # Ambil nilai jika indeks masih dalam batas list, jika sudah habis anggap 0
        a = l1[i] if i < len(l1) else 0
        b = l2[i] if i < len(l2) else 0
        
        amount = a + b + front_digit 
        reserve_value = str(amount) 
        
        if len(reserve_value) >= 2:
            front_digit = int(reserve_value[0]) 
            rear_digit = int(reserve_value[1]) 
            result.append(rear_digit)
        else:
            front_digit = 0                     
            result.append(int(reserve_value))   
        
        i += 1 # Lanjut ke indeks berikutnya
            
    # Jika looping selesai tapi masih ada sisa simpanan di depan
    if front_digit > 0:
        result.append(front_digit)
        
    return result
      
example1 = [9, 9, 9, 9, 9, 9, 9]
example2 = [9, 9, 9, 9]

print(addTwoNumbers(example1, example2))
# Output: [8, 9, 9, 9, 0, 0, 0, 1]