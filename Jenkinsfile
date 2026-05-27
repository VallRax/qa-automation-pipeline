pipeline {
    agent {
        docker {
            image 'qa-automation-pipeline'
            build true
        }
    }

    stages {
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