pipeline {
  agent any

  environment {
    // adjust if minikube.exe is elsewhere
    MINIKUBE          = 'C:\\Users\\titia\\minikube.exe'
    // your user’s minikube + kubeconfig paths
    MINIKUBE_HOME     = 'C:\\Users\\titia\\.minikube'
    KUBECONFIG        = 'C:\\Users\\titia\\.kube\\config'
    MINIKUBE_PROFILE  = 'minikube'   // change if your profile has a different name

    // keep kubectl from being proxied to Jenkins
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

    stage('Verify Minikube (must already be running)') {
      steps {
        bat """
        "%MINIKUBE%" -p "%MINIKUBE_PROFILE%" status || (echo Minikube not running & exit /b 1)
        """
      }
    }

    stage('Build image (Docker Desktop)') {
      steps {
        bat """
        docker version
        docker build -t mydjangoapp:latest .
        docker images | find "mydjangoapp"
        """
      }
    }

    stage('Load image into Minikube') {
      steps {
        bat """
        "%MINIKUBE%" -p "%MINIKUBE_PROFILE%" image load mydjangoapp:latest
        """
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat """
        "%MINIKUBE%" -p "%MINIKUBE_PROFILE%" kubectl -- apply -f deployment.yaml --validate=false
        "%MINIKUBE%" -p "%MINIKUBE_PROFILE%" kubectl -- rollout status deployment/django-deployment
        "%MINIKUBE%" -p "%MINIKUBE_PROFILE%" kubectl -- get pods -o wide
        "%MINIKUBE%" -p "%MINIKUBE_PROFILE%" kubectl -- get svc
        """
      }
    }

    stage('Show Service URL') {
      steps {
        bat """
        "%MINIKUBE%" -p "%MINIKUBE_PROFILE%" service movie-service --url || echo Update service name if needed
        """
      }
    }
  }
}
