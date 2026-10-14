cipher = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"

for shift in range(26):
    res = "".join(chr(97 + (ord(c) - 97 - shift) % 26) if c.isalpha() else c for c in cipher)
    

    if "that" in res or "be" in res:
        print(f"--- Робот зафиксировал осмысленный текст (сдвиг {shift}) ---")
        print(res)
        break
