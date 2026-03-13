def removeDuplicateLetters(s) :
  # Untuk mengetahui apakah huruf masih punya "cadangan" di belakang
  last_appear = {} # Output: {'c': 7, 'b': 6, 'a': 2, 'd': 4}, c mempunyai nilai 7 tertimpa di indeks 7 (akhir)
  for i in range(len(s)) :
    last_appear[s[i]] = i # Contoh {'c': 0}, key c mempunyai value yaitu 0 (0 itu dari indeks)
  
  result = [] # List baru sebagai stack/tumpukan
  
  for i in range(len(s)) : 
    current_val = s[i] # Awalan mempunyai nilai current_val = 'c'
    
    # Jika ada huruf di dalam list result, aman, abaikan (continue)!
    if current_val in result :
      continue 
    
    # Perulangan while akan dijalankan kalo semua syarat terpenuhi, jika tidak, akan dilempar ke result.append()
    while len(result) > 0 and current_val < result[-1] and last_appear[result[-1]] > i:
      result.pop() # Hapus huruf yang secara abjad lebih besar tersebut dari ujung list!
    
    """
    [1] Awalan untuk perulangan pertama, karena tidak ada huruf di dalam list result, maka ia menambahkan current_val 
    ke dalam list result.

    [2] Untuk perulangan selanjutnya, setelah perulangan while selesai menyingkirkan huruf yang lebih besar (jika ada),
    maka masukkan huruf saat ini ke ujung list.
    """
    result.append(current_val)
  
  return "".join(result)
    
example = "cbacdcbc" 
print(removeDuplicateLetters(example))
  