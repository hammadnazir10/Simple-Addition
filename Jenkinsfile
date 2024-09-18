pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'simple-addition-app'
        CONTAINER_NAME = 'simple-addition-container'
        CONTAINER_PORT = '8501'
        CONTAINER_HOST = '157.173.119.196' // Replace with your actual server IP or hostname
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hammadnazir10/Simple-Addition.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Deploy to Contabo') {
            steps {
                sshagent(['ccd']) { // Ensure SSH credentials are added in Jenkins
                    script {
                        // Use SSH to deploy the Docker container
                        sh """
                        ssh -o StrictHostKeyChecking=no user@${CONTAINER_HOST} << EOF
                            docker pull ${DOCKER_IMAGE} || true
                            docker stop ${CONTAINER_NAME} || true
                            docker rm ${CONTAINER_NAME} || true
                            docker run -d --name ${CONTAINER_NAME} -p ${CONTAINER_PORT}:${CONTAINER_PORT} ${DOCKER_IMAGE}
                        EOF
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
