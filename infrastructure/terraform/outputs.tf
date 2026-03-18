output "public_ip" {
  value       = aws_instance.pix_host.public_ip
  description = "IP publico da instancia para deploy do docker compose."
}

output "ssh_command" {
  value       = "ssh ubuntu@${aws_instance.pix_host.public_ip}"
  description = "Comando SSH sugerido."
}
