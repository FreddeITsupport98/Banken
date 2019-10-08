with open('text.txt', 'r') as f:
    
    size_to_read = -1 # tilldelar med 100 karakter inom int värde
    
    f_content = f.read(size_to_read) # file read med variabel f_content
    
    while  len(f_content) > 0: # medans längden är av f_content är mindre än 0 ska det stoppas
        print(f_content, end='')
        #f_content = f.read(size_to_read)
   