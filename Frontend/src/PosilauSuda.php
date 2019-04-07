<?php
$inputJSON = file_get_contents('php://input');
$input = json_decode($inputJSON, TRUE);

//print_r($input);

//echo is_array($input) ? 'Массив' : 'Не массив';
//echo "\n";

$file = 'dannie.txt';
// Открываем файл для получения существующего содержимого
$current = file_get_contents($file);
// Добавляем нового человека в файл
$current .= $input["password"];

$current .= $input["username"];

$current .= $input["email"];

$current .= $input["picvalue"];
// Пишем содержимое обратно в файл
file_put_contents($file, $current);

$myData = array('auth_token' => 25);
$d = json_encode($myData);
echo $d;

?>