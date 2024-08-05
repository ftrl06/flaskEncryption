# flaskEncryption
FLASK - AES (Advanced Encryption Standard) Example
This project demonstrates secure communication between a client and server using Flask. The client encrypts the data using AES (Advanced Encryption Standard) and sends it to the server. The server then decrypts and processes the received data.

Features and Functions

1. **Data Encryption and Decryption**:
   - AES Encryption**: Both the client and server use AES for data encryption and decryption. This ensures the secure transmission of data.
   - Encryption Key**: The key used for encryption is stored in the `config.py` file.

2. **Server (Flask)**:
   - Flask Framework**: A web server is created using Flask.
   - Receiving and Decrypting Data**: The server receives encrypted data from the client, decrypts it, processes it, and sends a response. This is handled in the `receive_data` endpoint.

3. **Client**:
   - Sending Data**: The client encrypts the data and sends it to the server in JSON format.
   - Server Response**: The client receives and prints the response from the server.

Use Cases

- Secure Data Transmission**: This project can be used in scenarios where secure data transmission over the network is required. For example, securely sending sensitive information (passwords, personal information, etc.) to a server.
- Encryption Education**: Provides a practical example for learning and applying AES encryption and decryption.
- Flask Applications**: Serves as a good reference for developers looking to build web applications with Flask and ensure data security.

Summary

This project sets up a Flask server that receives encrypted data from a client, decrypts it, and processes it. Using AES encryption ensures the security of the data during transmission between the client and the server. This setup is valuable for securely transmitting sensitive information over the network and provides a practical example of implementing encryption in Flask applications.
