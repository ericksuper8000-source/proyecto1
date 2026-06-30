# 🚀 Python CI/CD, Containers & DevOps Practice Project

📅 **Started:** 06/30/2026

This repository documents my transition from writing isolated Python exercises to building and operating real-world software delivery pipelines. 

The goal of this project is not to build a complex application, but to understand how modern software is developed, tested, containerized, validated, published, deployed, and maintained using industry-standard DevOps practices.

---

## 🎯 Project Goals

This project was created to gain hands-on experience with:

* CI/CD pipelines
* Automated testing
* Code quality validation
* Docker containerization
* Container registries
* Deployment automation
* Infrastructure concepts
* Service lifecycle management
* Multi-platform CI environments
* Production-oriented workflows

Rather than focusing exclusively on application complexity, this repository focuses on the **complete software delivery lifecycle**.

---

## 🧠 What This Project Demonstrates

This project currently includes:

* ✅ Python application development
* ✅ Unit testing with `pytest`
* ✅ Automated linting and formatting validation
* ✅ GitHub Actions CI pipelines
* ✅ GitLab CI/CD pipelines
* ✅ Docker image creation
* ✅ Docker Compose orchestration
* ✅ Docker Hub registry integration
* ✅ GitHub Container Registry (GHCR) integration
* ✅ GitLab Container Registry integration
* ✅ Multi-registry image publishing
* ✅ Automatic container restart policies
* ✅ Automatic container updates with Watchtower
* ✅ Continuous Deployment (CD) simulation

---

## 🏗️ Current Architecture

```text
Developer Push
      ↓
GitHub / GitLab
      ↓
CI Pipeline
├── flake8
├── black
├── pytest
└── Docker build
      ↓
┌────────────────────────────────────────┐
│              Docker Hub                │
│           erickdev8/mi-app             │
├────────────────────────────────────────┤
│       GitHub Container Registry        │
│          ghcr.io/.../mi-app            │
├────────────────────────────────────────┤
│        GitLab Container Registry       │
│        [registry.gitlab.com/](https://registry.gitlab.com/)...         │
└────────────────────────────────────────┘
      ↓
Watchtower detects updates
      ↓
Docker Compose recreates container
      ↓
Updated application running
🛠️ Technologies Used
Core Development
Python 3.11

pytest

flake8

black

CI/CD
GitHub Actions

GitLab CI/CD

Containers & Deployment
Docker

Docker Compose

Docker Hub

GitHub Container Registry (GHCR)

GitLab Container Registry

Watchtower

Development Tools
Git

Git Bash

Visual Studio Code

📦 Why Docker Was Added
Originally, this project consisted only of a simple Python application with unit tests. As the learning process evolved, Docker was introduced to better understand:

Portable environments

Container lifecycle management

Image registries

Deployment automation

Production-like environments

The objective was to simulate how modern applications move from development into deployment through automated delivery pipelines.

🔄 CI/CD Workflow
Every push or pull request triggers automated validation pipelines. The workflow currently performs:

Source checkout

Python environment setup

Dependency installation

flake8 lint validation

black formatting validation

pytest execution

Docker image build

Docker image tagging

Push to Docker Hub

Push to GitHub Container Registry (GHCR)

Push to GitLab Container Registry

The same Docker image is automatically published to multiple registries from a single CI pipeline. Once the image reaches the registries, Watchtower can automatically detect updates and recreate the running container. This creates a simplified Continuous Deployment workflow.

🧠 Key Concepts Learned
Throughout this project I learned:

Difference between CI and CD

Automated validation pipelines

Docker image lifecycle

Container registries and image distribution

Multi-registry publishing strategies

GitHub Actions workflow design

GitLab CI/CD fundamentals

Deployment automation concepts

Docker Compose orchestration

Watchtower update automation

Infrastructure reproducibility

Secure secret management in CI/CD systems

⚠️ Challenges Encountered
Some of the real-world issues solved during development included:

Infinite loop processes breaking CI pipelines

Docker Compose restart behavior

Container persistence issues

Watchtower compatibility challenges

Test import mismatches

Linting failures

Registry authentication issues

Secure credential management

Multi-platform CI differences between GitHub and GitLab

Multi-registry image publishing configuration

These challenges became valuable learning opportunities about software delivery and infrastructure operations.

🧩 Design Decisions
Why Docker Compose?
Even though the application currently contains only one service, Docker Compose was introduced early to learn:

Multi-service orchestration

Infrastructure organization

Production-oriented environments

Scalable deployment patterns

This allows the project to evolve naturally toward:

Databases

Reverse proxies

Caching services

Monitoring systems

Cloud deployments

🔥 What I Would Do Differently Starting Again
If I restarted the project today, I would:

Structure the application as a package earlier

Separate application logic from execution entry points sooner

Introduce environment variables from the beginning

Use versioned Docker tags in addition to latest

Add centralized logging strategies earlier

Add health checks from the start

Create separate development and production compose files

Introduce deployment environments sooner

However, learning progressively through mistakes was an important part of the experience.

🚀 Future Improvements
Planned future improvements include:

Linux VPS deployment

Docker Compose production deployment

Environment variable management

FastAPI integration

PostgreSQL services

Redis integration

Nginx reverse proxy

HTTPS with Let's Encrypt

AWS EC2 deployment

Health checks and service monitoring

Kubernetes orchestration

Observability and monitoring tooling

📚 Learning Philosophy
This repository reflects my belief that the best way to learn software engineering and DevOps is by building progressively more realistic systems. The focus is not perfection, but understanding:

Workflows

Infrastructure

Debugging

Automation

Deployment

Operations

Continuous improvement

Every new iteration adds complexity intentionally, allowing concepts to be learned through practical implementation rather than theory alone.

👤 Author
Erick Perez Aspiring DevOps Engineer Building hands-on experience with CI/CD, Containers, Linux, Automation, Cloud Infrastructure, and Software Delivery Pipelines 🚀
