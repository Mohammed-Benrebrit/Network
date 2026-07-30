# Network: Asynchronous Social Platform

A Twitter-like social networking web application engineered to handle complex relational data and asynchronous user interactions.

This platform was built as part of **Harvard's CS50** to master full-stack development, relational database design, and asynchronous client-server communication. As I advance my expertise in **Artificial Intelligence and Machine Learning (via Stanford's ML Specialization)**, mastering these backend architectures is critical. This project demonstrates my capability to engineer the scalable infrastructure and secure data pipelines required to support data-heavy, intelligent applications.

### 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

### 🧠 Architecture & Core Features

This application leverages vanilla JavaScript `fetch()` APIs to communicate with Django endpoints, executing database transactions and DOM manipulations without triggering full page reloads.

* **Relational Database Modeling:** Engineered complex, self-referential relationships within Django's ORM (`models.py`) to manage user follower networks and map unique user instances to specific post likes.
* **Asynchronous State Management:** Implemented non-blocking JavaScript functions to handle follow/unfollow and like/unlike actions. State mutations are transmitted to the backend via POST/PUT requests and instantly rendered in the UI.
* **In-Place Content Editing:** Users can securely edit their own posts dynamically. The client-side logic swaps the static text for a pre-populated `<textarea>`, dispatches a PUT request to update the database, and re-renders the new content seamlessly.
* **Server-Side Pagination:** Integrated Django's `Paginator` class to strictly limit query sets to 10 posts per page, minimizing database load times and optimizing frontend performance.
* **Secure Authentication:** Complete user registration, login, and session tracking utilizing Django's `AbstractUser` and CSRF protection mechanisms.

### 💻 Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Mohammed-Benrebrit/Network.git](https://github.com/Mohammed-Benrebrit/Network.git)
   cd Network
