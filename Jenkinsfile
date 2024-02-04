pipeline {
    agent any

    stages {
        stage('Image Olusturma') {
            steps {
                script {
                    bat '\"C:\\Users\\ahgq7\\AppData\\Local\\programs\\Python\\Python312\\python.exe\" wait.py 4000'
                }
            }
        }
		
		stage ('DockerHub Yukleme'){
			steps {
				script {
					bat '\"C:\\Users\\ahgq7\\AppData\\Local\\programs\\Python\\Python312\\python.exe\" wait.py 9000'
				}
			}
		}

        stage('AWS Yukleme ') {
            steps {
                script {
                    bat '\"C:\\Users\\ahgq7\\AppData\\Local\\programs\\Python\\Python312\\python.exe\" wait.py 12000'
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
                bat '\"C:\\Users\\ahgq7\\AppData\\Local\\programs\\Python\\Python312\\python.exe\" wait.py 689'
            }
        }
    }
}
