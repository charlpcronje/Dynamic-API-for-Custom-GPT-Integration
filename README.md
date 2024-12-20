# Dynamic API for Custom GPT Integration

## Purpose

The purpose of this system is to provide **ChatGPT** with direct access to a project environment, enabling it to perform tasks like:

- **Viewing and editing files**: Open, read, update, and create project files dynamically.
- **Running database queries**: Execute SQL commands securely and get results in real-time.
- **Executing file operations**: Combine files, search for content, compress directories, and perform other file manipulations.
- **Extending its own functionality**: Dynamically add new API endpoints and scripts, allowing ChatGPT to enhance its capabilities in real-time.

This system creates a highly interactive development environment where a **custom GPT** can:
- Collaborate on projects as an advanced assistant.
- Automate repetitive tasks.
- Evolve its functionality by extending the API to meet the specific needs of the project.

---

## How It Works

The system leverages a **Dockerized API** that integrates with a **GitHub repository** to manage project scripts and changes. Here's how it functions:

1. **Base API**:
   - A pre-configured FastAPI application exposes endpoints that allow ChatGPT to interact with your project.
   - The API can:
     - List and execute predefined scripts stored in the project.
     - Synchronize with a GitHub repository to keep scripts and changes version-controlled.

2. **Dynamic Extensions**:
   - ChatGPT can dynamically add new endpoints to the API by uploading code or scripts.
   - These new functionalities are versioned and pushed to the GitHub repository automatically, making them available for future projects.

3. **Docker Environment**:
   - The entire system runs in an isolated Docker container, ensuring security and portability.
   - The project folder is mounted into the container, allowing changes to persist while keeping the system sandboxed.

4. **GitHub Integration**:
   - Scripts and API changes are stored in a GitHub repository.
   - The system ensures all updates are committed and pushed, providing a history of changes and enabling reuse across projects.

---

## Final Functionality

This system allows ChatGPT to function as a **project-aware assistant** by:

1. **Accessing Project Files**:
   - ChatGPT can open, read, and modify project files securely within the API.

2. **Executing Project-Specific Tasks**:
   - Scripts can perform complex operations, such as file combinations, database queries, or custom automation.

3. **Adding New Capabilities**:
   - ChatGPT can upload new scripts or API endpoints to extend its functionality dynamically.

4. **Maintaining a Versioned API**:
   - The GitHub integration ensures every change is tracked, reusable, and shareable across different projects.

5. **Secure Collaboration**:
   - The Dockerized environment ensures all operations are contained within the project folder, preventing unintended system-level changes.

---

## Setup and Installation

### Prerequisites

1. **Docker and Docker Compose** installed on your system.
2. An existing **GitHub account** to host your script repository.
3. A project folder where this system will operate.

### Installation Steps

1. **Download the Setup Script**:
   Save the `setup_dynamic_api.sh` file in your project folder.

2. **Run the Setup Script**:
   Make the script executable and run it:
   ```bash
   chmod +x setup_dynamic_api.sh
   ./setup_dynamic_api.sh
   ```

3. **Follow the Script Instructions**:
   - Create a GitHub repository and provide the URL when prompted.
   - The script will:
     - Set up the project folder with all necessary files.
     - Initialize the Git repository and push the setup to GitHub.
     - Build and run a Docker container for the API.

4. **Access the API**:
   Once the setup is complete, access the API at:
   ```
   http://localhost:8000
   ```

---

## API Endpoints

### 1. `GET /`
- **Description**: Verifies the API is running.
- **Response**:
  ```json
  {
    "message": "Hello, from your GitHub-integrated API!"
  }
  ```

### 2. `GET /list-scripts`
- **Description**: Lists all scripts available in the `scripts` folder.
- **Response**:
  ```json
  {
    "scripts": ["sample_script.sh", "run_sql.sh"]
  }
  ```

### 3. `POST /run-script`
- **Description**: Executes a specified script with optional arguments.
- **Request Body**:
  ```json
  {
    "script_name": "sample_script.sh",
    "args": []
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "stdout": "This is a sample script!",
    "stderr": "",
    "return_code": 0
  }
  ```

### 4. `POST /git-sync`
- **Description**: Synchronizes the `scripts` folder with the GitHub repository (pull, commit, push).
- **Request Body** (optional):
  ```json
  {
    "message": "Updated scripts"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Git synchronization complete."
  }
  ```

---

## Benefits of the System

1. **Interactive Development**:
   - ChatGPT can assist directly in your project, automating tasks and providing insights.

2. **Dynamic Growth**:
   - The API can evolve in real-time as ChatGPT adds new functionality.

3. **Reusability**:
   - All scripts and API extensions are stored in GitHub, enabling you to reuse them across projects.

4. **Secure Operations**:
   - The Docker container ensures all operations are confined to the project environment.

5. **Version Control**:
   - GitHub integration provides a full history of changes, ensuring transparency and reversibility.

---

## Example Workflow

1. Start a new project:
   - Create a GitHub repository.
   - Run the setup script and provide the repository URL.

2. Collaborate with ChatGPT:
   - Use the API to read, modify, and execute scripts.
   - Add custom scripts or extend the API dynamically.

3. Commit and Push Changes:
   - Use the `/git-sync` endpoint to ensure all updates are saved in GitHub.

4. Use the Extended API:
   - Reuse scripts and functionalities in future projects by cloning the GitHub repository.

---

## Future Enhancements

- **Authentication**:
  - Add token-based or OAuth authentication to secure the API endpoints.
  
- **Custom GPT Integration**:
  - Directly link the OpenAPI schema to a custom GPT for seamless interactions.

- **Advanced Operations**:
  - Support more complex scripts, such as deployment automation or CI/CD workflows.

---

## Conclusion

This system transforms ChatGPT into an intelligent project assistant capable of performing dynamic tasks, adapting to project needs, and growing its own functionality over time. By combining the power of Docker, GitHub, and FastAPI, it provides a secure, extensible, and reusable environment for development collaboration.