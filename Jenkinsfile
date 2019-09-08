pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') { 
            steps { 
                sh 'echo testing Build' 
            }
        }
        stage('Test'){
            steps {
                sh 'echo testing Test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo testing Deploy'
            }
        }
    }
}
