# Trust

Author: Rajat

## Description

Do you trust me?

## Solution

The binary uses a custom strcmp function to compare each byte of input to the flag. The difference between this and the last challenge is the input is xored with a key and compared to the encrypted flag.

Both the encrypted flag and the key can be found in Ghidra. The flag is located in the `strcmp` function call, while the key is found in a byte array in strcmp.

```
Enc Flag: 0ar89WxG5KRwQHlsXjmUAlbXTc4d0rToF
Key: [0x44,0x33,7,0xd,0x6d,8,0x16,0x77,0x41,3,99,0x19,0x36,0x17,0x58,0x1d,0x1c,0x35,3,0x65,0x1e,0x23,0xc,0x6b,0xb,0x51,0,5,7,0x17,0x65,0x5c,0x20]
```

Using interactive python is a quick and easy way to decrypt the flag.

```python
>>> key = [0x44,0x33,7,0xd,0x6d,8,0x16,0x77,0x41,3,99,0x19,0x36,0x17,0x58,0x1d,0x1c,0x35,3,0x65,0x1e,0x23,0xc,0x6b,0xb,0x51,0,5,7,0x17,0x65,0x5c,0x20]
>>> flag = '0ar89WxG5KRwQHlsXjmUAlbXTc4d0rToF'
>>> for i in range(len(flag)):
...     print(chr(key[i] ^ ord(flag[i])), end='')
...
tRu5T_n0tH1ng_4nD_n0_On3_24a7e13f
```

