#Provider Block
provider "aws" {
  profile = "default"
  region = var.region
}

#Resources Block
resource "aws_security_group" "allow_http_and_SSH" {
  name = "aws_security_group"
  description = "allows HTTP traffic and SSH"

  ingress {
    description = "HTTP"
    from_port = 80
    to_port = 80
    protocol = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTPS"
    from_port = 443
    to_port = 443
    protocol = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port = 22
    to_port = 22
    protocol = "TCP"
    cidr_blocks = [var.ssh_ip]
  }

  ingress {
    description = "flask_app"
    from_port = 3000
    to_port = 3000
    protocol = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "outbound"
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "imagine" {
  ami = var.ami
  instance_type = var.instance_type
  key_name = var.key_name
  tags = {
    Name = var.instance_name
  }
  security_groups = [aws_security_group.allow_http_and_SSH.name]
}