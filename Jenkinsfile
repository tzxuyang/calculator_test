pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/tzxuyang/calculator_test']] ])
            }
        }
        stage('Build') {
            steps {
                git branch: '*/master', url: 'https://github.com/tzxuyang/calculator_test'
                sh 'python main.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python'
            }
        }

    }
}