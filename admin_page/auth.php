<?php

// ��������� ���� ����������� Telegram �� �������
$code = $_GET['code'];

// �������� YOUR_BOT_TOKEN �� ����� ������ Telegram-����
$botToken = '6348447273:AAE2cSkcFo1oZhWZYkf9SNMNYjNq5F8nyWs';

// ������������ URL ��� ������� �� ��������� ������ �������
$url = 'https://api.telegram.org/bot' . $botToken . '/getChatMember?chat_id=@channel_username&user_id=' . $code;

// ���������� GET-������� � Telegram API
$response = file_get_contents($url);

// ��������� ���������� � ������������ �� ������
$userInfo = json_decode($response, true);

// ��������� ����� ������������
$username = $userInfo['result']['user']['username'];

// ��������� ID ������������
$userId = $userInfo['result']['user']['id'];

// ������� ���������� � ������������ �� ���-��������
echo "��� ������������: " . $username . "<br>";
echo "ID ������������: " . $userId;
?>