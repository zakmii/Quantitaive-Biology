import numpy as np

def traceback(i,j,s1,s2,seq1,seq2,dp,score,match,mis,gap):
    n=len(seq1)
    m=len(seq2)
    if(i==0 and j==0):
        if(score==dp[n,m]):
            print(s2[::-1])
            print(s1[::-1])
            print()
        return
    
    if(i-1>=0):
        traceback(i-1,j,s1+seq1[i-1],s2+"-",seq1,seq2,dp,score+gap,match,mis,gap)

    if(j-1>=0):
        traceback(i,j-1,s1+"-",s2+seq2[j-1],seq1,seq2,dp,score+gap,match,mis,gap)
        
    if(i-1>=0 and j-1>=0):
        d=match
        if(seq1[i-1]!=seq2[j-1]):
            d=mis
        traceback(i-1,j-1,s1+seq1[i-1],s2+seq2[j-1],seq1,seq2,dp,score+d,match,mis,gap)
        
   

def globalAlignment(s1,s2,match,mis,gap):
    n=len(s1)
    m=len(s2)
    dp=np.zeros((n+1, m+1),dtype=int)
    #base case
    for i in range(n+1):
        dp[i,0]=i*gap
    
    for i in range(m+1):
        dp[0,i]=i*gap

    #traversing with transition conditions
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(s1[i-1]==s2[j-1]):
                dp[i,j]=match+dp[i-1,j-1]
            else:
                dp[i,j]=max(mis+dp[i-1,j-1],gap+dp[i-1,j],gap+dp[i,j-1])

    #printing the matrix
    for i in range(n+1):
        for j in range(m+1):
            print(dp[i,j],end=" ")
        print()
    align1=""
    align2=""
    traceback(n,m,align1,align2,s1,s2,dp,0,match,mis,gap)

    #returning the alignment score
    return dp[n,m]   

a=input("Enter Sequence 1:")
b=input("Enter Sequence 2:")
match=int(input("Enter Match Score:"))
mis=int(input("Enter Mismatch Penalty:"))
gap=int(input("Enter Gap Penalty:"))
print("Global Alignment Score:",globalAlignment(a,b,match,mis,gap))