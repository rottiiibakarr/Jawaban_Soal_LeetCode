def containsDuplicate(nums):
    last_appear = {}

    i = 0 
    
    while i < len(nums) - 1:
        j = i + 1 
        
        while j < len(nums):
            if nums[j] == nums[i]:
                # Buat 'key' ke dictionary jika belum ada
                if nums[i] not in last_appear:
                    # Dihitung 1 untuk kemunculan pertama (nums[i])
                    last_appear[nums[i]] = 1 
                
                # Setelah key ada, baru tambah 1 untuk duplikatnya (nums[j])
                last_appear[nums[i]] += 1 
                
            # Agar j selalu bertambah maju apapun kondisinya
            j += 1 
            
        # i harus selalu bertambah agar perulangan luar berjalan
        i += 1 
    
    # Mengecek apakah value dalam dictionary itu mempunyai nilai duplikat, berdasarkan key nya
    for key, value in last_appear.items():
        if value >= 2: # Setidaknya muncul 2 kali dalam array 
            return True
            
    # Jika program sampai ke baris ini, berarti tidak ada satupun duplikat yang ditemukan.
    return False

"""
Note:
Untuk kode program tersebut sebenarnya bisa dijalankan pada Leetcode, 
tetapi untuk kompleksitas waktunya itu lebih dari 30ms (maybe), jadi
dari Leetcode nya itu sendiri gak bisa, ada batas ambang nya sepertinya. 
"""
example = [1,2,3,4]
print(containsDuplicate(example)) 