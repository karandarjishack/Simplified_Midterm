**Overview:**

The aim of this project was to deploy a machine learning model trained for malware classification as an API endpoint on AWS SageMaker. Additionally, a Python client was developed to extract features from executable files and retrieve classification results from the SageMaker endpoint. Testing of the client and endpoint was performed using one malware PE file and one benign PE file from the test dataset created during Lab 5.4.

**
Project Goals:**

Deploy a pre-trained malware classification model on AWS SageMaker.
Develop a Python client application to interact with the deployed model.
Demonstrate the system's functionality using test data.


**Technical Approach:**

Deploying the Model on AWS SageMaker:

Utilized the trained model from Lab 5.4 for malware classification.
Followed AWS SageMaker documentation to deploy the model as an API endpoint.
Ensured monitoring of spending on AWS to remain within budget constraints.
**Developing the Python Client:**

Developed a Python client to interact with the deployed SageMaker endpoint.
The client extracted relevant features from executable files using techniques learned during Lab 5.4.
Integrated functionality to send feature vectors to the SageMaker endpoint and retrieve classification results.
**Testing and Demonstration:**

Tested the Python client and SageMaker endpoint using one malware PE file and one benign PE file.
Demonstrated the functionality of the client and endpoint in a video demo.
**Performance Analysis:**

Evaluated the performance of the deployed model and Python client based on the accuracy of classification results.
Monitored latency to ensure efficient processing of classification requests.
Conducted thorough testing to verify the robustness and reliability of the system.
**Conclusion:**

This project successfully deployed a machine learning model for malware classification as an API endpoint on AWS SageMaker. By developing a Python client, the endpoint's functionality was extended to accept executable files, extract features, and provide classification results. Testing with real-world samples demonstrated the effectiveness and practicality of the solution.

GitHub Repository:

Repository Link: [Provide your repository link here]
Please refer to the repository for the complete implementation details, code files, report, and video demo.
