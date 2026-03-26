pipeline {
    agent any 

    environment {
        IMAGE_NAME = "python-url-shortener"
        CONTAINER_NAME = "url-app"
    } 

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/SaiKumar7596/python-ulr-shortner-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Tests (Container)') {
            steps {
                sh '''
                docker run --rm $IMAGE_NAME pytest
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                docker run -d -p 80:5000 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Build & Deployment Successful!"
        }
        failure {
            echo "❌ Build Failed!"
        }
    }
}
