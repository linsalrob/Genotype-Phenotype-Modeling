#!/usr/bin/perl -w
#

use strict;

my $count;
for my $f (@ARGV) {
	open(IN, $f) || die "$! $f";
	while (<IN>) {
		chomp;
		my @a=split /\t/;
		$count->{$a[1]}->{$f}=1
	}
}

foreach my $k (keys %$count) {
	print join("\t", $k, (scalar(keys(%{$count->{$k}}))/scalar(@ARGV))), "\n";
}
