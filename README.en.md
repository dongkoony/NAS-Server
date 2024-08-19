# NAS Server and Webpage Project

[![EN](https://img.shields.io/badge/lang-en-blue.svg)](README.en.md) 
[![KR](https://img.shields.io/badge/lang-kr-red.svg)](README.md)

#### [한국어 문서 보기 (KR)](README.md)

This project is a personal NAS (Network Attached Storage) server and webpage built using Django. It provides a secure and efficient solution for file storage, management, and access. The server is designed to be easily deployable and will be containerized using Docker for streamlined deployment and scalability.

## Project Goals

- **Secure File Storage**: Ensure that all files are stored securely with proper authentication and access controls.
- **User Authentication**: Implement robust user authentication to restrict access to authorized users only.
- **Scalability**: Containerize the application using Docker for easy deployment and scalability.
- **Web Interface**: Provide a clean and user-friendly web interface for managing and accessing files.
- **Extensibility**: Build a modular and extensible architecture to allow future enhancements and integrations.

## Technologies Used

- **Framework**: Django (v3.2.25) - A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Database**: SQLite (Default), with options for MySQL or PostgreSQL for production environments.
- **Frontend**: Basic HTML/CSS templates (with plans for future enhancement).
- **Environment Management**: Python `virtualenv` or `conda` for managing dependencies and environments.
- **Containerization**: Docker - To be used for containerizing the application and ensuring consistent deployment across different environments.
- **Security**: Python `cryptography` and `pyOpenSSL` libraries for SSL/TLS support and encryption.
- **Environment Variables**: `python-dotenv` for managing environment variables securely.
- **Extensions**: Django Extensions for additional development tools.

## Setup and Installation

### Prerequisites

- Python 3.7+
- pip or conda for package management
- Docker (for containerization)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/dongkoony/NAS-Server.git
    cd NAS-Server
    ```

2. **Set up the Environment:**

    Using `virtualenv`:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Or using `conda`:

    ```bash
    conda create -n nas python=3.7
    conda activate nas
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    ```bash
    - mysql-server: MySQL server software, used to host a MySQL database server.
      - sudo apt-get install mysql-server
    
    - libmysqlclient-dev: MySQL development library, supporting the `mysqlclient` Python package for communication with the MySQL server.
      - sudo apt-get install libmysqlclient-dev
    
    - openssl: An open-source library supporting SSL/TLS communication.
      - sudo apt-get install openssl
    
    - ufw: A simple firewall configuration tool.
      - sudo apt-get install ufw
    ```
    
4. **Environment Variables:**

    Create a `.env` file in the root directory and add the following variables:

    ```plaintext
    DJANGO_SECRET_KEY=<Your_Secret_Key>
    DJANGO_ALLOWED_HOSTS=<Your_IP>
    DJANGO_DEBUG=True <True / False>
    ```

5. **Run the Application:**

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

    Access the application at `http://127.0.0.1:8000`.

### Docker Container (Planned)

This project will be containerized using Docker to simplify deployment and scaling. The following steps will be added:

- **Dockerfile**: Create a Dockerfile to define the Docker image.
- **Docker Compose**: Use Docker Compose to manage multi-container applications, if needed.
- **CI/CD Pipeline**: Implement a CI/CD pipeline to automate testing and deployment using tools like GitHub Actions.

## Versioning

This project uses [Semantic Versioning](https://semver.org/) for version control. 

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or questions, please reach out via [shin.dh922@gmail.com](mailto:shin.dh922@gmail.com).
