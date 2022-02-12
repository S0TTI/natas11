<?php

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=");
$text = json_encode($defaultdata);
$outText = "";

for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
}
echo  $outText ;

?>