class Solution:
    def reportSpam(self, message, bannedWords) :
                        
                        
                        c = 0 
                        m = {}
                        b = {}
                        for i in message:
                            if i not in m :
                                m[i] =0 
                            else:
                                m[i]+=1
                                
                                
                        for i in bannedWords:
                            if i not in m :
                                m[i] =0 
                            else:
                                m[i]+=1
                                
                                
                        for i ,j in m.items():
                            if j == 1 :
                                c+=1
                                
                                
                        if c==2 :
                            return True
                        return False

            
            
message = ["hello","world","leetcode"] 
bannedWords = ["world","hello"]

a = Solution()
a.reportSpam(bannedWords, message)
a.reportSpam(["hello","programming","fun"],["world","programming","leetcode"])