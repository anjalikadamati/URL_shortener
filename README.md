# 🔗 Scalable URL Shortener

A production-ready URL shortener built with Flask, designed with scalability and performance in mind using Redis caching, NGINX load balancing, and Dockerized microservices.

---

## 🚀 Features

* 🔗 Shorten long URLs into compact links
* ⚡ Redis caching for fast redirection
* 📊 Click tracking (analytics)
* ⏳ Optional expiration for links
* 🚫 Rate limiting using Redis (prevents abuse)
* ⚖️ Load balancing using NGINX
* 🐳 Fully Dockerized (multi-container setup)
* 🔄 Multiple backend instances (horizontal scaling)
* 🌐 REST API + React frontend

---

## 🏗️ Architecture

Client → NGINX (Load Balancer) → Flask Instances (Gunicorn) → MySQL
↓
Redis (Cache)

---

## 🛠️ Tech Stack

### Backend

* Flask
* Gunicorn
* SQLAlchemy
* MySQL

### Frontend

* React (Vite)
* CSS (custom styling)

### Infrastructure

* Docker & Docker Compose
* NGINX (reverse proxy + load balancing)
* Redis (caching + rate limiting)

---

## 📡 API Endpoints

### 🔹 Create Short URL

POST `/shorten`

```json
{
  "url": "https://example.com"
}
```

---

### 🔹 Redirect

GET `/<short_code>`

---

### 🔹 Get Recent Links

GET `/api/recent`

---


---

## ⚙️ Local Setup

```bash
git clone <your-repo>
cd url-shortener

docker-compose up --build
```

---

## 🌍 Deployment

* Backend: Render (Docker)
* Frontend: Vercel

---

## 🧠 Key Concepts Implemented

* Caching using Redis to reduce DB load
* Rate limiting using Redis counters
* Load balancing across multiple instances using NGINX
* Stateless backend services for scalability
* Separation of concerns using microservices

---

## 📌 Future Improvements

* User authentication
* Custom aliases for URLs
* Advanced analytics dashboard
* QR code generation
* AWS deployment (EC2, RDS, S3)

---
