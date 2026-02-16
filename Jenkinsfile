pipeline {
    agent any

    environment {
        APP_NAME = "fruit-shop"
        APP_PORT = "5000"
        GIT_URL = "https://github.com/nganesh2425-bit/fruit-shop.git"  // replace with your repo
        GIT_BRANCH = "main"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "Pulling latest code from main branch..."
                git branch: "${GIT_BRANCH}", url: "${GIT_URL}"
            }
        }

        stage('Deploy Application') {
            steps {
                echo "Building and redeploying with Docker Compose..."
                sh """
                    docker-compose down || true
                    docker-compose up -d --build
                """
            }
        }
    }

    post {
        success {
            echo "✅ Application redeployed successfully on branch ${GIT_BRANCH}"
        }
        failure {
            echo "❌ Deployment failed. Check logs."
        }
    }
}

