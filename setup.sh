#!/bin/bash
set -e

usage() {
    echo "Usage: $0"
    echo "This script does not take any arguments. Execution works by just calling the script like this: ./setup.sh"
    echo "This script sets up the development environment for the project."
    echo "It performs the following tasks:"
    echo "1. Installs uv if it's not already installed."
    echo "2. Installs Docker if it's not already installed."
    echo "3. Installs required VS Code extensions if they are not already installed."
    echo "4. Sets up a virtual environment using uv."
}

install_uv() {
    # For a quick uv guide, see https://realpython.com/python-uv/
    # Check if uv is installed
    if ! command -v uv &> /dev/null
    then
        echo "uv is not installed. Installing uv..."
        curl -LsSf https://astral.sh/uv/install.sh | sh
        # add uv to PATH
        export PATH="$HOME/.local/bin:$PATH"
    fi
}

install_docker() {
    if [ ! command -v docker &> /dev/null || ! command -v docker compose &> /dev/null ];
    then
        echo "Docker or Docker Compose is not installed. Installing..."
        # Installation follows the official Docker installation guide for Ubuntu: https://docs.docker.com/engine/install/ubuntu/
        # Add Docker's official GPG key:
        # GPG keys are used to verify the authenticity of packages. By adding Docker's GPG key, you ensure that the packages you install from Docker's repository are legitimate and have not been tampered with.
        sudo apt update
        sudo apt install ca-certificates curl
        sudo install -m 0755 -d /etc/apt/keyrings
        sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
        sudo chmod a+r /etc/apt/keyrings/docker.asc

        # Add the repository to Apt sources:
        # This step adds Docker's official repository to your system's package manager (Apt). By doing this, you can easily install and update Docker using standard package management commands. The repository contains the latest stable versions of Docker, ensuring that you have access to the most recent features and security updates.
        sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

        sudo apt update
        # Install Docker Engine, CLI, and Containerd packages
        sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
        echo "Docker installed successfully."
        echo "Adding current user to the docker group to run docker without sudo."
        sudo usermod -aG docker $USER
        echo "User added to docker group."
        echo "!!! Please log out and log back in for the group changes to take effect. !!!"
        echo "In wsl you can run 'wsl --shutdown' in PowerShell to restart the WSL environment."
    else
        echo "Docker and Docker Compose are already installed."
    fi
}

install_vscode_extensions() {
    if ! command -v code &> /dev/null
    then
        echo "VS Code is not installed. Please install it to use this script."
        exit 1
    else
        echo "Checking VS Code extensions."
        # List of install extensions
        extensions=$(code --list-extensions)

        # Required extensions
        required_extensions=(
            "ms-python.python"
            "charliermarsh.ruff"
            "tamasfe.even-better-toml"
            "njpwerner.autodocstring"
        )

        # required_extensions[@] the "@" is used to expand the array and pass each element as a separate argument to the loop.
        for extension in "${required_extensions[@]}"; do
            # grep -q returns true if the pattern is found, and false otherwise. The -q option suppresses the output of grep, so it won't print anything to the terminal.
            if ! echo "$extensions" | grep -q "$extension"; then
                echo "Installing VS Code extension: $extension"
                code --install-extension "$extension"
            else
                echo "VS Code extension already installed: $extension"
            fi
        done
    fi
}

setup_venv() {
    if [ ! -d ".venv" ]; then
        echo "Setting up virtual environment using uv..."
        uv venv .venv
    fi
}

setup() {

    # Check for help flag
    if [[ "$1" == "--help" || "$1" == "-h" ]]; then
        usage
        exit 0
    fi
    
    # Initialize local setup
    install_uv
    install_docker
    install_vscode_extensions
    setup_venv
    
    echo "Setup complete! You're ready to code."
}

# Run the setup function with all arguments passed to the script
setup "$@"