

import re

randStr="cat cat's"

print(re.findall('[cat]+["s]*',randStr))

# randStr="doctor octors doctor's"
#
# print(re.findall("[doctor]+['s]*",randStr))