pipeline {
    agent any

    stages {
        stage('Image Olusturma') {
            steps {
                script {
                    bat 'python wait.py 85000'
                }
            }
        }
		
		stage ('DockerHub Yukleme'){
			steps {
				script {
					bat 'python wait.py 196000'
				}
			}
		}

        stage('AWS Yukleme ') {
            steps {
                script {
                    bat 'python wait.py 210000'
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
                bat 'python wait.py 689'
            }
        }
    }
}
