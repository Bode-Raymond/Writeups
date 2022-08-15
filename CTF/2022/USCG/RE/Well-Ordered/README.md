# Well Ordered

Author: rajat

## Description

Have you found yourself getting disorganized? My new program will help you make sure that everything is in order!

## Solution

The binary provided for the challenge contains 2 noteable functions.

1. `before()`
2. `nth_occurrence()`

The `before()` function will determine wether or not the occurence of parameter 1 determined by parameter 2 occurs before the 3rd parameter at the ocurrence specified by the 4th parameter

The `nth_occurrence()` function will determine the index of the charater specified by parameter 1 at the occurence determined by parameter 2.

Using this information it is possible to manually build a map of the occurence of charaters. This information can be followed to determine the flag.

```
m:0 <- 4:0
3:1 <- _:1
5:1 <- 2:0
F:0 <- 3:2
_:3 <- 1:1
3:2 <- _:3
_:0 <- 5:0
y:0 <- 0:0
0:2 <- e:0
R:0 <- _:2
r:0 <- 3:1
c:0 <- 5:1
s:0 <- _:4
k:0 <- 3:0
a:0 <- 8:0
N:0 <- _:5
1:0 <- F:0
_:1 <- y:0
8:0 <- c:0
R:1 <- _:6
1:1 <- s:0
l:0 <- 1:0
3:0 <- _:0
e:0 <- e:1
2:0 <- 0:2
0:1 <- r:1
_:5 <- 0:1
d:0 <- 3:3
_:2 <- l:0
5:0 <- U:0
i:0 <- N:0
_:6 <- a:0
0:0 <- u:0
3:3 <- R:1
4:0 <- k:0
_:4 <- i:0
U:0 <- r:0
r:1 <- d:0
u:0 <- R:0

Flag:       m4k3_5Ur3_y0uR_l1F3_1s_iN_0rd3R_a8c520ee
Occurence:  0000000011000020002310400511031600010201
```

