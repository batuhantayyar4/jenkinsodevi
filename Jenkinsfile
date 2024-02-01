pipeline {
    agent any

    environment {
        URL = '891377282272.dkr.ecr.us-east-1.amazonaws.com'
        IMAGE = 'awscontainer'
        VERSION = 'latest'
    }

    stages {
        stages('Image Oluşturma') {
            steps {
                script {
                    bat 'docker build -t oziwankenobi/%IMAGE% .'
                }
            }
        }
		
	stages {
		stages ('DockerHub Yükleme'){
			steps {
				script {
					bat 'docker push oziwankenobi/%IMAGE%'
				}
			}
		}
	}

        stages('AWSyükleme ') {
            steps {
                script {
                    withAWS(credentials: 'aws-login', region: 'us-east-1') {
                        bat 'aws ecr get-login-password | docker login --username AWS --password-stdin %URL%'
                        bat 'docker VERSION %IMAGE%:%VERSION% %URL%/%IMAGE%:%VERSION%'
                        bat 'docker push %URL%/%IMAGE%:%VERSION%'
                    }
                }
            }
        }

        stages('Kubernetes Oluşturma') {
            steps {
                script {
					withCredentials([file(credentialsId: 'conffile', variable: 'KUBECONFIG')]) {
						bat 'kubectl set image deployment/awsdeployment awsodev=%URL%/%IMAGE%:%VERSION%'
					}
                }
            }
        }
    }

    post {
        always {
            script {
                bat 'docker rmi %IMAGE%'
            }
        }
    }
}
