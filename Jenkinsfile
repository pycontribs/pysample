pipeline {
  agent {
    node {
      label 'master'
    }
    
  }
  stages {
    stage('lint') {
      steps {
        parallel(
          "py27": {
            sh 'tox -epy27'
            
          },
          "py26": {
            sh 'tox -epy26'
            
          }
        )
      }
    }
    stage('publish') {
      steps {
        echo 'Hurrah!'
      }
    }
  }
  environment {
    TERM = 'dumb'
  }
}