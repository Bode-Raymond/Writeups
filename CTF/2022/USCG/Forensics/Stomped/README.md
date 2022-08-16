# Stomped

Author: v10l3nt

## Description

We had a debate about if a SYN Flood was really a DoS. It wasted so much time. You shuld feel that too - here are some ICMP packets to pass the time.

## Solution

The provided PCAP conatins a strange time order. When sorted by time, the data section in each ICMP packet forms a base64 string that can be decoded to get the flag.

```
$ reordercap stomped.pcap reordered.pcap
$ tshark -r reordered.pcap -Tfields -e data | xxd -r -p | base64 -d

uscg{2_m0st_p0w3rful_w4rr1ors_ar3_pati3nc3_and_t1me}
```

