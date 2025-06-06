pipeline {
    agent any
    triggers {
        githubPush()
    }
    environment {
        DOCKER_IMAGE_NAME = 'calc'
        GITHUB_REPO_URL = 'https://github.com/Ashutosh-Jadhav/mini_proj_calc.git'
    }

    stages {
        stage('checkout') {
            steps {
                script {
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }

        stage('test') {
            steps {
                script {
                    sh 'python3 -m unittest test.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}" , "--no-cache .")
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script{
                    docker.withRegistry('' , 'DockerHubCred') {
                        sh 'docker tag calc ashutoshj/calc:latest'
                        sh 'docker push ashutoshj/calc'
                    }
                }
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                script {
                    withEnv(["ANSIBLE_HOST_KEY_CHECKING=False"]) {
                        ansiblePlaybook(
                            playbook: 'deploy.yml',
                            inventory: 'inventory'
                        )
                    }
                }
            }
        }
    }

    post {
        success{
            mail to: 'ashutosh.j001@gmail.com',
            subject: "Application Deployment SUCCESS: Build ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: "The build was successful!"
        }
        failure {
            mail to: 'ashutosh.j001@gmail.com',
            subject: "Application Deployment FAILURE: Build ${env.JOB_NAME} #{env.BUILD_NUMBER}",
            body: "The build failed."
        }
        always {
            cleanWs()
        }
    }

}
