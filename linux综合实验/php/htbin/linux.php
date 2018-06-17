<?php

$con = mysqli_connect('localhost', 'user', 'password','linux');
if (!$con)
 {
 die('Could not connect: ' . mysqli_connect_error());
 }

//echo "连接成功\n";

$sql="SELECT * FROM demo";

$result = mysqli_query($con,$sql);

$dic = array();

while($row = mysqli_fetch_assoc($result))
 {
 $dic[$row['name']]=$row['id'];
 }

echo json_encode($dic);
mysqli_close($con);
?>
