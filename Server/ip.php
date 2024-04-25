<?php

// Function to sanitize input data
function sanitize($data) {
    return htmlspecialchars(trim($data));
}

// Get IP address
$ipaddress = $_SERVER['HTTP_CLIENT_IP'];

$ifnot = $_SERVER['HTTP_X_FORWARDED_FOR']."\r\n";

// Get user agent
$useragent = isset($_SERVER['HTTP_USER_AGENT']) ? sanitize($_SERVER['HTTP_USER_AGENT']) : '';

// Log format
$logEntry = "IP: $ipaddress\nUser Agent: $useragent\nifnot: $ifnot\n\n";

// Log file
$logFile = 'ip.log';

// Append to log file
file_put_contents($logFile, $logEntry, FILE_APPEND | LOCK_EX);

?>
