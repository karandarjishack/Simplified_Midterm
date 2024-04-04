**Youtube:** https://youtu.be/2HlF7h_7xbw
# Simplified Midterm

**Overview:**

The aim of this project was to deploy a machine learning model trained for malware classification as an API endpoint on AWS SageMaker. Additionally, a Python client was developed to extract features from executable files and retrieve classification results from the SageMaker endpoint. Testing of the client and endpoint was performed using one malware PE file and one benign PE file from the test dataset created during Lab 5.4.

**Project Goals:**
Deploy a pre-trained malware classification model on AWS SageMaker.

Develop a Python client application to interact with the deployed model.

Demonstrate the system's functionality using test data.


**Technical Approach:**

Deploying the Model on AWS SageMaker:

Utilized the trained model from Lab 5.4 for malware classification.
Followed AWS SageMaker documentation to deploy the model as an API endpoint.
Ensured monitoring of spending on AWS.


**Developing the Python Client:**

Developed a Python client to interact with the deployed SageMaker endpoint.
Integrated functionality to send feature vectors to the SageMaker endpoint and retrieve classification results.



**Performance Analysis:**

Evaluated the performance of the deployed model and Python client based on the accuracy of classification results.
Monitored latency to ensure efficient processing of classification requests.
Conducted thorough testing to verify the robustness and reliability of the system.


**Conclusion:**

This project successfully demonstrated the deployment of a pre-trained malware classification model as a cloud-based API endpoint on AWS SageMaker. The rest of the part haven’t been executed but will be uploaded and documentation will be updated for the same soon for the last part.


**References:**


AWS SageMaker Documentation: https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html

Introduction to Amazon SageMaker: https://youtu.be/YcJAc-x8XLQ


Getting Started with Amazon SageMaker: https://sagemakerexamples.readthedocs.io/en/latest/intro.html

PyTorch in SageMaker: https://docs.aws.amazon.com/sagemaker/latest/dg/pytorch.html



