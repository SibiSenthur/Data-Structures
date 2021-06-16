class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack=[]
        result_set = [0]*len(T)
        for x in range(len(T)-1,-1,-1):
            while(stack and stack[-1][0]<=T[x]):
                stack.pop()
            if stack:
                result_set[x]=stack[-1][1]-x
            stack.append((T[x],x))
        return result_set
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
        