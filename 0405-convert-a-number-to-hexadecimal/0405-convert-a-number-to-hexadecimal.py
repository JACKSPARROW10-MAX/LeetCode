class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        a=num & 0xffffffff
        hex_str="0123456789abcdef"
        hex_code=""
        while a>0:
            rem=a%16
            hex_code=hex_str[rem]+hex_code
            a=a//16
        
        return hex_code