pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/hammadnazir10/Simple-Addition.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t simple-addition-app .'
                }
            }
        }
        stage('Deploy to Contabo') {
            steps {
                sshagent(credentials: ['contabo-ssh']) {
                    sh '''
                        scp -o StrictHostKeyChecking=no simple-addition-app.tar.gz user@157.173.119.196:/home/user/
                        ssh user@157.173.119.196 "docker load -i /home/user/simple-addition-app.tar.gz && docker run -d simple-addition-app"
                    '''
                }
            }
        }
    }
}
