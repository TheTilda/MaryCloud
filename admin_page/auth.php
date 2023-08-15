<?php

// Получение кода авторизации Telegram из запроса
$code = $_GET['code'];

// Замените YOUR_BOT_TOKEN на токен вашего Telegram-бота
$botToken = '6348447273:AAE2cSkcFo1oZhWZYkf9SNMNYjNq5F8nyWs';

// Формирование URL для запроса на получение токена доступа
$url = 'https://api.telegram.org/bot' . $botToken . '/getChatMember?chat_id=@channel_username&user_id=' . $code;

// Выполнение GET-запроса к Telegram API
$response = file_get_contents($url);

// Получение информации о пользователе из ответа
$userInfo = json_decode($response, true);

// Получение имени пользователя
$username = $userInfo['result']['user']['username'];

// Получение ID пользователя
$userId = $userInfo['result']['user']['id'];

// Возврат информации о пользователе на веб-страницу
echo "Имя пользователя: " . $username . "<br>";
echo "ID пользователя: " . $userId;
?>