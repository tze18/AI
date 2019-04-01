import re
test_string = 'find: I love cats, I love dogs, skip: I love logs, I love cogs'
pattern = 'I love cats|I love dogs'
ans=re.findall(pattern,test_string)
print(ans)