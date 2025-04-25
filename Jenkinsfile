pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sujalgp/forest-fire-app'
    }
    

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Sujal2806/Forest-Fire-Detection.git'
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
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME
                    '''
                }
            }
        }
    }

    post {
        failure {
            echo '🚨 Build failed!'
        }
        success {
            echo '✅ Docker image built and pushed successfully!'
        }
    }
}
