<!DOCTYPE html>
<?php
$ini = parse_ini_file("../settings.ini", true);
$settings = $ini["Website"];
$sql = new mysqli(
	$ini["Sql"]["hostname"],
	$ini["Sql"]["username"],
	$ini["Sql"]["password"],
	$ini["Sql"]["database"]
);

$result = mysqli_query($sql, "SELECT * FROM PlayerCount;");

$res = mysqli_fetch_all($result);
/*[
 *	[Time, PC],
 *	[Time, PC],
 *	...
 *]
*/

$dps = array();
$len = $result->num_rows;
for ($i = 0; $i < $len; $i++) {
	array_push($dps, array("x" => $res[$i][0], "y" => intval($res[$i][1])));
}

$cur = array();
$status = 0;
exec("../log.py", $cur, $status);
$cur = $cur[0];

?>
<html lang="en">
<head><script>
        window.onload = function() {
                
	    var dataPoints = <?php echo json_encode($dps, JSON_NUMERIC_CHECK); ?>;
	    for (var i = 0; i < dataPoints.length; i++) {
		dataPoints[i].x = new Date(dataPoints[i].x + " GMT+01:00");
	    }
            console.log(dataPoints); 
            var chart = new CanvasJS.Chart("chartContainer", {
                animationEnabled: true,
                theme: "dark1",
                zoomEnabled: true,
                title: {
                    text: $settings["graphtitle"]
                },
                axisY: {
                    title: "Players",
                    titleFontSize: 24
                },
                data: [{
                    type: "line",
		    dataPoints: dataPoints
                }]
            });
	    chart.render();
        }
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title><?php echo $settings["pagetitle"]?></title>
</head>
<body>
    <div id="chartContainer" style="height: 80%; width: 90%;"></div>
    <div id="currentCount">
	<p>Current playercount: <?php echo $cur; ?></p>
    </div>
<script src="https://canvasjs.com/assets/script/jquery-1.11.1.min.js"></script>
<script src="https://cdn.canvasjs.com/jquery.canvasjs.min.js"></script>
    
</body>
</html>
