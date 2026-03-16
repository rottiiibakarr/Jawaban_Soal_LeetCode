def containsDuplicate(nums) :
    # Buat penampung berupa set, untuk mengidentifikasi apakah terdapat duplikat 
    watching = set() 

    for num in nums :
        # Jika num ada didalam penampung, pasti duplikat!
        if num in watching :
            return True # Jika ada duplikat, return True
        
        watching.add(num) # Jika belum ada, masukkan num kedalam variabel set 'watching'
    
    return False # Jika tidak ada duplikat, return False

example = [1,1,1,3,3,4,3,2,4,2] # Beberapa element terdapat duplikat 
print(containsDuplicate(example)) # Output: True