pipeline {
    agent any

    stages {
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