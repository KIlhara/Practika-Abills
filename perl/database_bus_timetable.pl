#!/usr/bin/perl

use DBI;
my $name = $ARGV[0]; 
my $choice = $ARGV[1];
my $update = $ARGV[2];
my $insert_name = $ARGV[3];
my $insert_cost = $ARGV[4];
my $insert_status = $ARGV[5];

my $host = "127.0.0.1";  
 # вымышленный MySQL-сервер
my $port = "3306";  
 # порт, на который открываем соединени
my $user = "root";  
 # имя пользователя (вымышленное)
my  $pass = "misha";
 # пароль
my $db = "bus_timetable";
 # имя базы данных-по умолчанию равно имени пользователя
#print "Content-type: text/html\n\n";


$dbh = DBI->connect("DBI:mysql:$db:$host:$port",$user,$pass);
if ($name eq 'show' ){
  $sth = $dbh->prepare("select * from schedule;");
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
}

elsif($name eq 'delete'){
  $sth = $dbh->prepare("delete from schedule where id='$choice';");
  $sth->execute;
  print "Delete completed\n";
  $rs = $sth->finish;
}

elsif($name eq 'update'){
  $sth = $dbh->prepare("update schedule set id='$update' where name='$choice';");
  $sth->execute;
  print "Update completed\n";
  $rs = $sth->finish;
}

elsif($name eq 'insert'){
  my $insert_id = $choice;
  my $insert_time = $update;
  $sth = $dbh->prepare("insert into schedule values('$insert_id','$insert_time','$insert_name','$insert_cost','$insert_status');");
  $sth->execute;
  print "Insert completed\n";
  $rs = $sth->finish;
}

$rc = $dbh->disconnect; # соединение 
