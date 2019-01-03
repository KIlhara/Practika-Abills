#!/urs/bin/perl

my $name = $ARGV[0];

if($name eq 'write'){
  open($DATE, ">", "file.txt")or "Couldn't file.txt, $!";
  print $DATE "Hello world of war\n";
  print $DATE "Game war\n";
}

elsif ($name eq 'open'){
  open($DATE, "<", "file.txt")or "Couldn't file.txt, $!";
  while (<$DATE>){
    print "$_";
  }
close $DATE;
}
else{
  print "Error\n";
}


