import numpy as np

def localTrace(i,j,s1,s2,seq1,seq2,dp,score,match,mis,gap,maxi):
    if(dp[i][j]==0 and score==maxi):
        print(s2[::-1])
        print(s1[::-1])
        print()
        return
    elif(dp[i][j]==0):
        return
    if(i-1>=0):
        localTrace(i-1,j,s1+seq1[i-1],s2+"-",seq1,seq2,dp,score+gap,match,mis,gap,maxi)

    if(j-1>=0):
        localTrace(i,j-1,s1+"-",s2+seq2[j-1],seq1,seq2,dp,score+gap,match,mis,gap,maxi)
        
    if(i-1>=0 and j-1>=0):
        d=match
        if(seq1[i-1]!=seq2[j-1]):
            d=mis
        localTrace(i-1,j-1,s1+seq1[i-1],s2+seq2[j-1],seq1,seq2,dp,score+d,match,mis,gap,maxi)

def localAlignment(s1,s2,match,mis,gap):
    n=len(s1)
    m=len(s2)
    dp=np.zeros((n+1, m+1),dtype=int)

    #traversing with transition conditions
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(s1[i-1]==s2[j-1]):
                dp[i,j]=match+dp[i-1,j-1]
            else:
                dp[i,j]=max(0,mis+dp[i-1,j-1],gap+dp[i-1,j],gap+dp[i,j-1])

    #printing the matrix
    maxi=0
    for i in range(n+1):
        for j in range(m+1):
            maxi=max(maxi,dp[i,j])
            print(dp[i,j],end=" ")
        print()
    
    for i in range(n+1):
        for j in range(m+1):
            if(dp[i][j]==maxi):
                align1=""
                align2=""
                localTrace(i,j,align1,align2,s1,s2,dp,0,match,mis,gap,maxi)
    
    #returning the alignment score
    return maxi


a=input("Enter Sequence 1:")
b=input("Enter Sequence 2:")
match=int(input("Enter Match Score:"))
mis=int(input("Enter Mismatch Penalty:"))
gap=int(input("Enter Gap Penalty:"))

print("Local Alignment Score:",localAlignment(a,b,match,mis,gap))
