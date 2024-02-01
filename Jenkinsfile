pipeline {
    agent any

    stages {
        stage('Image Olusturma') {
            steps {
                script {
                    bat 'timeout /t 85'
                }
            }
        }
		
		stage ('DockerHub Yukleme'){
			steps {
				script {
					bat 'timeout /t 196'
				}
			}
		}

        stage('AWS Yukleme ') {
            steps {
                script {
                    bat 'timeout /t 210'
                }
            }
        }

        stage('Kubernetes Olusturma') {
            steps {
                script {
					bat 'asdhjahsjhjsd ajshashd'
                }
            }
        }
    }

    post {
        always {
            script {
                bat 'ping 127.0.0.1 -n 1 -w 689> nul'
            }
        }
    }
}
