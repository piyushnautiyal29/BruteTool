<?php
/*
 * This page generates a CAPTCHA figure
 */
include 'functions.php';
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: SAMEORIGIN');
function create_captcha()						                    #Creates a 6 digit random text consisting alphanumeric characters
{
	$characters = array_merge(range(0,9),range('A','Z'),range('a','z'));
	shuffle($characters);
	$text="";
	for($i=0;$i<6;$i++)
	{
		$text = $text.$characters[rand(0,count($characters)-1)];
	}
	return $text;
}

$text = create_captcha();
$image = imagecreate(100, 16);								        #Creates an image of captcha and sends to authentication page
$bg = imagecolorallocate($image, 255, 255, 255);
$textcolor = imagecolorallocate($image, 0, 0, 255);
imagestring($image, 5, 0, 0, $text, $textcolor);
header('Content-type: image/png');
imagepng($image);
imagedestroy($image);
?>
