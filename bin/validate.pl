#!/usr/bin/perl

use strict;
use utf8;
use warnings;

use WebService::Validator::CSS::W3C;


my $css = "";
while(<STDIN>){ $css .= $_; }

my $val = WebService::Validator::CSS::W3C->new;
my $ok = $val->validate(string => $css);

if ($ok and !$val->is_valid) {
	die('Not valid CSS');
}
print STDOUT "OK.\n";
exit 0;
