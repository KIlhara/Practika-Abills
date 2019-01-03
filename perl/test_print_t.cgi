#!/usr/bin/perl
use strict;
use warnings;
use CGI;
main();

#********************************
  #database
#********************************
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

#*********************************
  # main function
#*********************************
sub main {
  print_template();
  show_table();
  delete_data();
  update_data();
  insert_data();
return 1;
}

#*********************************
  # add_info function
#*********************************
sub print_template {
print qq{Content-Type: text/html\n\n};
 open(my $DATE, "<", "test_t.html")or "Couldn't test_t.html, $!";
  while (<$DATE>){
    print "$_";
  }
close $DATE;
return 1;
}

#*********************************
  # show data function
#*********************************
sub show_table {
$dbh = DBI->connect("DBI:mysql:$db:$host:$port",$user,$pass);
$sth = $dbh->prepare("select * from games;");
 # готовим запрос
$sth->execute;
 # исполняем запрос
  while ($ref = $sth->fetchrow_arrayref){
    print "$$ref[0]." # результат
    . "$$ref[1] "
    . "$$ref[2] "
    . "$$ref[3] "
    . "$$ref[4] \n\n";
 } 
 $rc = $sth->finish;# закрываем
 $rc = $dbh->disconnect; # соединение 
return 1;
}

#*********************************
  # delete info function
#*********************************
sub delete_data {
  my $delete;
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
  my $update;
  my $choice;
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
  my $insert_id;
  my $insert_name;
  my $insert_genre;
  my $insert_developer;
  my $insert_languages;
  $sth = $dbh->prepare("insert into games values('$insert_id','$insert_name','$insert_genre','$insert_developer','$insert_languages');");
  $sth->execute;
  $rs = $sth->finish;
  $rc = $dbh->disconnect; # соединение 
  return 1;
 } 

