</> groovy

pipeline {
    agent any 

    environment {
         IMAGE_NAME = "python-url-shortner"
	 EC2_IP = "YOUR_EC2_IP"
       
     } 


     stages {


         stage('Clone Code') {
	     steps {
	         git 'https://github.com/SaiKumar7596/python-ulr-shortner-app.git'

	      }

	  }


	 stage('Install Dependencies') {
	     steps {
	         sh 'pip insytall -r requirements.txt'

             }

	   }

          stage('Run Tests') {
	      steps {

	          sh 'pytest'
	       }

	   }

	   stage('Build Docker Image') {
	       steps {
	           sh 'docker build -t $IMAGE_NAME .'
	       }
	   }

	   stage('Deploy to EC2') {
            steps {
                sh '''
                ssh -o StrictHostKeyChecking=no ubuntu@$EC2_IP << EOF
                docker stop url-app || true
                docker rm url-app || true
                docker run -d -p 80:5000 --name url-app $IMAGE_NAME
                EOF
                '''
            }
        }
    }
}
