# scripts

Some useful scripts for monitoring

## check_bgp.pl

Monitor BGP in Quagga routing daemon. 

### Usage

`perl check_bgp.pl`

### Requirements

User should be in sudoers with permissions for vtysh. Smth like that:

`youruser ALL=(ALL) NOPASSWD: /usr/bin/vtysh -c sh ip*`

## bind_stats.py

Get qtype stats from bind9 DNS. 

### Usage

`python bind_stats.py %QTYPE%`

```
$ python bind_stats.py AAAA
198556650
```

### Requirements

1. pip install requests

1. Of course bind9 should be configured with json support. We hate XML, right? In bind config do not forget to add smth like:

```
statistics-channels {
        inet 127.0.0.1 port 8080 allow { 127.0.0.1; };
};
```

## modify_path.py

Just a funny script for modifying traceroute output with scapy.

### Usage

1. Block icmp6 on local firewall (ip6tables)
1. Add alias ipv6 address to the interface
1. Run the script with needed params

`python modify_path.py -i interface_name -r replace_ip`

More details at https://spronin.blogspot.ru/2016/12/when-scapy-gets-bored.html

### Requirements

1. pip install scapy


