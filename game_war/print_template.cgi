#!/usr/bin/perl

use strict;
use warnings;
use CGI;
use DBI;
use Data::Dumper;

print qq{Content-Type: text/html\n\n};
#*********************************
  #database
#*********************************
my $host = "127.0.0.1";  
 # MySQL-сервер
my $port = "3306";  
 # порт
my $user = "root";  
 # користувач
my  $pass = "misha";
 # пароль
my $db = "game_war";
 # база даних

my $dbh = DBI->connect("DBI:mysql:$db:$host:$port",$user,$pass);

our ($sth, $ref, $rc, $rs, %FORM);

main();

#*********************************
  # main function
#*********************************
sub main {
  parse_form();

  if ($FORM{add}==1) {
    insert_data();
  }
  elsif ($FORM{delete}){
    # print "you delete game $FORM{name}";
    delete_data($FORM{delete});
  }

  my $perunt = print_template("template.html");
  my $kards = show_table();



  print print_template("main_templete.html",{TEMPLETE1 => $perunt, TEMPLETE2 => $kards});
  # my $main_tem = print_template("main_templete.html",{TEMPLETE1 => $perunt, TEMPLETE2 => $kards});
  # print $main_tem;
return 1;
}
#*********************************
  # add_info function
#*********************************
sub print_template {
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
 

#*********************************
  # show info function
#*********************************
sub show_table {
$sth = $dbh->prepare("select * from games;");
 # готовим запрос
$sth->execute;
 # исполняем запрос
my $ret;
while (my @ary = $sth->fetchrow_array())
{  
    $ret= $ret. print_template("template1.html", {
      ID        => $ary[0],
      NAME      => $ary[1],
      GENRE     => $ary[2],
      DEVELOPER => $ary[3],
      LANGUAGES => $ary[4],
      });
}
return $ret;
}


#*********************************
  # delete info function
#*********************************
sub delete_data {
  my ($delete)=@_;
  $sth = $dbh->prepare("delete from games where id_game='$delete';");
  $sth->execute;
  $rs = $sth->finish;
  $rc = $dbh->disconnect; # соединение 
  return 1;
}

#*********************************
  # updata info function
#*********************************
sub update_data {
  my $update=0;
  my $choice=0;
  $sth = $dbh->prepare("update games set name_game='$update' where id_game='$choice';");
  $sth->execute;
  $rs = $sth->finish;
  $rc = $dbh->disconnect; # соединение 
  return 1;
}

#*********************************
  # insert info function
#*********************************
sub insert_data {
  my $insert_id=$FORM{id};
  my $insert_name=$FORM{name};
  my $insert_genre=$FORM{genre};
  my $insert_developer=$FORM{developer};
  my $insert_languages=$FORM{languages};
  $sth = $dbh->prepare("insert into games values('$insert_id','$insert_name','$insert_genre','$insert_developer','$insert_languages');");
  $sth->execute;
  $rs = $sth->finish;
  $rc = $dbh->disconnect; # соединение 
 } 

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
