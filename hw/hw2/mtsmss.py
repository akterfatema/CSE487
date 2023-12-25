import subprocess
import re


def discover_mtu():
    # Run ping command with the "Don't Fragment" flag and increasing packet sizes
    for packet_size in range(1460, 1000, -1):
        ping_command = "ping 8.8.8.8 -f -l " + \
            str(packet_size)  # Change the IP address as needed
        result = subprocess.run(
            ping_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        output = result.stdout
        print(output)
        # Check if packet fragmentation occurred
        if "sent" in output:
            return packet_size

    return None


def discover_mss():
    # Run ping command and extract MSS from the output
    ping_command = "ping -c 1 www.google.com"  # Change the IP address as needed
    result = subprocess.run(ping_command, shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    output = result.stdout
    print(output)
    # Extract MSS value from output using regular expression
    mss_match = re.search(
        r"icmp_seq=\d+ ttl=\d+ time=\d+\.\d+ ms MSS=(\d+)", output)
    if mss_match:
        mss = int(mss_match.group(1))
        return mss

    return None


# Discover MTU and MSS
mtu = discover_mtu()
mss = discover_mss()

# Print the results
if mtu:
    print(f"Discovered MTU: {mtu} bytes\n\n")
else:
    print("MTU discovery failed")

if mss:
    print(f"Discovered MSS: {mss} bytes")
else:
    print("MSS discovery failed")
