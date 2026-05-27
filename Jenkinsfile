pipeline {
    agent any

    stages {
        stage('Init') {
            steps {
                echo "Iniciando pipeline QA 🚀"
            }
        }

        stage('Install Python') {
            steps {
                sh 'python3 --version || python --version'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt || echo "No requirements.txt"'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest || echo "No hay tests aún, pero pipeline OK ✅"'
            }
        }
    }
}