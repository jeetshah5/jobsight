import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Use custom nltk data path
nltk.data.path.append("/Users/shrigems/nltk_data")

# Load job data
df = pd.read_csv("data/jobs.csv")
text = " ".join(df["title"].dropna()).lower()

# Tokenize using regex instead of nltk.word_tokenize()
tokens = re.findall(r'\b[a-z]+\b', text)  # Extract only alphabetic words
tokens = [word for word in tokens if word not in stopwords.words("english")]

# Count top keywords
keyword_counts = Counter(tokens)
top_keywords = keyword_counts.most_common(15)

# Output
print("\n📊 Top Keywords in Job Titles:\n")
for word, count in top_keywords:
    print(f"{word}: {count}")

# Save
pd.DataFrame(top_keywords, columns=["keyword", "count"]).to_csv("data/keywords.csv", index=False)
print("\n✅ Saved top keywords to data/keywords.csv")
