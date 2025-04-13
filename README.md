# AWS Assignment – S3, EC2, Lambda, Terraform, Boto3, and CI/CD

This project showcases AWS services including S3, EC2, Lambda, IAM, and integrates Infrastructure as Code using Terraform, scripting with Python (Boto3), and CI/CD automation using GitHub Actions.

---

## Table of Contents

- [Task 1: AWS Services](#task-1-aws-services)
- [Task 2: Scripting](#task-2-scripting)
- [Task 3: CI/CD Basics](#task-3-cicd-basics)
- [Task 4: Infrastructure as Code (Terraform)](#task-4-infrastructure-as-code-terraform)
- [Cost Estimation](#cost-estimation)
- [Prerequisites](#prerequisites)
- [How to Use](#how-to-use)
- [Links to AWS SDK Docs](#links-to-aws-sdk-docs)

---

## Task 1: AWS Services

### 1. S3 Bucket (Static Website)
- Created an S3 bucket with public access enabled for hosting a static website.
- Configured index.html as the entry point.

### 2. EC2 Instance
- Launched an Amazon Linux EC2 instance.
- Installed Apache and hosted a simple HTML page.
- Security group allows HTTP (port 80) access from my IP only.

### 3. Lambda Function
- Python-based Lambda triggered on S3 object creation.
- Logs event data to CloudWatch.

---

## Task 2: Scripting

### 1. Python + Boto3 Script
- Lists all S3 buckets.
- Displays total number of objects in a specified bucket.

### 2. CSV Analyzer
- Analyzes student data (name, age, grades).
- Prints names of students with average grade above a threshold.

Sample CSV Format:
name,age,grade John,20,85,90,80 Jane,22,70,75,72


## Task 3: CI/CD Basics

- Configured a GitHub repository.
- Set up GitHub Actions to run Python scripts on push.
- Ensures all scripts are tested automatically.

CI/CD File: .github/workflows/deploy.yml

---

## Task 4: Infrastructure as Code (Terraform)

### 1. Terraform Files
- Provisioned an EC2 instance with security group and Apache setup.
- Created an S3 bucket for static content.
- IAM role and Lambda integrated with S3 bucket events.

### 2. Parameterized Variables
- instance_type, key_name, bucket_name, and my_ip are configurable.

---

## Cost Estimation

| Service       | Monthly Estimate | Annual Estimate |
|---------------|------------------|-----------------|
| EC2 (t2.micro)| Free (first year)| $0              |
| S3            | ~$0.01           | ~$0.12          |
| Lambda        | Free Tier        | $0              |

> Total Annual Cost: Less than $1 (assuming usage remains within free tier and light traffic)

---

## Prerequisites

- AWS CLI & credentials configured
- Terraform installed
- Python 3.8+ with Boto3
- GitHub account & repo



