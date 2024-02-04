pipeline {
    agent any

    stages {
        stage('Image Olusturma') {
            steps {
                script {
                    bat '\"C:\\Users\\ahgq7\\AppData\\Local\\programs\\Python\\Python312\\python.exe\" wait.py 3000'
                }
            }
        }
		
		stage ('DockerHub Yukleme'){
			steps {
				script {
					bat '\"C:\\Users\\ahgq7\\AppData\\Local\\programs\\Python\\Python312\\python.exe\" wait.py 11000'
				}
			}
		}

        stage('AWS Yukleme ') {
            steps {
                script {
                    bat '\"C:\\Users\\ahgq7\\AppData\\Local\\programs\\Python\\Python312\\python.exe\" wait.py 13000'
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
