pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar tests API') {
            steps {
                sh 'pytest'
            }
        }
    }

    post {
        always {
            echo 'Proceso terminado'
        }
        failure {
            echo '❌ Hay pruebas fallidas'
        }
    }
}