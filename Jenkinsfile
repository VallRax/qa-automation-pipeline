pipeline {
    agent any

    stages {
        stage('Clonar código') {
            steps {
                git 'https://github.com/VallRax/qa-automation-pipeline.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Ejecutar tests API') {
            steps {
                sh 'pytest tests/test_api.py -v'
            }
        }

        stage('Ejecutar tests UI (Selenium)') {
            steps {
                sh 'pytest tests/test_ui.py -v'
            }
        }
    }

    post {
        success {
            echo '✅ Todo pasó correctamente'
        }
        failure {
            echo '❌ Hay pruebas fallidas'
        }
    }
}