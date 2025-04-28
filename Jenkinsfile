pipeline {
    agent any

    stages {
        stage('🔄 Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('🐳 Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                }
            }
        }

        stage('🛠️ Build Docker Image') {
            steps {
                sh "docker build -t sujalgp/forest-fire-app ."
            }
        }

        stage('🚀 Push Docker Image') {
            steps {
                sh "docker push sujalgp/forest-fire-app"
            }
        }
    }
    post {
        always {
            echo '✅ Pipeline completed.'
        }
    }
}
