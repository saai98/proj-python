pipeline {
    agent any

    tools {
        // Ensure this matches the SonarScanner name in Global Tool Configuration
        sonarQubeScanner 'SonarScanner'
    }

    environment {
        // Optional: You can also move credentials to Jenkins Secrets and use them securely
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/saai98/proj-python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    pytest tests/
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('MySonarQubeServer') {
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=My-Python-App \
                          -Dsonar.sources=. \
                          -Dsonar.python.version=3 \
                          -Dsonar.login=${SONAR_AUTH_TOKEN}
                    '''
                }
            }
        }
    }
}

