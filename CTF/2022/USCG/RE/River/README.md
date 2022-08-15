# River

Author: Rajat

## Description

I love rafting!

## Solution

When run the program will create 5 child processes. Each process interacts with the data essentially creating a pipe which the data will travel through. 

Threads:

1. Read in data
2. XOR each byte of input by 0x56
3. XOR each byte of input with the previous byte of input
4. XOR the input with a fixed key array
5. Compare resulting data to fixed array containing the flag

By following this order in reverse it is possible to recover the flag.

Flag: tH3_gr34t_R1v3r_3bb5_4nD_fL0w5_8a3c41eb

```python
flag = [None] * 0x27
flag[0] = 0x99;
flag[1] = 0x69;
flag[2] = 0x3b;
flag[3] = 0xfc;
flag[4] = 0x9d;
flag[5] = 0x1a;
flag[6] = 0xa0;
flag[7] = 0x19;
flag[8] = 0xd3;
flag[9] = 0xa9;
flag[10] = 0x87;
flag[11] = 0xdd;
flag[12] = 0x82;
flag[13] = 0xca;
flag[14] = 0x61;
flag[15] = 0x38;
flag[16] = 0xff;
flag[17] = 0x55;
flag[18] = 0x5e;
flag[19] = 0xce;
flag[20] = 0xaf;
flag[21] = 0x9c;
flag[22] = 0xa6;
flag[23] = 0xd;
flag[24] = 0xd3;
flag[25] = 100;
flag[26] = 0x9a;
flag[27] = 0xea;
flag[28] = 0x27;
flag[29] = 0x86;
flag[30] = 0x6f;
flag[31] = 0x7f;
flag[32] = 1;
flag[33] = 0xe0;
flag[34] = 0xad;
flag[35] = 0x48;
flag[36] = 0xdd;
flag[37] = 0x61;
flag[38] = 0x9a;

keys = [None] * 0x27
keys[0] = 0xbb;
keys[1] = 0x55;
keys[2] = 0x62;
keys[3] = 0xac;
keys[4] = 0xfc;
keys[5] = 0x5f;
keys[6] = 0x80;
keys[7] = 0x5b;
keys[8] = 0xb3;
keys[9] = 0xc0;
keys[10] = 0xea;
keys[11] = 0xd7;
keys[12] = 0xa8;
keys[13] = 0x85;
keys[14] = 10;
keys[15] = 0x5a;
keys[16] = 0xf8;
keys[17] = 0x66;
keys[18] = 0x59;
keys[19] = 0xaa;
keys[20] = 0xc2;
keys[21] = 0x93;
keys[22] = 0x91;
keys[23] = 0x28;
keys[24] = 0xff;
keys[25] = 0x78;
keys[26] = 0x9c;
keys[27] = 0x8a;
keys[28] = 0x66;
keys[29] = 0xa4;
keys[30] = 0x44;
keys[31] = 0x3a;
keys[32] = 0x73;
keys[33] = 0xf7;
keys[34] = 0x8f;
keys[35] = 8;
keys[36] = 0xfa;
keys[37] = 0x75;
keys[38] = 0xba;

for i in range(39):
    flag[i] = flag[i] ^ keys[i]

for i in range(1, 39):
    flag[-i] = flag[-i] ^ flag[-i - 1]

for i in range(39):
    flag[i] = flag[i] ^ 0x56
    print(chr(flag[i]), end='')

print()
```

