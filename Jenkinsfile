pipeline {
  agent any

  environment {
    // adjust if minikube.exe is in a different folder
    MINIKUBE = 'C:\\Users\\titia\\minikube.exe'
    // make sure kubectl can read your local kubeconfig
    KUBECONFIG = 'C:\\Users\\titia\\.kube\\config'

    // prevent proxies from hijacking kubectl -> Jenkins login page
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

    stage('Ensure Minikube Up') {
      steps {
        bat """
        "%MINIKUBE%" status || "%MINIKUBE%" start --driver=docker
        """
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        bat """
        REM === Point Docker CLI to Minikube's daemon ===
        call "%MINIKUBE%" docker-env --shell=cmd > docker_env.bat
        call docker_env.bat

        REM === Build image inside Minikube Docker ===
        docker build -t mydjangoapp:latest .
        """
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat """
        REM === Apply manifests using Minikube's kubectl ===
        "%MINIKUBE%" kubectl -- apply -f deployment.yaml --validate=false

        REM === Wait for rollout (deployment name must match your YAML) ===
        "%MINIKUBE%" kubectl -- rollout status deployment/django-deployment

        REM === Show services/pods for debugging ===
        "%MINIKUBE%" kubectl -- get pods -o wide
        "%MINIKUBE%" kubectl -- get svc
        """
      }
    }

    stage('Show Service URL') {
      steps {
        bat """
        REM This prints the NodePort URL if available
        "%MINIKUBE%" service movie-service --url || echo (If this fails, check service name)
        """
      }
    }
  }
}
