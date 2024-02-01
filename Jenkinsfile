pipeline {
    agent any

    stages {
        stage('Image Oluşturma') {
            steps {
                script {
                    bat 'timeout /t 85'
                }
            }
        }
		
	stage {
		stage ('DockerHub Yükleme'){pipeline {
    agent any

    stage {
        stage('Image Olusturma') {
            steps {
                script {
                    bat 'timeout /t 85'
                }
            }
        }
		
	stage {
		stage ('DockerHub Yukleme'){
			steps {
				script {
					bat 'timeout /t 196'
				}
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

			steps {
				script {
					bat 'timeout /t 196'
				}
			}
		}
	}

        stage('AWSyükleme ') {
            steps {
                script {
                    bat 'timeout /t 210'
                }
            }
        }

        stage('Kubernetes Oluşturma') {
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
