words = "aabbccddd"
def count(word):
    out = {}

    for i in word:
        if i in out:
            out[i] +=1
        else:
            out[i] = 1

    return out       
print(count("aabbccddd"))

# out = {a:2 , b:2 ,c:2 , d:3}

