class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        a = 0
        length = len(target)
        output = []
        for i in range(1, n+1):
            if a < length:
                if target[a] == i:
                    output.append("Push")
                    a+=1
                else:
                    output.append("Push")
                    output.append("Pop")
        return output
        
        