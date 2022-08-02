<?php

$destino = "contacto@rcrmateriales.com.mx";
$nombre = $_POST["nombre"];
$empresa = $_POST["empresa"];
$telefono = $_POST["telefono"];
$email = $_POST["email"];
$mensaje = $_POST["mensaje"];

$contenido = "Nombre: ".$nombre ."\n Empresa: " . $empresa . "\n Teléfono: ". $telefono .  "\n Email: ". $email . "\n Mensaje: " . $mensaje;

mail($destino,"Información",$contenido);
header("Location:home.html");

?>