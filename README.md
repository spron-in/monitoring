# monitoring scripts

Some useful scripts for monitoring

## check_bgp.pl

Monitor BGP in Quagga routing daemon. Usage: `perl check_bgp.pl`

User should be in sudoers with permissions for vtysh. Smth like that:

`youruser ALL=(ALL) NOPASSWD: /usr/bin/vtysh -c sh ip*`
