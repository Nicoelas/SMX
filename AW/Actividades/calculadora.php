<html>
<head>
</head>
<body style="display: flex; justify-content: center; align-items: center; height: 100vh;">
<?php
if (count($_GET) == 3 && isset($_GET['op1']) && isset($_GET['op2']) && isset($_GET['op'])) {
    $op1 = $_GET['op1'];
    $op2 = $_GET['op2'];
    $op = $_GET['op'];

    if (is_numeric($op1) && is_numeric($op2)) {
        if ($op == 'suma') {
            $resultado = $op1 + $op2;
        } elseif ($op == 'resta') {
            $resultado = $op1 - $op2;
        } elseif ($op == 'multiplicacion') {
            $resultado = $op1 * $op2;
        } elseif ($op == 'division') {
            if ($op2 != 0) {
                $resultado = $op1 / $op2;
            } else {
                $resultado = "Error: División por cero.";
            }
        } else {
            $resultado = "Operación no válida. Debe ser suma, resta, multiplicación o división.";
        }

        echo "Resultado: $resultado";
    } else {
        echo "Por favor, asegúrate de que op1 y op2 sean valores numéricos.";
    }
} else {
    echo "Por favor, proporciona solo los parámetros necesarios (op1, op2, op).";
}
?>
</body>
</html>

