# 🚀 Python CI/CD & Docker Deployment Practice Project

📅 Started: 06/23/2026

This repository documents my transition from writing isolated Python exercises to building and operating a small real-world software delivery pipeline.

The goal of this project is not to create a large Python application, but to understand how modern software is developed, tested, containerized, validated, deployed, and automatically updated using real DevOps workflows.

---

# 🎯 Project Goals

This project was created to practice:

- Real CI/CD workflows
- Automated testing pipelines
- Docker containerization
- Container registries
- Deployment automation
- Infrastructure concepts
- Service persistence and recovery
- Multi-platform CI environments

Instead of focusing exclusively on application complexity, this repository focuses on the **software delivery lifecycle**.

---

# 🧠 What This Project Demonstrates

This project currently includes:

✅ Python application development  
✅ Unit testing with pytest  
✅ Automated linting and formatting validation  
✅ GitHub Actions CI pipelines  
✅ GitLab CI/CD pipelines  
✅ Docker image creation  
✅ Docker Hub registry integration  
✅ Docker Compose orchestration  
✅ Automatic container restart policies  
✅ Automatic container updates with Watchtower  
✅ Continuous Deployment (CD) simulation

---

# 🏗️ Current Architecture


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
Docker Hub Registry
        ↓
Watchtower detects updates
        ↓
Docker Compose recreates container
        ↓
Updated application running

----------

# 🛠️ Technologies Used
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
Watchtower
Development Tools
Git
Git Bash
Visual Studio Code

# 📦 Why Docker Was Added

Originally, the project only consisted of a simple Python application and unit tests.

As the learning process evolved, Docker was introduced to understand:

portable environments
container lifecycle management
image registries
production-like deployments
deployment automation

The objective was to simulate how modern applications move from development into production environments.

# 🔄 CI/CD Workflow

Every push or pull request triggers automated validation pipelines.

The workflow currently performs:

Source checkout
Python environment setup
Dependency installation
flake8 lint validation
black formatting validation
pytest execution
Docker image build
Push to Docker Hub

Once the image reaches Docker Hub, Watchtower automatically detects the new version and recreates the running container.

This creates a simplified Continuous Deployment flow.

# 🧠 Key Concepts Learned

Throughout this project I learned:

Difference between CI and CD
Why containers matter
How Docker images differ from containers
Why registries are important
Why production services should run detached
How restart policies work
How container orchestration begins with Docker Compose
How deployment automation works
Why observability and logs matter
How automated deployments detect and apply updates

# ⚠️ Challenges Encountered

Some of the real problems solved during development included:

Infinite loop processes breaking CI pipelines
Docker Compose restart behavior
Container persistence issues
API compatibility issues with Watchtower
Test import mismatches
Linting failures
Managing Docker Hub credentials securely
Multi-platform CI differences between GitHub and GitLab

These issues became valuable learning opportunities about real software operations.

# 🧩 Design Decisions
Why Docker Compose?

Even though the application currently contains only one service, Docker Compose was intentionally introduced early to learn:

multi-service orchestration
infrastructure structure
production-like environments
scalable deployment patterns

This allows the project to grow naturally into:

databases
reverse proxies
caching services
monitoring systems
cloud deployments


# 🔥 What I Would Do Differently Starting Again

If I restarted the project today, I would:

Structure the application as a package earlier
Separate application logic from execution entrypoints sooner
Introduce environment variables from the beginning
Use versioned Docker tags instead of only latest
Add logging strategies earlier
Add health checks to containers
Create development and production compose files separately

However, learning progressively through mistakes was an important part of the experience.

# 🚀 Future Improvements

Planned future improvements include:

GitHub Container Registry integration
GitLab Container Registry integration
Multi-registry image publishing
FastAPI integration
PostgreSQL services
Redis integration
Nginx reverse proxy
Remote VPS deployment
AWS EC2 deployment
Kubernetes orchestration
Monitoring and observability tooling


# 📚 Learning Philosophy

This repository reflects my belief that the best way to learn software engineering is by building progressively more realistic systems.

The focus is not perfection, but understanding:

workflows
infrastructure
debugging
iteration
automation
deployment lifecycle


# 👤 Author
Erick Perez

Junior Python Developer
Learning DevOps, CI/CD, Containers, and Cloud Infrastructure 🚀
