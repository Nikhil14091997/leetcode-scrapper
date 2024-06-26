
# LeetCode GraphQL Profile Scraper with FastAPI

This project is a FastAPI application for scraping LeetCode user profiles using GraphQL. It provides multiple REST endpoints for accessing various data related to LeetCode profiles.

## Installation

To get started with this project, follow these steps:

1. **Fork the Repository**: Fork this repository to your GitHub account by clicking the "Fork" button at the top-right corner of the page.

2. **Ensure Python 3 is Installed**: Make sure you have Python 3 installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/downloads/).

3. **Install Dependencies**: Use pip to install the required dependencies listed in the `requirements.txt` file. You can install them by running the following command in your terminal:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once you've installed the dependencies, you can start using the FastAPI application. The endpoints provided by this application allow you to retrieve various data from LeetCode profiles.

   ```bash
   python app.py
   ```

## Endpoints

### 1. Get User Public Profile
- **Endpoint**: `/user_public_profile/{username}`
- **Description**: Get the public profile of a user.
- **Parameters**:
  - `username`: The username of the user.
- **Returns**: The public profile of the user.

### 2. Get User Detailed Public Profile
- **Endpoint**: `/user_detailed_public_profile/{username}`
- **Description**: Get the detailed public profile of a user.
- **Parameters**:
  - `username`: The username of the user.
- **Returns**: The detailed public profile of the user.

### 3. Get User Language Stats
- **Endpoint**: `/user_language_stats/{username}`
- **Description**: Get the language stats of a user.
- **Parameters**:
  - `username`: The username of the user.
- **Returns**: The language stats of the user.

### 4. Get User Skill Stats
- **Endpoint**: `/user_skill_stats/{username}`
- **Description**: Get the skill stats of a user.
- **Parameters**:
  - `username`: The username of the user.
- **Returns**: The skill stats of the user.

### 5. Get User Contest Ranking Info
- **Endpoint**: `/user_contest_ranking_info/{username}`
- **Description**: Get the contest ranking info of a user.
- **Parameters**:
  - `username`: The username of the user.
- **Returns**: The contest ranking info of the user.

### 6. Get User Problems Solved
- **Endpoint**: `/user_problems_solved/{username}`
- **Description**: Get the problems solved by a user.
- **Parameters**:
  - `username`: The username of the user.
- **Returns**: The problems solved by the user.

### 7. Get User Profile Calendar
- **Endpoint**: `/user_profile_calendar/{username}/{year}`
- **Description**: Get the profile calendar of a user for a specific year.
- **Parameters**:
  - `username`: The username of the user.
  - `year`: The year of the calendar.
- **Returns**: The profile calendar of the user.

Each endpoint serves a specific purpose related to scraping LeetCode profile data. Refer to the documentation or code for more details on how to use each endpoint.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to submit a pull request with your changes. Make sure to follow the contribution guidelines outlined in the `CONTRIBUTING.md` file.

## License

This project is licensed under the NA.
