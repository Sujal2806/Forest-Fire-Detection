pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "sujalgp/forest-fire-app"
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'
    }
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Sujal2806/Forest-Fire-Detection.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }
        stage('Test') {
            steps {
                echo '✅ Skipping unit tests (can add test_model.py later)'
            }
        }
        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        docker.image(DOCKER_IMAGE).push('latest')
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop forest-app || true'
                sh 'docker rm forest-app || true'
                sh "docker run -d -p 8501:8501 --name forest-app ${DOCKER_IMAGE}:latest"
            }
        }
    }
}
