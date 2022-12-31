# Task A1

## Description

We believe that the attacker may have gained access to the victim's network by phishing a legitimate users credentials and connecting over the company's VPN. The FBI has obtained a copy of the company's VPN server log for the week in which the attack took place. Do any of the user accounts show unusual behavior which might indicate their credentials have been compromised?

Note that all IP addresses have been anonymized.

## Solution

It can be noted from the description that because the credentials are legitimate, the solution will not be found in failed logins or users not found. Additionally, due to IP addresses being anonymized, there will be no geo-disparate data or any similar metric that can be used to find anomalies. Using the information derived from the challenge description, it can be seen that the most likely anomaly is simultaneous logins.

I used `awk` with `sort` to parse the data in a way that allowed me to easily analyze time stamps.

`awk -F ',' '{print $2,"\t",$3,"\t",$4/60/60}' vpn.log | sort`

Looking through the data returned from the above command reveals that Kimberly.M had multiple sessions open at the same time.

