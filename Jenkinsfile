pipeline {
    agent any

    stages {
        stage('Instalar dependencias') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Tests API') {
            steps {
                sh '''
                . venv/bin/activate
                pytest tests/api
                '''
            }
        }

        stage('Tests UI Selenium') {
            steps {
                sh '''
                . venv/bin/activate
                pytest tests/ui
                '''
            }
        }
    }
}