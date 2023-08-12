pipeline {
    agent any
    stages {
        stage('Build') {
            parallel {
                stage('Build') {
                    steps {
                        sh 'echo "Building repo'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest test_main.py'       
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deploying the application'
                sh 'export $(cat .env | xargs) && flask run'
            }
        }
    }

    post {
		always {
			echo 'The pipeline completed'
			junit allowEmptyResults: true, testResults:'/home/nadnan/myProjects/test_reports/*.xml'
		}
		success {				
			echo "Flask application up and running!!"
		}
		failure {
			echo 'Build stage failed'
			error('Stopping early…')
		}
	}
}



