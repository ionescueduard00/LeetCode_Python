class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=""
        rest=0
        nr=0
        n=max(len(a),len(b))
        a=a.zfill(n)
        b=b.zfill(n)
        
        for i in range (len(a)-1,-1,-1):
            if i<len(b):
                nr=int(a[i])+int(b[i])+rest
                rest=nr//2
                result=str(nr%2)+result
            if i>=len(b):
                nr=int(a[i])+rest
                rest=nr//2
                result=str(nr%2)+result
        
        if rest==1:
            result="1"+result
        return result

            
               
        