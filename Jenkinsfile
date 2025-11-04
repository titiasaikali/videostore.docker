pipeline {
  agent any

  environment {
    // Full path so Local System can find it
    MINIKUBE = 'C:\\Users\\titia\\minikube.exe'

    // Prevent proxy hijacking of kubectl calls
    HTTP_PROXY  = ''
    HTTPS_PROXY = ''
    http_proxy  = ''
    https_proxy = ''
    NO_PROXY    = '127.0.0.1,localhost'
    no_proxy    = '127.0.0.1,localhost'

    DOCKER_BUILDKIT = '1'
  }

  triggers {
    // Poll GitHub every 2 minutes
    pollSCM('H/2 * * * *')
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/titiasaikali/videostore.docker'
      }
    }

    stage('Build image (Docker Desktop)') {
      steps {
        bat """
        echo === Docker info ===
        docker version
        docker build -t mydjangoapp:latest .
        docker images | find "mydjangoapp"
        """
      }
    }

    stage('Load image into Minikube') {
      steps {
        bat """
        echo === Minikube status (cluster must already be running) ===
        "%MINIKUBE%" status || (echo Minikube not running & exit /b 1)

        echo === Loading image into Minikube ===
        "%MINIKUBE%" image load mydjangoapp:latest
        """
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat """
        echo === Apply manifests ===
        "%MINIKUBE%" kubectl -- apply -f deployment.yaml --validate=false

        echo === Wait for rollout (adjust name if different) ===
        "%MINIKUBE%" kubectl -- rollout status deployment/django-deployment

        echo === Current pods & services ===
        "%MINIKUBE%" kubectl -- get pods -o wide
        "%MINIKUBE%" kubectl -- get svc
        """
      }
    }

    stage('Show Service URL') {
      steps {
        bat """
        echo === Service URL (adjust service name if needed) ===
        "%MINIKUBE%" service movie-service --url || echo Update service name if this fails
        """
      }
    }
  }
}
