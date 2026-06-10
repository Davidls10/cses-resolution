dna_string = input()
greater_len = 1
current_len = 1
seq_start_char = dna_string[0]
 
for i in range(1, len(dna_string)):
    if dna_string[i] == seq_start_char:
        current_len += 1
    else:
        if current_len > greater_len:
            greater_len = current_len
        current_len = 1
        seq_start_char = dna_string[i]
        
if current_len > greater_len:
    greater_len = current_len
    
print(greater_len)