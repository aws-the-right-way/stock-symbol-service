pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') { 
            steps { 
                sh 'echo testing Build'
                sh 'sleep 128s'
            }
        }
        stage('Publish') {
            steps {
                sh 'echo testing Publish'
                sh 'sleep 36s'
            }
        }
        stage('Deploy Stage') {
            steps {
                sh 'echo testing Deploy Stage'
                sh 'sleep 286s'
            }
        }
        stage('Release approval') {
            steps {
                sh 'echo testing Release approval'
                sh 'sleep 9s'
            }
        }
        stage('Canary deployment') {
            steps {
                sh 'echo testing Canary'
                sh 'sleep 313s'
            }
        }
        stage('Deploy to production') {
            steps {
                sh 'echo testing Deploy Prod'
                sh 'sleep 378s'
            }
        }
    }
}
