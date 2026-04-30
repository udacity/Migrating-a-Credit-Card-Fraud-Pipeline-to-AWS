# Migrating a Credit Card Fraud Pipeline to AWS

In this project, you will work as a cloud architect at a credit card company. The company's data scientists have developed a fraud detection pipeline on-premises, which includes:

1. A Spark pipeline running on a Hadoop cluster that transforms incoming data and trains the model.
2. A containerized API running on an on-premises server that returns a fraud/no-fraud response.
3. A function or workflow that updates the data used to train the model and triggers model retraining.

Your task is to migrate this pipeline to AWS Cloud, ensuring improved security, scalability, performance, and cost-efficiency. You will use the skills learned in this course to:

1. **Evaluate each workload and select appropriate AWS services** for storage, model training, API deployment, retraining, and monitoring/logging.
2. **Modify the starter source code** so the training job, prediction API, and retraining workflow run with your selected AWS services instead of relying on local-only execution.
3. **Deploy and configure the selected AWS services**, including the IAM roles or service permissions needed for the services to run and interact securely.
4. **Provide evidence that the migrated pipeline works in AWS** by completing the project template with short explanations and screenshots showing the training job, model artifact, running API service, retraining workflow, and IAM/service permission configuration.

## Getting Started

Follow the steps below to make modifications to the code on your local machine:

1. Clone the project repo 
2. Make the necessary modifications to the code where "#TODO"s have been provided
3. Upload the appropriate code to your AWS environment
4. Deploy and configure your selected AWS services
5. Complete the project template with your rationale, screenshots, and workflow explanation

### Dependencies

```
Python 3.9
PySpark 3.3.1
FastAPI 0.89.1
Joblib 1.2.0
Pipenv 2022.10.4
```

### Installation for Local Machine
We highly recommend completing the project work in AWS Cloud9.

1. Clone the repository to your local machine
2. (Optional) Install and create a virtual environment using pipenv
   - ```pip install pipenv```
   - ```pipenv shell```
3. Install the necessary dependencies using pipenv in each project directory
   - ```pipenv install pyspark fastapi joblib```
   - Note: the directories are meant to be standalone pipenv environments, so you can run ```pipenv shell``` in each directory to activate the environment.
4. You can run starter scripts locally while developing using the following command:
   - ```pipenv run python <app_name>.py```

## Project Instructions

Complete the project by migrating the starter fraud detection pipeline to AWS. Your submission must include the modified project code and a completed project template.

<a href="https://video.udacity-data.com/topher/2026/April/69f3095b_migrating_a_credit_card_fraud_template/migrating_a_credit_card_fraud_template.docx" target="_blank">Download the project template from here</a>.

For each workload, complete the following tasks:

⬜ **Select the AWS services for your architecture**

- Choose suitable AWS services for data and model storage, model training, API deployment, retraining or refresh, and monitoring/logging.
- Base your choices on the workload requirements and course content.
- Document each selected service and your rationale in the template.

⬜ **Modify the provided Python scripts**

- Update the starter scripts to work with your selected AWS services (**address all TODOs**).
- Include the training script, API script, retraining or refresh workflow code, and any required deployment files.
- Use AWS-accessible data and model locations for deployed execution.

⬜ **Configure the AWS services and permissions**

- Provision the AWS services needed for your architecture.
- Configure IAM roles, execution roles, task roles, service roles, or service permissions so the services can run and interact securely.
- Do not include AWS secret access keys in your code or submission.

⬜ **Provide evidence in the template**

- Add readable screenshots showing:
  - The model training job or training service completed successfully.
  - The trained model artifact exists in AWS storage or a managed model artifact location.
  - The prediction API service is deployed and running.
  - The retraining workflow ran, logged an invocation, or started the training process.
  - The IAM roles or service permissions used by the architecture. Include all roles or service permissions used, with at least two separate role/service permission examples.
- Add short answers explaining how the final AWS workflow connects the training job, model artifact, API, and retraining process.

### Model Training Job

The development team's model training job uses PySpark to:

  - Extract the raw data from the source location
  - Transform the data (splitting into train/test, modifying columns for training)
  - Load the resulting data into the input folder
  - Train the model and output the resulting model in the destination folder

The development team would like an AWS service that satisfies the following requirements:

- Automate as much as possible of the data preparation environment.
- Integrate with other AWS services.
- The team does not have experience managing infrastructure, so they would like to use a fully managed service.
- The model will only be trained monthly, so they do not want to pay for ongoing infrastructure.
- Eventually, they would like to develop a data catalog of all of their existing datasets.

Your evidence should show the training job or service completed successfully and show where the trained model artifact was saved.

### Model Deployment API

Once the model is trained, the development team uses the trained model via a FastAPI service to:

  - read the incoming transaction
  - process the transaction as fraud or non-fraud
  - return the result at the endpoint

The development team would like to deploy their API to an AWS service that:

- Can serve as a container orchestration service without the need to manage servers or Kubernetes clusters.
- Can automatically scale to support an increased load of requests.
- Integrates with CloudWatch and CloudTrail for monitoring and logging.

Your evidence should show the deployed API service running and explain how it accesses the trained model.

### Model Retraining Function

The model retraining function is an event-based function that:

  - Monitors for new data in an AWS-accessible source, storage location, database, or event flow.
  - Triggers retraining when a new file is added.
  - Labels the model as latest and saves it for inference.

They would like an AWS service that:

- Does not require the developers to manage servers.
- Can respond to new data or a scheduled refresh and execute the retraining workflow.
- Is efficient for this infrequent monthly workload.
- Can easily integrate with the service used for the model training job.

Your evidence should show the retraining workflow ran, logged an invocation, or started the training process.


## License
[License](../LICENSE.txt)
