# Hidden Wisdom

## Description

I got banned from my favorite video game for hacking, but a friend found a way to send me a message through the game anyway. Can you help me find his hidden wisdom?

## Solution

There is a noticable pattern in the timing between packets in the PCAP file which point to the flag being hidden in the time deltas. 

The flag appears to be encoded in a binary format using the time delta encoding as shown below:

Time delta ~= 0.000002 => NOP
Time delta ~= 0.1 => 0
Time delta ~= 0.3 => 1

The times can be extracted using `tshark` and `awk` as shown below.

```bash
tshark -r hidden_wisdom.pcap | awk -F ' ' '{print $2}' > time.txt
```

Once the time stamps are extracted the flag can be recoved using python to parse the data.

```python
f = open('time.txt', 'r')

prev = 0
char = ''

for time in f.readlines():
    time = round(float(time.strip()),2)
    delta = time - prev

    if delta > 0.28 and delta < 0.32:
        char += '1'
    elif delta > 0.08 and delta < 0.12:
        char += '0'
    
    prev = time

    if len(char) == 8:
        print(chr(int(char ,2)), end='')
        char = ''

print()
```

