pipeline {
    agent any

    stages {
        stages('Image Olusturma') {
            steps {
                script {
                    bat 'timeout /t 85'
                }
            }
        }
		
	stages {
		stages ('DockerHub Yukleme'){
			steps {
				script {
					bat 'timeout /t 196'
				}
			}
		}
	}

        stages('AWS Yukleme ') {
            steps {
                script {
                    bat 'timeout /t 210'
                }
            }
        }

        stages('Kubernetes Olusturma') {
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
