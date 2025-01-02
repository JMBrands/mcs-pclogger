<?php
$out = array();
$status = 0;

exec("python log.py debug", $out, $status);

echo $out[0];


?>
