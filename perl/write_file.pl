#!/usr/bin/perl



=head1 NAME


  Hellow world

=cut

my $name = $ARGV[0];

if ($name eq 'write'){
  open(my $DATA, ">", "file.txt")or die "Couldn't file file.txt, $!";
    print $DATA "Hello Game\n";
    print $DATA "Game war\n\n";
}
elsif ($name eq 'open'){
  open(my $DATA, "<", "file.txt")or die "Couldn't file file.txt, $!";
    while (<$DATA>){
      print "$_";
    }
  close $DATA;
}
else {
  print "Error\n";
}


#***************************************************
=head2 hello_world() - Welcome function

  Arguments:
    $name  - User name
  Returns:
    TRUE or FALSE

  Examples:
   hello_world('Johny');


=cut
#***************************************************
#
