# Social Network Application - Backend with Python

## Project Creators
- Nairo Elsner - [GitHub](https://github.com/nairoelsner/)
- Paulo Renato Neto - [GitHub](https://github.com/seven-renato/)

## Project Description

This project was developed as part of the 4th semester of the Data Structures and Languages course, taught by Prof. Dr. Eduardo Nunes Borges, at the Federal University of Rio Grande. The main goal is to implement a social network application that simulates loading, manipulation, and verification operations of a set of in-memory data structures.

## Functional Requirements

The application meets the following functional requirements:

- Individuals or organizations can create profiles on the network and are users of the application.
- Individuals can choose to keep certain profile information private.
- Individuals can relate to other individuals in different ways: friendship (bidirectional), family (bidirectional), or acquaintance (unidirectional).
- Individuals or organizations can be clients of other organizations.
- Users can search for individuals or organizations based on any information recorded in the profiles. The search should be performed in levels, meaning first those connected to the user and then those connected to the connected ones and so on.
- It should be possible to visualize the social network graph centered on the user, with at least two levels.

## Non-functional Requirements

- The application must have a graphical interface to perform all functionalities.
- The interface can be desktop-dependent on the operating system or web-based.

## Instructions for the Frontend

This directory contains the source code for the frontend of the application developed with React JS and Ant Design.

### Execution

[Click here](https://social-network-graphs.vercel.app/) to view the live demo in the browser.

### Project Structure

- `src/`: Contains the source code of the application.
- `src/data_structures`: Contains data structures implementations, such as the graph.
- `src/social_network`: Contains all the implementation files for the social network itself, as well as the users' implementation.
- `src/initialization`: Contains the code responsible for populating the social network with users and random relationships.

### Technologies Used

- Python
- Flask for API

## Frontend with ReactJS for Social Network respository
[Click here](https://github.com/seven-renato/social-network-frontend) to visit the repository.

### Contribution

Feel free to contribute to code improvements or bug fixes. Open an [issue](https://github.com/seu-usuario/nome-do-repositorio/issues) to discuss major changes.

### License

This project is distributed under the [MIT license](https://opensource.org/licenses/MIT). Refer to the `LICENSE` file for details.
