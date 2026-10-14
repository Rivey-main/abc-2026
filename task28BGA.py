def nums_to_letters(text: str) -> str:
    words = text.split()
    result = []
    
    for word in words:
        if word.isdigit():
            num = int(word)
            if num == 0:
                result.append(" ")
            else:
                
                result.append(chr(97 + num - 1))
        else:
            result.append(word)
            
    
    return "".join(result).replace(" , ", ", ").replace(" !", "!")


print(nums_to_letters("8 5 12 12 15")) 


print(nums_to_letters("8 5 12 12 15 , 0 23 15 18 12 4 !")) 

