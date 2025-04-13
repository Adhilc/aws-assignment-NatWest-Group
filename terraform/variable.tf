variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "EC2 Key pair name"
}

variable "bucket_name" {
  description = "Name of the S3 bucket"
}

variable "my_ip" {
  description = "Your public IP with CIDR"
  default     = "0.0.0.0/0"
}

variable "ami_id" {
  default = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI (may need to update)
}