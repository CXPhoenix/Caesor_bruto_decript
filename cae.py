class Caesor:
    def __init__(self):
        self._alphaBase = [chr(ord("a")+i) for i in range(26)]
        self._escapes = "{}_-"

    def bruto_cae_decrypt(self, encode):
        for i in range(26):
            re = f"[ROT{i}] "
            for s in encode:
                if s in self._escapes:
                    re += s
                    continue
                strIndex = self._alphaBase.find(s)
                if strIndex != -1:
                    rotStr = self._alphaBase[(strIndex + i)%len(self._alphaBase)]
                else:
                    rotStr = s
                re += rotStr
            print(re)
    
    def setAlphaBase(self, alphaBase):
        self._alphaBase = alphaBase

    def setEscapes(self, escapes):
        self._escapes = escapes
                
