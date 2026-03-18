variable "aws_region" {
  description = "Regiao AWS (Brasil: sa-east-1)."
  type        = string
  default     = "sa-east-1"
}

variable "project_name" {
  description = "Nome do projeto."
  type        = string
  default     = "pix-fraud-realtime"
}

variable "instance_type" {
  description = "Tipo da instancia EC2 que hospeda docker-compose."
  type        = string
  default     = "t3.large"
}

variable "allowed_cidrs" {
  description = "CIDRs permitidos para acesso SSH/API/Grafana."
  type        = list(string)
  default     = ["0.0.0.0/0"]
}

variable "ssh_key_name" {
  description = "Nome da key pair para SSH."
  type        = string
}
