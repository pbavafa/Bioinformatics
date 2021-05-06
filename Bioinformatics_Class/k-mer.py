# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    # print("freq",freq)
    # print("freq.values()",freq.values())
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
        # add each key to words whose corresponding frequency value is equal to m
    return words

# Copy your FrequencyMap() function here.
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        if Pattern in freq:
            freq[Pattern] += 1
        else:
            freq[Pattern] = 1
    return freq

