properties([[$class: 'JobLocalConfiguration', changeReasonComment: ''], pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone") {
      git credentialsId: '630919f2-d46e-494d-8f5e-d2fcd7508c27', url: 'https://github.com/limorss/DevOps3006.git'
    }
    stage("show files") {
        bat "dir"
    }
}
