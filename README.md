# 📊 Marketing Client Portal - Serverless AWS Project

This project demonstrates how to build a fully **serverless marketing client registration portal** using AWS services. It is designed for marketing companies that need to register and retrieve client information efficiently and securely.

---

## 🧰 Technologies and AWS Services Used

- **Amazon S3** – Static website hosting
- **CloudFront** – CDN and HTTPS delivery
- **API Gateway** – RESTful API management
- **AWS Lambda** – Backend logic (register & retrieve)
- **DynamoDB** – NoSQL database storage
- **(Optional) KMS** – Data encryption
- **(Optional) Route 53** – Custom domain setup

---

## 🖼️ Features

- Client registration form (Name, Email, Company, Requested Service)
- Client information retrieval by email
- Clean, responsive interface using HTML + Bootstrap
- REST API with `POST` and `GET` methods
- Scalable and secure serverless architecture

---

## 🧱 Architecture Overview


---

## 🚀 Deployment Steps

### 1. DynamoDB
- Create a table named `Clients`
- Primary key: `email` (String)

### 2. Lambda
- Create a function with permission to access DynamoDB
- Add CORS headers to all responses
- Connect it to API Gateway

### 3. API Gateway
- Create a REST API
- Add the following endpoints:
  - `POST /clients` – to register clients
  - `GET /clients/{email}` – to retrieve client info
- Enable CORS for all methods
- Deploy the API to a stage

### 4. Frontend (HTML)
- Upload `index.html` and images to an S3 bucket
- Enable static website hosting
- Create a CloudFront distribution pointing to the S3 bucket

### 5. (Optional)
- Use KMS to encrypt DynamoDB data
- Use Route 53 to map a custom domain (e.g., `portal.yourcompany.com`)

---

## 🔍 Testing

1. Visit the CloudFront URL
2. Submit a new client registration
3. Retrieve client data using the email
4. Verify entries in DynamoDB

---

## 🛠️ Troubleshooting

| Issue                          | Solution                                                   |
|-------------------------------|------------------------------------------------------------|
| CORS errors                   | Enable CORS in both API Gateway and Lambda responses       |
| API not responding / 404      | Check resource paths, deployment stage, and method setup   |
| Frontend changes not visible  | Invalidate CloudFront cache and clear browser cache        |
| Lambda not executing/logging  | Verify IAM permissions and check CloudWatch logs           |

---

## ✨ Credits

Project developed by [Your Name or Company] as part of the **DevOps Easy Learning** course.  
Built with modern, scalable AWS serverless architecture.

---

## 📄 License

This project is free to use for educational and professional purposes. You may adapt it to fit your company's needs.
