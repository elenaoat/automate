from hashlib import md5

# hexdigests of the words in /etc/dictionaries-common/words
hexdigests = {}
# hashes loaded from the file "words"
known_hashes = []
# uncovered passwords
passwords = []

# hash all words inside /etc/dictionaries-common/words
with open("/etc/dictionaries-common/words", "r") as f:
    word = f.readline().rstrip("\n")
    while word:
        hexdigests[md5(word).hexdigest()] = word
        word = f.readline().rstrip("\n")
# load hashes from the given file
with open("words", "r") as f:
    hashedpassword = f.readline()
    while hashedpassword:
        known_hashes.append(hashedpassword.rstrip("\n"))
        hashedpassword = f.readline()
# find hashes that corresponds to the ones computed from the known dictionary
for h in known_hashes:
    if h in hexdigests.keys():
        passwords.append(hexdigests[h])
# print found passwords
print passwords
