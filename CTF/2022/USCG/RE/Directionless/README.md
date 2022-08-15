# Directionless

Author: Rajat

## Description

I tried to print the flag, but it got a little lost...

## Solution

When executed this program seems to print nothing, but one look at the assembler dump or ghidra shows that `write()` is being called, but all the file descriptiors are different and do not match with the normal file descriptors of 0, 1, or 2.

```c
int main() {
  write(0x14,&DAT_00100934,1);
  write(7,&DAT_00100936,1);
  write(0xc,&DAT_00100938,1);
  write(4,&DAT_0010093a,1);
  write(0x12,&DAT_0010093c,1);
  write(10,&DAT_00100938,1);
  write(0x1d,&DAT_00100934,1);
  write(0x15,&DAT_00100938,1);
  write(9,&DAT_0010093e,1);
  write(0x1c,&DAT_00100940,1);
  write(0xf,&DAT_00100942,1);
  write(0x10,&DAT_00100938,1);
  write(5,&DAT_00100944,1);
  write(0xe,&DAT_0010093c,1);
  write(8,&DAT_00100946,1);
  write(0x19,&DAT_00100948,1);
  write(0x11,&DAT_0010094a,1);
  write(6,&DAT_00100938,1);
  write(0x1a,&DAT_0010094c,1);
  write(3,&DAT_0010094a,1);
  write(0x16,&DAT_00100946,1);
  write(0xd,&DAT_0010094e,1);
  write(0x1b,&DAT_00100950,1);
  write(0xb,&DAT_00100952,1);
  write(0x13,&DAT_00100954,1);
  write(0x17,&DAT_00100956,1);
  write(0x18,&DAT_0010094e,1);
  return 0;
}
```

There are multiple different ways to solve this challenge. One way is to open the binary in a tool such as ghidra and sort the file descripters by hand. Alternativly, ltrace can be used to print out the syscalls and sort them automatically with command line tools.


```bash
ltrace ./directionless 2>&1 | sed 's/write(//' | awk -F ',' '{print $1,'\t',$2}' | sort -n | awk -F '"' '{printf $2}'
h0w_D1d_i_93t_h3Re_1b9a78ce
```

