### **Prompt for New Context Window**

I am working on a project that integrates a **custom GPT** with a dynamic API to assist with various development tasks in a highly interactive and extensible manner. The goal is to enable ChatGPT to interact with a project environment, perform file and database operations, extend its own functionality by adding new API endpoints, and ensure all changes are version-controlled via GitHub. Here's the detailed explanation:

---

### **Project Purpose**

The purpose of this system is to create an environment where a custom GPT can:

1. **Access Project Files**:
   - Open, read, modify, and create files dynamically within a project environment.

2. **Perform File Operations**:
   - Execute tasks like combining files, searching content, or compressing directories using Bash scripts.

3. **Run Database Queries**:
   - Send SQL commands to a connected database and retrieve results securely.

4. **Extend the API Dynamically**:
   - Add new API endpoints and scripts at runtime to enhance its capabilities, allowing the GPT to adapt to the project needs.

5. **Version Control with GitHub**:
   - Push all changes (scripts and API extensions) to a GitHub repository to ensure reusability across projects.

6. **Secure Execution**:
   - Run all operations in a secure, Dockerized environment to isolate the project and prevent unintended system-level changes.

---

### **System Overview**

This system comprises the following components:

1. **Dynamic API**:
   - A FastAPI-based Python application that exposes endpoints for file operations, script execution, and GitHub integration.

2. **Scripts Folder**:
   - A directory (`scripts`) where Bash scripts are stored and managed. These scripts perform specific tasks and are accessible via the API.

3. **GitHub Integration**:
   - The system clones a predefined GitHub repository into the project environment and synchronizes any changes (pull, commit, push) using Git.

4. **Docker Environment**:
   - The entire setup runs in a Docker container, ensuring a secure and isolated environment. The project folder is mounted into the container, so changes persist outside the container.

5. **Setup Script**:
   - A comprehensive Bash script (`setup_dynamic_api.sh`) automates the entire setup process, including project folder creation, file generation, GitHub repository initialization, Docker container setup, and API deployment.

---

### **Workflow**

1. **Setup**:
   - The `setup_dynamic_api.sh` script guides you through:
     - Creating a GitHub repository.
     - Generating project files (`main.py`, `Dockerfile`, `docker-compose.yml`, sample scripts).
     - Initializing a Git repository, committing files, and pushing them to GitHub.
     - Building and running the Docker container.

2. **Usage**:
   - Access the API at `http://localhost:8000` and use the following endpoints:
     - `GET /list-scripts`: List all available scripts in the `scripts` folder.
     - `POST /run-script`: Execute a specific script with optional arguments.
     - `POST /git-sync`: Synchronize the `scripts` folder with the GitHub repository.

3. **Custom GPT Integration**:
   - A custom GPT uses the API's OpenAPI schema to interact with the project, enabling it to:
     - Dynamically execute tasks.
     - Extend its functionality by adding new API endpoints.
     - Collaborate on the project by automating repetitive tasks and providing intelligent suggestions.

4. **Version Control**:
   - All updates (new scripts, API extensions) are committed and pushed to GitHub, ensuring a reusable and versioned workflow.

---

### **Features**

1. **Dynamic API**:
   - Supports real-time addition of new API endpoints, allowing the GPT to extend its functionality.

2. **Script Execution**:
   - Executes predefined or newly added Bash scripts securely within the project environment.

3. **GitHub Synchronization**:
   - Maintains a centralized repository for all scripts and API changes, ensuring consistency and reusability.

4. **Secure Environment**:
   - Dockerized setup isolates the project environment, ensuring safe execution of scripts and operations.

---

### **Key Files and Their Purpose**

1. **`main.py`**:
   - The FastAPI application that provides the dynamic API.
   - Includes endpoints for script management, Git synchronization, and custom functionality.

2. **`Dockerfile`**:
   - Defines the Docker image for the API, including dependencies like Python, Git, and SSH.

3. **`docker-compose.yml`**:
   - Manages the Docker container setup, including port mapping and script folder mounting.

4. **`scripts/`**:
   - Contains Bash scripts for performing tasks like file operations, database queries, or custom automations.

5. **`.ssh/`**:
   - Stores your SSH keys, enabling the container to perform Git operations securely.

6. **`setup_dynamic_api.sh`**:
   - Automates the entire setup process, guiding the user step-by-step to initialize the project, connect to GitHub, and deploy the API.

---

### **What I Need in This Context**

1. **Understanding of the System**:
   - Recognize that this system is designed to integrate ChatGPT with a project environment dynamically and securely.

2. **Ability to Extend**:
   - Help me refine or extend this system further, such as improving security, adding new features, or optimizing performance.

3. **OpenAPI Schema**:
   - Generate a schema for the API endpoints to provide to the custom GPT for seamless integration.

4. **Documentation**:
   - Ensure everything is well-documented for clarity and ease of use, especially for future reuse or sharing with others.

5. **Suggestions**:
   - Provide any suggestions or improvements to make this system more robust, versatile, or efficient.

---

This prompt sets the context for what we’re building and ensures the new context window is fully informed of the project’s goals and current progress. Let me know if you'd like further refinements!