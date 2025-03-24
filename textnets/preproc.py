import jieba
from collections import defaultdict

class ChineseTokenizer:
    def __init__(self):
        self.stopwords = set(["的", "是", "在", "和", "了", "有"])
        jieba.initialize()
    
    def tokenize(self, text):
        words = jieba.cut(text)
        return [w for w in words if w not in self.stopwords and len(w) > 1]

def chinese_phraser(docs, min_count=5, threshold=10):
    tokenizer = ChineseTokenizer()
    phrases = defaultdict(int)
    
    for doc in docs:
        tokens = tokenizer.tokenize(doc)
        for i in range(len(tokens)-1):
            bigram = f"{tokens[i]}{tokens[i+1]}"
            phrases[bigram] += 1
    
    return [phrase for phrase, count in phrases.items() 
            if count >= min_count and len(phrase) > 1]
