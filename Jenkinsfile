pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hammadnazir10/Simple-Addition.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('simple-addition-app')
                }
            }
        }
        stage('Deploy to Contabo') {
            steps {
                script {
                    sshPublisher(
                        publishers: [
                            sshPublisherDesc(
                                configName: 'contabo-server',
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: '**/Dockerfile',
                                        remoteDirectory: '/var/jenkins_home/deploy',
                                        removePrefix: '',
                                        excludes: '',
                                        flatten: false
                                    )
                                ],
                                usePromotionTimestamp: false,
                                useWorkspaceInPromotion: false,
                                verbose: true
                            )
                        ]
                    )
                    
                    // Additional stage to run commands on the server
                    sshCommand(
                        command: '''
                            cd /var/jenkins_home/deploy
                            docker build -t simple-addition-app .
                            docker run -d -p 8501:8501 simple-addition-app
                        ''',
                        remote: [name: 'contabo-server']
                    )
                }
            }
        }
    }
}
