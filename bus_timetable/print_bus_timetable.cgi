#!/usr/bin/perl

use utf8;
use strict;
use warnings;
use CGI;
use DBI;
use Data::Dumper;


print qq{Content-Type: text/html\n\n};

#********************************
#           Database            #
#********************************
my $host="127.0.0.1";

my $port="3306";

my $user="root";

my $pass="misha";

my $db="bus_timetable";

my $dbh = DBI->connect("DBI:mysql:$db:$host:$port",$user,$pass,{mysql_enable_utf8 => 1});

our ($sth, $ref, $rc, $rs, %FORM);

main();
#*********************************
#          main function         #
#*********************************
sub main{
  parse_form();

  if ($FORM{add} && $FORM{add}==1) {
    insert_data();
  }

  my $intput = intput_bus("insert_bus_timetable.html");
  my $output = show_table();
  my $main_templete = intput_bus("main_bus_timetable.html",{INSERT => $intput, SHOW => $output});
  print $main_templete;
  
}

#********************************
#         reading file          #
#********************************
sub intput_bus {
  my($link, $attributes) = @_;
  my $content;
  open(my $DATE, "<", "$link") or die "Couldn't $link, $!";
   while (<$DATE>){
    my @vars = $_ =~ /\%(.+?)\%/g;
    foreach my $var (@vars){
      $_ =~ s/\%$var\%/($attributes->{$var} || '')/ge;
    }
      $content = $content. $_;
   }
 close $DATE;
return $content;
}

#********************************
#      output data in file      #
#********************************
sub show_table {
  $sth = $dbh->prepare("select * from schedule;");
   # готовим запрос
  $sth->execute;
   # исполняем запрос
  my $ret;
  while (my @ary = $sth->fetchrow_array())
  {  
    $ret= $ret. intput_bus("show_bus_timetable.html", {
      ID         => $ary[0],
      TIME       => $ary[1],
      NAME       => $ary[2],
      COST       => $ary[3],
      STATUS     => $ary[4],
      });
  }
  return $ret;
}

#********************************
#    intput data in database    #
#********************************
sub insert_data {
  my $insert_id=$FORM{id};
  my $insert_time=$FORM{time};
  my $insert_name=$FORM{name};
  my $insert_cost=$FORM{cost};
  my $insert_status=$FORM{status};
  $sth = $dbh->prepare("insert into schedule values('$insert_id','$insert_time','$insert_name','$insert_cost','$insert_status');");
  $sth->execute;
  $rs = $sth->finish;
  $rc = $dbh->disconnect; # соединение 
 }

#*********************************
#  Delete data from database     #
#*********************************
# sub delete_data{
#   my $choise;
#   $sth = $dbh->


# } 
#*********************************
#            GET request         #
#*********************************
sub parse_form {
  # read(STDIN, my $buffer, $ENV{'CONTENT_LENGTH'});
  my $buffer = $ENV{QUERY_STRING};
# Split information into name/value pairs
  my @pairs = split(/&/, $buffer);
  foreach my $pair (@pairs) {
    my($name, $value) = split(/=/, $pair);
    $value =~ tr/+/ /;
    $value =~ s/%(..)/pack("C", hex($1))/eg;
    $FORM{$name} = $value;
  }
}
