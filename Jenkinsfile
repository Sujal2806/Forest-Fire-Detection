pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = 'sujalgp/forest-fire-detection'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-creds', url: 'https://github.com/Sujal2806/Forest-Fire-Detection.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "echo $DOCKER_HUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB_CREDENTIALS_USR --password-stdin"
                    sh "docker push $IMAGE_NAME"
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    sh "docker rmi $IMAGE_NAME"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
    }
}
