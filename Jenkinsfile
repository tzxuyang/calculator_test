pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class, branches: [[name: '*/master']] ])
            }
        stage('Build') {
            steps {
                git branch: '*/master', url: 'https://github.com/tzxuyang/calculator_test'
                sh 'python main.py'
            }
        }
        }
        stage('Test') {
            steps {
                sh 'python main.py'
            }
        }

    }
}