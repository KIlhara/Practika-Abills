#!/usr/bin/perl
my $choise = $ARGV[0];

if ($choise eq 'show'){
  open(my $DATE, "<", "test.txt") or  die "Cen't open test.txt: $!";
  while(<$DATE>){
    print $_;
  }
}

elsif ($choise eq 'insert'){ 
  open(my $r, ">", "text.txt") or die "Cen't open text.txt:$!";
  print $r "dark";
}

