pipeline {
    agent any

    stages {
        stage('Git Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/soheldev/flaskapp.git'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t flask:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker rm -f flask || true
                    docker run -dit --name flask -p 5000:5000 flask:latest
                '''
            }
        }
    }
}
