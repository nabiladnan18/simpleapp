pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nabiladnan18/simpleapp.git']])
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application...'
                echo 'Installing dependencies...'
                sh 'python3 -m pip install -r requirements.txt'
                echo 'Installed dependencies'
                echo 'Building complete'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing the application...'
                sh 'python3 -m pytest test_main.py'
            }
        }
        stage('Deploy') {
            echo 'Deploying the application now'
        }
    }
}
