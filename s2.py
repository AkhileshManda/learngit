s= input()
s=s.lower()
s1= s.split(" ")
sw=0
p=0
l= len(s1)
stp=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
lstp= len(stp)
prep=['above','across','after','at','around','before','behind','below','beside','between','by','down','during','for','from','in','inside','onto','of','off','on','out','through','to','under','up','with']
lprep=len(prep)


for i in range(l):
    for j in range(lstp):
        if(s1[i]==stp[j]):
            print(s1[1])
            sw=sw+1
            
    for k in range(lprep):
        if(s1[i]==prep[k]):
            print(s1[i])
            p=p+1

    


print("Number of stop words:",sw)
print("Number of prepositions:",p)
        
    
