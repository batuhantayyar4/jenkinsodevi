pipeline {
    agent any

    environment {
        // ECR ve Kubernetes ayarları
        REGISTRY_URL = '992382515999.dkr.ecr.us-east-1.amazonaws.com'
        IMAGE_NAME = 'odev'
        TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t %IMAGE_NAME% .'
                }
            }
        }

        stage('Push to AWS ECR') {
            steps {
                script {
                    withAWS(credentials: 'aws-credentials', region: 'us-east-1') {
                        bat 'aws ecr get-login-password | docker login --username AWS --password-stdin %REGISTRY_URL%'
                        bat 'docker tag %IMAGE_NAME%:%TAG% %REGISTRY_URL%/%IMAGE_NAME%:%TAG%'
                        bat 'docker push %REGISTRY_URL%/%IMAGE_NAME%:%TAG%'
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                        bat 'kubectl set image deployment/my-app-deployment odev=%REGISTRY_URL%/%IMAGE_NAME%:%TAG%'
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                bat 'docker rmi %IMAGE_NAME%'
            }
        }
    }
}
