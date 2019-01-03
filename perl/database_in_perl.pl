#!/usr/bin/perl

use DBI;
my $name = $ARGV[0]; 
my $choice = $ARGV[1];
my $update = $ARGV[2];
my $insert_genre = $ARGV[3];
my $insert_developer = $ARGV[4];
my $insert_languages = $ARGV[5];

my $host = "127.0.0.1";  
 # вымышленный MySQL-сервер
my $port = "3306";  
 # порт, на который открываем соединени
my $user = "root";  
 # имя пользователя (вымышленное)
my  $pass = "misha";
 # пароль
my $db = "game_war";
 # имя базы данных-по умолчанию равно имени пользователя
#print "Content-type: text/html\n\n";


$dbh = DBI->connect("DBI:mysql:$db:$host:$port",$user,$pass);
if ($name eq 'show' ){
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
}

elsif($name eq 'delete'){
  $sth = $dbh->prepare("delete from games where id_game='$choice';");
  $sth->execute;
  print "Delete completed\n";
  $rs = $sth->finish;
}

elsif($name eq 'update'){
  $sth = $dbh->prepare("update games set name_game='$update' where id_game='$choice';");
  $sth->execute;
  print "Update completed\n";
  $rs = $sth->finish;
}

elsif($name eq 'insert'){
  my $insert_id = $choice;
  my $insert_name = $update;
  $sth = $dbh->prepare("insert into games values('$insert_id','$insert_name','$insert_genre','$insert_developer','$insert_languages');");
  $sth->execute;
  print "Insert completed\n";
  $rs = $sth->finish;
}

else{
  print "Error\n";
}

$rc = $dbh->disconnect; # соединение 
