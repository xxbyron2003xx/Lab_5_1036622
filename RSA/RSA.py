def exponenciacion_binaria(base, exponente):
    if exponente == 0:
        return 1
    elif exponente % 2 == 0:
        mitad = exponenciacion_binaria(base, exponente // 2)
        return mitad * mitad
    else:
        mitad = exponenciacion_binaria(base, (exponente - 1) // 2)
        return base * mitad * mitad
        
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
    
class RSA:
    def __init__(self,p,q):
        self.p = p
        self.q = q
        self.n = p*q
        self.omega = (p-1)*(q-1)
        _mcd = 2
        _e = 2
        while _mcd != 1 or _e%2!=0:
            _mcd = mcd(self.omega, _e)
            _e = _e + 1
        self.e = _e - 1

        mod = 0
        j = 0
        while mod != 1:
            j = j+1
            mod = (self.e * j) % self.omega
        
        self.j = j
        
    def crypt(self, msg):
        crypt_arr = []
        for ch in msg:
            ch_int = ord(ch)
            cyph_int = exponenciacion_binaria(ch_int,self.e)
            crypt_arr.append(cyph_int%self.n)
        return crypt_arr
        
    def decrypt(self,crypt_rsa):
        msg = ""
        for val_int in crypt_rsa:
            val_exp = exponenciacion_binaria(val_int,self.j)
            val_exp = val_exp%self.n
            msg += chr(val_exp)
        return msg