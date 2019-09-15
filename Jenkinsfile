def withPod(body) {
  podTemplate(label: 'pod', serviceAccount: 'jenkins', containers: [
    
    containerTemplate(name: 'docker', image: 'stock-symbol', command: 'cat', 
    ttyEnabled: true),
    
    containerTemplate(name: 'kubectl', image: 'stock-symbol', 
    command: 'cat', ttyEnabled: true)
   ], 
  
  volumes: [
    hostPathVolume(mountPath: '/var/run/docker.sock',
     hostPath: '/var/run/docker.sock'),
  ]
) { body() }
}

withPod { 
  node('pod') { /*request an instance of Pod template*/
    def tag = "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    def service = "stock-symbol:${tag}"

    checkout scm /*check out the latest code from git*/

    container('docker') { /*enter Docker container*/ 
      stage('Build') { /*start new pipeline stage*/
        sh("docker build -t ${service} .") /*build Docker image*/
      }
    } 
}

def tagToDeploy = "[ecr-url]/${service}"

stage('Publish') {
  withDockerRegistry(registry: [credentialsId:'aws-ecr']) {
    sh("docker tag ${service} ${tagToDeploy}") 
    sh("docker push ${tagToDeploy}")
  }
}

stage('Deploy Stage') {
  /*use sed to replace BUILD_TAG with the Docker image name*/
  sh("sed -i.bak 's#BUILD_TAG#${tagToDeploy}#' ./deploy/staging/*.yml") ,

  container('kubectl') {
    /*apply all config. files in deploy/staging to cluster, 
    using staging namespace*/
    sh("kubectl --namespace=staging apply -f deploy/staging/") 
  }
}

stage('Release approval') {
  input message: "Release ${tagToDeploy} to production?"
}

stage('Canary deployment') {
  deploy.toKubernetes(tagToDeploy, 'canary', 'stock-symbol-canary')
  
  try {
    /*manual action is required*/
    input message: "Release ${tagToDeploy} to production?"
    } catch (Exception e) {
      deploy.rollback('stock-symbol-canary')
    }
}

stage('Deploy to production') {
  deploy.toKubernetes(tagToDeploy, 'production', 'stock-symbol')
}
