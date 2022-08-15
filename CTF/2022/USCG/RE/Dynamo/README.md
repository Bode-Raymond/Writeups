# Dynamo

Author: Rajat

## Description

I've been staring at this code for hours, but I just can't figure out what it's doing...

## Solution

ltrace:
```bash
strcmp("password", "d3bU9g3Rs_4r3_c00L_8da39b72")        = 12
puts("Wrong!!")                                          = 8
```

gdb:
```
b *main+88
r lmao
strcmp@plt (
    $rdi = 0x007fffffffe739 → 0x454853006f616d6c ("lmao"?),
    $rsi = 0x007fffffffe210 → "d3bU9g3Rs_4r3_c00L_8da39b72",
    $rdx = 0x007fffffffe210 → "d3bU9g3Rs_4r3_c00L_8da39b72",
    $rcx = 0x0000000000005c
)
```

