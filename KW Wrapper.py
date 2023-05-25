#!/usr/bin/env python
# coding: utf-8

# In[13]:


def concatenate_keywords(keywords):
    n = len(keywords)
    results = []
    for i in range(n):
        for j in range(i, n):
            keyword = " ".join(keywords[i:j+1])
            if keyword not in results:
                results.append(keyword)
    return results

def format_keyword(keyword):
    return '"' + keyword + '"' # add quotes around keyword for phrase match

def format_exact_match(keyword):
    return '[' + keyword + ']' # add square brackets for exact match

input_str = input("Enter a list of keywords separated by commas: ")
keywords = [kw.strip() for kw in input_str.split(",")]
output = concatenate_keywords(keywords)

phrase_match_output = [format_keyword(kw) for kw in output] # phrase match version
exact_match_output = [format_exact_match(kw) for kw in output] # exact match version

print("Phrase match output:")
print("\n".join(phrase_match_output))

print("\nExact match output:")
print("\n".join(exact_match_output))


# In[ ]:




