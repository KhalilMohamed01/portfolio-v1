# Projects

## Project Overview

Mohamed Khalil has built several academic and personal software projects covering full-stack web development, artificial intelligence, data science, real-time applications, payment management, and data processing.

* **AI-Powered Job Application Tracker** — Full-stack application combining job application management, AI-powered job analysis, tailored application content generation, email synchronization, and analytics.
* **School Clubs Management Platform** — Full-stack web application for managing school clubs, events, students, and club-manager workflows.
* **Automotive Sales Forecasting** — Data science application using SARIMA and Prophet to forecast automotive sales through a Flask API and Angular dashboard.
* **School Payment Management Platform** — Web application for managing school fees, invoices, parent accounts, administrative workflows, email communication, and Stripe payments.
* **Chess Learning Platform** — Personal project built around chess learning, game analysis, mistakes detection using Stockfish, and chess puzzles.
* **Valorant Competitive Platform** — Personal project designed around competitive Valorant leagues, real-time features, player performance, team formation, and map selection.

Mohamed often uses projects as practical learning environments. He generally starts with an idea or problem that interests him and then identifies the technologies and concepts required to implement it. This allows him to learn through concrete development rather than only through isolated exercises or tutorials. When learning from documentation or tutorials, he prefers adapting the concepts to his own projects rather than reproducing the original example exactly.

---

# AI-Powered Job Application Tracker

The AI-Powered Job Application Tracker is a full-stack platform designed to help manage and improve the job application process. The application combines traditional software engineering with artificial intelligence to analyze job offers, compare them with a candidate's profile, select relevant experiences and projects, generate tailored application content, and track applications throughout the recruitment process.

The backend is built with Java and Spring Boot 4 and uses a feature-based architecture. It exposes REST APIs consumed by the Vue frontend. Spring Security, JWT authentication, and BCrypt password hashing are used to authenticate users and protect API endpoints. DTOs are used to control the data exchanged between the API and frontend rather than exposing database entities directly.

The application uses PostgreSQL with JPA and Hibernate. The database stores information about users, candidate profiles, experiences, projects, job offers, applications, application statuses, and status history. Historical application-status information is preserved so that the application can provide funnel-style analytics and show how applications progress over time rather than only storing their current status.

A central part of the project is its AI-powered job analysis pipeline. OpenAI is used to process job offers through several steps rather than relying on one large prompt. The system isolates the relevant job-offer information, analyzes the offer, evaluates the relevance of the candidate's previous professional experiences and projects, assigns relevance scores from 0 to 100, selects the most relevant experiences and projects, rewrites relevant experience bullet points to better match the offer, and generates or adapts the candidate's profile summary.

The application also contains a candidate profile with information about the candidate's skills, experiences, projects, background, and professional information. This information is used during job matching and when generating tailored application content.

The project includes automated resume generation. AI-generated content is inserted into a LaTeX template before the final document is generated. The resume-generation system uses FreeMarker, LaTeX, pdflatex, and MiKTeX.

The platform also integrates with Microsoft Outlook through the Microsoft Graph API. OAuth2 is used for authentication, and the integration handles email synchronization, token refresh, email processing, and duplicate detection. Email messages are deduplicated using their message IDs. Jsoup is used when HTML email content needs to be processed, and the project also experiments with Ollama as part of email processing. The objective is to identify relevant job-related messages and connect them with the appropriate application information.

The frontend is built with Vue 3, TypeScript, the Composition API, Pinia, Vue Router, and Tailwind CSS. It provides interfaces for managing job offers and applications, viewing candidate information, reviewing AI analysis, viewing application history, and exploring analytics. Docker Compose is used to run the application's services together.

This project allowed Mohamed to explore full-stack development, REST API design, authentication and authorization, PostgreSQL, database design, AI integration, multi-step LLM pipelines, prompt-based processing, email automation, OAuth2, document generation, analytics, and Docker. It is also one of his main projects for exploring how artificial intelligence can be integrated into a traditional software application.

---

# School Clubs Management Platform

The School Clubs Management Platform is a full-stack web application designed to help manage school clubs and their events. The application provides different functionality for club managers and students.

Club managers can manage their clubs and create, update, and delete events. Students can browse available clubs and view their events. The application therefore combines administrative workflows with a student-facing interface for discovering school activities.

The application uses JWT-based authentication and supports different user roles. Access to functionality is controlled according to the user's role, allowing club managers and students to interact with the platform according to their responsibilities.

The project uses the MERN stack: MongoDB for data storage, Express.js for the backend, React for the frontend, and Node.js as the runtime environment.

Through this project, Mohamed worked with full-stack JavaScript development, REST APIs, JWT authentication, CRUD operations, MongoDB, React, Express.js, Node.js, and role-based access control.

---

# Automotive Sales Forecasting

The Automotive Sales Forecasting project is a data science application designed to forecast automotive sales using historical data. The project combines statistical forecasting models with a web-based dashboard so that analytical results can be accessed and visualized through an application.

The forecasting system uses two approaches: SARIMA and Prophet. These models are used to analyze historical sales data and generate future forecasts. The project therefore combines statistical time-series analysis with software development.

A Flask API provides access to the forecasting functionality and acts as the connection between the forecasting logic and the frontend. The frontend is built with Angular and TypeScript and provides a dashboard for visualizing the forecasting results.

This project allowed Mohamed to explore the intersection between software engineering and data science. He worked with time-series forecasting, statistical models, Python, Flask APIs, Angular dashboards, data visualization, and the integration of analytical models into a web application.

---

# School Payment Management Platform

The School Payment Management Platform is a web application designed to manage school fee payments and related administrative workflows. The system provides functionality for both parents and school administrators.

Parents can use the platform to manage school fee payments, view payment-related information, and access invoices. Administrators can manage payment information and the associated administrative processes. The application also includes email functionality for communicating with parents.

The platform integrates Stripe for online payment processing, allowing parents to make school-related payments through the application.

The project includes parent accounts, an administrative interface, school fee management, invoice management, email communication, and online payments. It therefore combines user management, administrative workflows, payment processing, invoicing, email communication, and third-party API integration within a full-stack web application.

---

# Chess Learning Platform

The Chess Learning Platform is a personal project that Mohamed built around his interest in chess and his goal of using software to support his own learning.

The project focuses on learning from played games rather than simply providing a traditional chess-playing interface. One of the main concepts is to analyze games using Stockfish, identify mistakes made during games, and use those mistakes as learning opportunities.

The platform also includes the idea of chess puzzles and opening learning. The purpose is to combine game analysis, mistake detection, and targeted practice into a personal chess-learning environment.

The project reflects Mohamed's approach to learning through building. Rather than studying chess only through existing platforms, he used his interest in chess as an opportunity to build software around the problems he personally wanted to solve.

---

# Valorant Competitive Platform

The Valorant Competitive Platform is a personal project that Mohamed built around competitive gaming and his interest in real-time web technologies.

The platform is designed around league-based competition. Players can participate in leagues where they compete against other players belonging to the same league. Teams can be formed from players within the league, with different team combinations possible rather than permanently assigning players to fixed teams.

The project also includes the concept of an individual performance leaderboard, allowing player performance to be tracked independently of team composition. Competitive matches can involve map bans and map selection as part of the match workflow.

One of the main technical motivations behind the project was learning WebSockets and understanding how real-time communication could be used in a practical application. Rather than learning WebSockets through an isolated example, Mohamed built a competitive platform where real-time features could have a concrete purpose.

The project combines his interest in competitive games with his interest in learning new software technologies and experimenting with real-time application architecture.

---

# Project Development Approach

Mohamed frequently uses personal and academic projects as learning environments. Instead of learning a technology only through isolated exercises, he often starts with an idea or problem that interests him and then determines which technologies and concepts are needed to implement it.

This approach can be seen across several projects. The AI-powered job application tracker combines his interest in artificial intelligence with full-stack application development. The Automotive Sales Forecasting project combines software engineering with data science. The Chess Learning Platform uses software to support his personal interest in chess, while the Valorant Competitive Platform uses a competitive gaming concept as a practical reason to explore real-time communication with WebSockets.

When following tutorials or documentation, Mohamed generally adapts the concepts to his own ideas rather than reproducing the original example exactly. This allows him to use projects as practical environments for understanding technologies, architectures, and technical problems.

Some projects were primarily developed as personal or academic learning projects rather than as products intended for public deployment. They are nevertheless built projects that allowed Mohamed to explore specific technologies and solve concrete problems.

---

# Technical Areas Explored

Across his projects, Mohamed has worked with or explored full-stack web development, frontend development, backend development, REST APIs, authentication and authorization, relational databases, NoSQL databases, data science, time-series forecasting, artificial intelligence, LLM integration, AI-powered workflows, email automation, OAuth2, payment integration, document generation, Docker, real-time applications, and data processing.

His projects span several technology stacks, including Java and Spring Boot, Python and Flask, Angular and TypeScript, Vue.js and TypeScript, React and Node.js, PostgreSQL, MongoDB, and various third-party APIs and services. This variety has allowed him to work on different types of software problems, from traditional CRUD applications and business workflows to AI pipelines, forecasting systems, payment processing, document generation, and real-time applications.
