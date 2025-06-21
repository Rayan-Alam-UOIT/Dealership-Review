# 🚗 Dealership Review Portal

A full-stack web application that allows users to browse, review, and manage dealership branches across the United States. Built using Django, React, Node.js, MongoDB, and deployed with Docker, Kubernetes, and IBM Cloud Code Engine.

![Solution Architecture](architecture.png)

---

## 🧩 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🎯 Features](#-features)
- [🔧 Tech Stack](#-tech-stack)
- [📁 Folder Structure](#-folder-structure)
- [🚀 Setup & Deployment](#-setup--deployment)
- [🧪 Testing](#-testing)
- [🔐 Roles & Use Cases](#-roles--use-cases)
- [📡 Microservices Overview](#-microservices-overview)
- [📸 Screenshots](#-screenshots)
- [📄 License](#-license)

---

## 📌 Project Overview

The Dealership Review Portal provides a centralized platform for customers to browse dealership branches, view and post reviews, and for admins to manage car data. This platform brings transparency and trust to the dealership experience.

---

## 🎯 Features

### 🔓 Anonymous Users
- View About Us and Contact Us pages
- Browse dealership listings
- Filter dealerships by state
- View dealership reviews

### ✅ Authorized Users
- Log in with Django auth system
- Post reviews with sentiment analysis
- Submitted reviews appear at the top, sorted by timestamp

### 🛠️ Admin Users
- Log in to Django admin panel
- Manage car makes, models, and metadata

---

## 🔧 Tech Stack

| Layer                     | Technology                           |
|--------------------------|--------------------------------------|
| Frontend (User)          | React + Bootstrap                    |
| Backend (App)            | Django + SQLite                      |
| Backend (Dealers/Reviews)| Node.js (Express) + MongoDB          |
| NLP                      | IBM Watson (Code Engine)             |
| Deployment               | Docker, Kubernetes, IBM Cloud        |
| Authentication           | Django User Auth                     |

---
