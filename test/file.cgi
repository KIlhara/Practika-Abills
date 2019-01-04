#!/usr/bin/perl
my $choise = $ARGV[0];

if ($choise eq 'show'){
  open(my $data, "<", "text.txt") or  die "Cen't open text.txt: $!";
  while(<$data>){
    print $_;
  }
}

elsif ($choise eq 'insert'){ 
  open(my $dat, ">", "text.txt") or die "Cen't open text.txt:$!";
  print $dat "Dark power\n";
}

