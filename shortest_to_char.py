class Sol:
    def shortest_to_char(self, s,c):
        idx=[index for index, value in enumerate(s) if value == c]
        l=[]
        for i in range(len(s)):
            min=len(s)-1
            for j in idx:
                ans=abs(i-j)
                if ans<min:
                    min=ans
            l.append(min)
        return l
if __name__ == '__main__':
    p = Sol()
    print(p.shortest_to_char(s = "aaab", c = "b"))
