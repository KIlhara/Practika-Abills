#!/usr/bin/perl


open(my $DATA,'<','file.txt')or die "Couldn't open file.txt,$!";

while(<$DATA>){
	print "$_";
}

close $DATA;
