# Climatria

## Description

Realtime Climate (US only) is a full-stack web application that provides free, timely alerts via email from Climate Central staff whenever climate-relevant events occur locally. The application focuses on delivering alerts related to local conditions, forecasts, key statistics, and links to additional resources. Users can subscribe to receive alerts based on their location and can easily unsubscribe when they no longer wish to receive updates.

## Tools and Technologies

### Frontend

- **React.js**: JavaScript library for building user interfaces.
- **Material-UI**: React components for faster and easier web development.
- **Vite**: Frontend tooling for development and building the application.
- **JavaScript (ES6+)**: Programming language used in the frontend.

### Backend

- **Python**: Programming language used in the backend.
- **Flask**: Web framework used for building the API.
- **MongoDB**: NoSQL database used for storing user information.
- **Sinch**: API service used for sending SMS messages for verification.
- **ARIMA**: Model used for processing time-series data related to climate events.
- **Docker**: Containerization platform used for deploying the application.
- **AWS EC2**: Cloud service used for deploying the application on a virtual server.

### Deployment

- **Docker Compose**: Tool used to define and run multi-container Docker applications.
- **AWS EC2**: Application is deployed on an EC2 instance running Docker containers.

The application is deployed on an AWS EC2 instance.
To access the live version of the application, visit http://3.145.3.230:5173/

## Data Sources

- **EIA API**: Used to retrieve a list of energy grid balancing authorities, which are key in determining the local energy conditions that may trigger climate alerts.
- **Sinch API**: Utilized for phone number verification during user sign-up.
- **Custom Climate Models**: Includes ARIMA models for predictive analysis and alerts.

## API Endpoints

### User Management

- **`POST /api/signup`**

  - Description: Sign up a user for climate alerts.
  - Request Body:
    ```json
    {
      "name": "string",
      "email": "string",
      "phoneNumber": "string",
      "zipCode": "string",
      "balancingAuthority": "string",
      "frequency": "string"
    }
    ```
  - Responses:
    - `201 Created`: User successfully signed up.
    - `409 Conflict`: Email already exists.
    - `500 Internal Server Error`: An error occurred during signup.

- **`POST /api/unsubscribe`**
  - Description: Unsubscribe a user from climate alerts.
  - Request Body:
    ```json
    {
      "email": "string"
    }
    ```
  - Responses:
    - `200 OK`: User successfully unsubscribed.
    - `404 Not Found`: Email not found in the system.
    - `500 Internal Server Error`: An error occurred during unsubscription.

### Data Management

- **`GET /api/balancing_authorities`**
  - Description: Retrieve a list of balancing authorities available for selection during signup.
  - Response:
    - `200 OK`: Returns a JSON array of balancing authorities.

## Installation and Running the Application

### Prerequisites

- **Docker** and **Docker Compose** installed on your machine.
- **Python 3.12+** installed on your machine.
- **Node.js and npm** installed on your machine.

### Backend Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/climate-alerts-app.git
   cd climate-alerts-app
   ```

2. **Set Up Environment Variables:**

- Create a .env file in the root directory and add the following environment variables:

```bash
MONGO_URI=mongodb+srv://<username>:<password>@climatria.6oxhz.mongodb.net
SINCH_API_KEY=your_sinch_api_key
SINCH_API_SECRET=your_sinch_api_secret
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Application:**

```bash
python app.py
```

### Frontend Setup

1. **Navigate to the Frontend Directory:**

```bash
cd src/climatriaUI
```

2. **Install Dependencies:**

```bash
cd src/climatriaUI
```

3. **Run the Application:**

```bash
npm run dev
```

### Running with Docker

1. **Build and Run the Containers:**
   from the project root directory run:

```bash
docker-compose up --build
```

2. The application will be available at http://localhost:8080 for the backend and http://localhost:3000 for the frontend.

### Deployment

The application is deployed on an AWS EC2 instance using Docker. The frontend and backend are containerized using Docker Compose and run on the EC2 instance.

Frontend URL: http://your-ec2-public-ip:3000
Backend API URL: http://your-ec2-public-ip:8080

### Contact

For any questions or issues, please contact the project maintainer at climatria@gmail.com.
