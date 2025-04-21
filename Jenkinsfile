pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/saai98/proj-python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
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
                          -Dsonar.host.url=http://65.2.141.49:9000 \
                          -Dsonar.login=sqp_862bfe8dad631d86dc9e24edbc91ea336c5a4fae
                    '''
                }
            }
        }
    }
}

