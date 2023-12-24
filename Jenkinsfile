pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "checking out the git repo"
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/tzxuyang/calculator_test']] ])
            }
        }
        stage('Install'){
            steps {
                echo "install default lib"
                sh "apt install python3-pandas"
            }
        }
        stage('Build') {
            steps {
                // git branch: '*/master', url: 'https://github.com/tzxuyang/calculator_test'
                echo "run python main code"
                sh 'python3 main.py'
            }
        }
        stage('Test') {
            steps {
                echo "run python main code"
                sh 'python3 test.py'
            }
        }

    }
}
