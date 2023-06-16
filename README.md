# OpenBrute

A Python module to perform brute force attacks on MD5 hashes

## Installation

Clone the GitHub repository to your local machine:

``` console
git clone https://github.com/ArloMichael/OpenBrute.git
```

## Usage

The `attack` function takes three arguments:

1.  `target_hash` - the target MD5 hash that needs to be cracked.
2.  `char_set` - a string of characters to be used in the password generation.
3.  `max_length` - the maximum length of the generated passwords.

Here's an example usage:

``` python
import string
from openbrute import attack

# Target MD5 hash
target_hash = 'd077f244def8a70e5ea758bd8352fcd8'

# Character set to be used for password generation
char_set = string.ascii_letters

# Maximum password length
max_length = 5

# Brute force the hash
password = attack(target_hash, char_set, max_length)

# Print the password
print(password)
```

This will output:

``` python
'cat'
```
