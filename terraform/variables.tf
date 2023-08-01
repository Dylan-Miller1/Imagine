#Region
variable "region" {
  description = "the region for the service"
  type = string
  default = "us-east-1"
}

#Security Group
variable "ssh_ip" {
  description = "ip allowed for ssh"
  type = string
  default = "YOUR_IP_HERE"
}

#EC2
variable "instance_type" {
  description = "type of instnace we wish to launch"
  type = string
  default = "t2.micro"
}

variable "ami" {
  type = string
  default = "ami-09538990a0c4fe9be"
}

variable "instance_count" {
  type = number
  default = 1
}

variable "instance_name" {
  type = string
  default = "imagine_ec2"
}

variable "key_name" {
  type = string
  default = "YOUR_KEY_PAIR_NAME"
}

