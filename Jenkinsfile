void setBuildStatus(String message, String state) {
    step([
        $class: "GitHubCommitStatusSetter",
        reposSource: [$class: "ManuallyEnteredRepositorySource", url: "https://github.com/most-serene/sps2023/"],
        contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
        errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
        statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
    ]);
}

void setBuildBadge(String apiKey, String projectId, String status) {
    httpRequest contentType: "APPLICATION_JSON", httpMode: "POST", ignoreSslErrors: true,
        requestBody: JsonOutput.toJson([status: status, api_key: apiKey]), url: "https://217.160.40.42:45001/projects/" + projectId
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
                echo env.BRANCH_NAME
                sh """
                    cp $JENKINS_HOME/.envvars/sps2023/djangoProd.env moviesApp/.env
                    BRANCH=${env.BRANCH_NAME} docker compose -f docker-compose-prod.yml --env-file $JENKINS_HOME/.envvars/sps2023/.env build
                """
                echo "Build finished"
            }
        }
        stage('Test') {
            steps {
                echo "Tests started"
                echo env.BRANCH_NAME
                sh """
                    ls
                    python3 -m venv venv
                    . venv/bin/activate
                    cd moviesApp 
                    pip install -r requirements.txt
                    python3 manage.py test
                """
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
                BRANCH=${env.BRANCH_NAME} docker compose -f docker-compose-prod.yml --project-name sps2023 --env-file $JENKINS_HOME/.envvars/sps2023/production.env up -d --build
                docker container ls -a
                """
                
                echo 'Deliver finished'
            }
        }
    }
    post {
        success {
            setBuildStatus("Build succeeded", "SUCCESS");
            script {
                if (env.BRANCH_NAME == 'master') {
                    withEnv(readFile("$JENKINS_HOME/.envvars/sps2023/jenkinsEnv.txt").split('\n') as List) {
                        setBuildBadge(env.API_KEY, "3", "success");
                    }
                }
            }
        }
        failure {
            setBuildStatus("Build failed", "FAILURE");
            script {
                if (env.BRANCH_NAME == 'master') {
                    withEnv(readFile("$JENKINS_HOME/.envvars/sps2023/jenkinsEnv.txt").split('\n') as List) {
                        setBuildBadge(env.API_KEY, "3", "failed");
                    }
                }
            }
        }
    }
}