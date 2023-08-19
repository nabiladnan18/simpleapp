pipeline {
    agent any

    stages {
        // stage('Checkout') {
        //     steps {
        //         checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nabiladnan18/simpleapp.git']])
        //     }
        // }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/nabiladnan18/simpleapp'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest test_main.py'
            }
        }
    }
}
