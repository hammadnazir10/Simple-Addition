pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git branch: 'main', url: 'https://github.com/hammadnazir10/Simple-Addition.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build('simple-addition-app')
                }
            }
        }
        stage('Deploy to Contabo') {
            steps {
                script {
                    // Define server details
                    def server = '157.173.119.196'
                    def user = 'root'
                    def password = 'dEivnquVA2tl2K1F'

                    // SSH into Contabo and deploy
                    sshPublisher(
                        publishers: [
                            sshPublisherDesc(
                                configName: 'contabo-server',
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: '**/Dockerfile', // Change this if you need to transfer more files
                                        remoteDirectory: '/path/to/deploy', // Adjust this path as needed
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
                }
            }
        }
    }
}
