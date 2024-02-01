pipeline {
    agent any

    stages {
        stages('Image Oluşturma') {
            steps {
                script {
                    bat 'timeout /t 85'
                }
            }
        }
		
	stages {
		stages ('DockerHub Yükleme'){
			steps {
				script {
					bat 'timeout /t 196'
				}
			}
		}
	}

        stages('AWSyükleme ') {
            steps {
                script {
                    bat 'timeout /t 210'
                }
            }
        }

        stages('Kubernetes Oluşturma') {
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
