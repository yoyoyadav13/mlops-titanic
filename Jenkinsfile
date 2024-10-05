pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/master']],
                    userRemoteConfigs: [[
                        url: 'git@github.com:yoyoyadav13/mlops-titanic.git',
                        credentialsId: 'github-credentials'  // Use your GitHub credentials ID here
                    ]]
                ])
            }
        }
        stage('Data Preprocessing') {
            steps {
                // Your data preprocessing steps
            }
        }
        stage('Train Model') {
            steps {
                // Your model training steps
            }
        }
    }
}
