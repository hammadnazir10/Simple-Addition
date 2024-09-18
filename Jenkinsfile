\pipeline {
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
                    // Build Docker image using the Dockerfile
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
                    def password = credentials('contabo-server-password') // Use credentials ID

                    // SSH into Contabo and deploy Docker image
                    sshPublisher(
                        publishers: [
                            sshPublisherDesc(
                                configName: 'contabo-server',
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: '**/Dockerfile', // Change this if needed
                                        remoteDirectory: '/path/to/deploy', // Adjust this path
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
