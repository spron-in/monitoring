# monitoring scripts

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

`
$ python bind_stats.py AAAA

198556650
`

### Requirements

1. pip install requests

1. Of course bind9 should be configured with json support. We hate XML, right? In bind config do not forget to add smth like:

`
statistics-channels {
        inet 127.0.0.1 port 8080 allow { 127.0.0.1; };
};
`
