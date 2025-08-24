# Jenkins Pipeline Setup Instructions

## Prerequisites

1. **Jenkins Server**: Ensure Jenkins is running with Docker support
2. **Docker Hub Account**: Create account at https://hub.docker.com
3. **GitHub Repository**: Your code should be in a GitHub repository

## Setup Steps

### 1. Configure Docker Hub Credentials in Jenkins

1. Go to Jenkins Dashboard → Manage Jenkins → Manage Credentials
2. Click on "Global" domain
3. Click "Add Credentials"
4. Select "Username with password"
5. Enter:
   - **Username**: Your Docker Hub username
   - **Password**: Your Docker Hub password (or access token)
   - **ID**: `docker-hub-credentials` (must match the Jenkinsfile)
   - **Description**: Docker Hub Credentials

### 2. Update Jenkinsfile Configuration

Before running the pipeline, update these values in the Jenkinsfile:

```groovy
environment {
    DOCKER_REPO = 'derickobeng/messaging-app'  // Your Docker Hub username
    DOCKER_REGISTRY = 'docker.io'  // Change if using different registry
}
```

### 3. Create Jenkins Pipeline Job

1. Go to Jenkins Dashboard
2. Click "New Item"
3. Enter job name (e.g., "messaging-app-pipeline")
4. Select "Pipeline"
5. Click "OK"
6. In the Pipeline section:
   - Definition: Pipeline script from SCM
   - SCM: Git
   - Repository URL: Your GitHub repository URL
   - Branch: */main (or your default branch)
   - Script Path: messaging_app/Jenkinsfile

### 4. Required Jenkins Plugins

Ensure these plugins are installed:
- Docker Pipeline
- Pipeline: Stage View
- HTML Publisher
- JUnit
- Blue Ocean (recommended)

### 5. Manual Pipeline Trigger

1. Go to your pipeline job
2. Click "Build Now"
3. Monitor the pipeline execution in Blue Ocean or Classic view

## Pipeline Stages

The pipeline includes these stages:

1. **Checkout**: Pull code from GitHub
2. **Install Dependencies**: Install Python packages and pytest
3. **Lint**: Code quality checks with pycodestyle
4. **Test**: Run pytest with coverage reports
5. **Build Docker Image**: Build and tag Docker images
6. **Security Scan**: Optional security scanning with Trivy
7. **Push Docker Image**: Push to Docker Hub (only on main/master branch)
8. **Deploy**: Deploy container locally (only on main/master branch)
9. **Integration Tests**: Test deployed application

## Environment Variables

The pipeline uses these environment variables:

- `IMAGE_NAME`: Local Docker image name
- `DOCKER_REPO`: Docker Hub repository
- `CONTAINER_NAME`: Running container name
- `HOST_PORT`/`CONTAINER_PORT`: Application ports

## Troubleshooting

### Common Issues:

1. **Docker permission denied**: Ensure Jenkins user has Docker permissions
2. **Registry push failed**: Check Docker Hub credentials
3. **Tests failing**: Review test reports in Jenkins
4. **Container won't start**: Check Docker logs

### Debug Commands:

```bash
# Check Docker images
docker images | grep messaging-app

# Check running containers
docker ps | grep messaging-app

# View container logs
docker logs messaging-app-container
```

## Reports Generated

The pipeline generates these reports:
- HTML Test Report (pytest)
- Code Coverage Report
- JUnit XML for Jenkins integration
- Docker image security scan (optional)

Access reports through Jenkins job → Build History → Select Build → Published Reports
