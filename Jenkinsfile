void setBuildStatus(String message, String state) {
    step([
        $class: "GitHubCommitStatusSetter",
        reposSource: [$class: "ManuallyEnteredRepositorySource", url: "https://github.com/most-serene/sps2023/"],
        contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
        errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
        statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
    ]);
}

pipeline {
    agent any
    triggers {
        pollSCM 'H/5 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Build started"
                sh '''
                    docker compose -f docker-compose-prod.yml --env-file $JENKINS_HOME/.envvars/sps2023/.env build
                '''
                echo "Build finished"
            }
        }
        stage('Test') {
            steps {
                echo "Tests started"
                echo env.BRANCH_NAME
                sh '''
                    echo ${env.BRANCH_NAME}
                    ls
                    python3 -m venv venv
                    . venv/bin/activate
                    cd application 
                    pip install -r requirements.txt
                    python3 manage.py test
                '''
                echo "Tests finished"
            }
        }
        stage('Deliver') {
            when {
                branch "master"
            }
            steps {
                echo 'Deliver started'

                sh """
                docker container ls -a
                docker compose -f docker-compose-prod.yml --project-name sps2023 --env-file $JENKINS_HOME/.envvars/sps2023/production.env up -d --build
                docker container ls -a
                """
                
                echo 'Deliver finished'
            }
        }
    }
    post {
        always {
            // archiveArtifacts artifacts: 'services/codeExecutor/build/libs/**/*.jar', fingerprint: true
            // archiveArtifacts artifacts: 'services/projectService/build/libs/**/*.jar', fingerprint: true
            junit 'services/projectService/build/test-results/**/*.xml'
        }
        success {
            setBuildStatus("Build succeeded", "SUCCESS");
        }
        failure {
            setBuildStatus("Build failed", "FAILURE");
        }
    }
}