pipeline {
    agent any

    stages {
        stage('Instalar dependencias') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Tests API') {
            steps {
                sh 'pytest tests/api'
            }
        }

        stage('Tests UI Selenium') {
            steps {
                sh 'pytest tests/ui'
            }
        }
    }
}