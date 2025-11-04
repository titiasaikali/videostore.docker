pipeline {
  agent any
  environment {
    IMAGE = "movies-app:latest"
    CONTAINER = "movies-app"
    PORT = "8000"
  }
  stages {
    stage('Checkout') {
      steps {
        cleanWs()
        git branch: 'main', url: 'https://github.com/titiasaikali/videostore.docker.git'
      }
    }
    stage('Build Docker Image') {
      steps { sh 'docker build -t $IMAGE .' }
    }
    stage('Stop old container') {
      steps { sh 'docker rm -f $CONTAINER || true' }
    }
    stage('Run new container') {
      steps { sh 'docker run -d --name $CONTAINER -p $PORT:$PORT $IMAGE' }
    }
  }
  post { success { echo "Deployed at http://localhost:${PORT}" } }
}

