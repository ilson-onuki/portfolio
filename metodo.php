<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Receber dados GET</title>

<?php     
//$usuario = $_GET ['usuario'];
//$senha = $_GET ['senha'];

$usuario = $_POST ['usuario'];
$senha = $_POST ['senha'];


?>
</head>
<body>
    
</body>

<?php echo htmlspecialchars ($_POST ['usuario']); ?>
<br>
<?php echo htmlspecialchars ($_POST ['senha']); ?>



</html>