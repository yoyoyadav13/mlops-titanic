pipeline {
    agent any

    stages {
        stage('Verify Git Version') {
            steps {
                script {
                    def gitVersion = sh(script: 'git --version', returnStdout: true).trim()
                    echo "Git version: ${gitVersion}"
                }
            }
        }
        stage('Clone Repository') {
            steps {
                script {
                    // Clone your repository
                    sh 'git clone https://github.com/yourusername/your-repo.git'  // Replace with your repo URL
                }
            }
        }
        stage('Setup Environment') {
            steps {
                echo 'Setting up environment...'
                sh 'pip install -r requirements.txt'  // Install dependencies
            }
        }
        stage('Data Preprocessing') {
            steps {
                echo 'Running data preprocessing...'
                sh 'python preprocess.py'  // Run your preprocessing script
            }
        }
        stage('Train Model') {
            steps {
                echo 'Training the model...'
                sh 'python train.py'  // Run your training script
            }
        }
        stage('Deploy Model') {
            steps {
                echo 'Deploying the model...'
                sh 'python deploy.py'  // Run your deployment script
            }
        }
    }
}