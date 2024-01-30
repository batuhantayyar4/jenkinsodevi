pipeline {
    agent any

    environment {
        // ECR ve Kubernetes ayarları
        REGISTRY_URL = '992382515999.dkr.ecr.us-east-1.amazonaws.com/odev'
        IMAGE_NAME = 'my-app'
        TAG = 'latest'

        // Jenkins Credential Manager'da saklanan kimlik bilgilerini kullan
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                // Docker imajını oluştur
                script {
                    bat 'docker build -t %IMAGE_NAME% .'
                }
            }
        }

        stage('Push to AWS ECR') {
            steps {
                // AWS kimlik doğrulaması yap
                script {
                    withEnv(['AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY']) {
                        bat '(aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin %REGISTRY_URL%)'
                    }
                }
                // ECR'ye Docker imajını gönder
                script {
                    bat 'docker tag %IMAGE_NAME%:%TAG% %REGISTRY_URL%/%IMAGE_NAME%:%TAG%'
                    bat 'docker push %REGISTRY_URL%/%IMAGE_NAME%:%TAG%'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Kubernetes'e dağıtım yap
                script {
                    bat 'kubectl set image deployment/my-app-deployment my-app=%REGISTRY_URL%/%IMAGE_NAME%:%TAG%'
                }
            }
        }
    }

    post {
        always {
            // Her durumda çalışacak temizlik adımları
            script {
                // Örneğin Docker imajlarını temizle
                bat 'docker rmi %IMAGE_NAME%'
            }
        }
    }
}
