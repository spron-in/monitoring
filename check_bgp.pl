#!/usr/bin/perl -w
#
#
#

use strict;

my @bgp_vtysh = ();
my @bgp6_vtysh = ();
my $EXIT_FLAG = 0;
my ($nei, $state, $state_check, $HOST);

my $sudo = '';
my $vtysh = '';

if ($^O =~ m/linux/i) {
	$sudo = '/usr/bin/sudo';
	$vtysh = '/usr/bin/vtysh';
}
elsif ($^O =~ m/freebsd/i) {
	$sudo = '/usr/local/bin/sudo';
	$vtysh = '/usr/local/bin/vtysh';
}

if (! $sudo or ! $vtysh) {
	$EXIT_FLAG++;
}

@bgp_vtysh = `$sudo $vtysh -c 'sh ip bgp summary'`;
@bgp6_vtysh = `$sudo $vtysh -c 'sh ipv6 bgp summary'`;

if (! @bgp_vtysh) {
    $EXIT_FLAG++;
}

foreach (@bgp_vtysh) {

	chomp;
    
    if ($_ =~ m/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.+\s+(\D+)$/i) {
		$EXIT_FLAG++;
    } else {
        next;
    }
}

my $flag = 0;
foreach (@bgp6_vtysh) {

	chomp;

    if ($_ =~ m/^[a-f0-9\:]+$/i) {
        $flag = 1;
    } 
    elsif ($flag == 1 and m/.+(\D+)$/) {
        $flag = 0;
        $EXIT_FLAG++;
    } elsif ($flag == 0 and $_ =~ m/^[a-f0-9\:]+\s+4.+(\D+)$/) {
        $EXIT_FLAG++;
    } else {
        $flag = 0;
        next;
    }

}

print "$EXIT_FLAG\n";
