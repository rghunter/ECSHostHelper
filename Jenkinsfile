#!/usr/bin/env groovy
node('docker'){ 
    stage 'Building image'
        checkout scm 
        def image = docker.build "ECSHostHelper:${env.BUILD_TAG}" 
    stage 'Push Image'
        docker.withRegistry("https://490553117019.dkr.ecr.us-east-1.amazonaws.com") {
            if (env.BRANCH_NAME == 'master') {
                image.push("${env.BUILD_NUMBER}")
                image.push("latest")
            }else {
                image.push("${env.BUILD_TAG}")
            }
        }
}
