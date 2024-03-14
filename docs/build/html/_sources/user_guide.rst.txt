User Guide
==========

Welcome to the Lettings application user guide. This guide will help you navigate through various tasks and use cases commonly encountered while working with the application.

1. Modifying Tests in tests.py Files
-------------------------------------
The tests.py files, present in each Django app, contain unit tests to ensure the functionality of the application. Follow these steps to modify tests:

   a. Locate the tests.py file in the Django app you wish to modify.
   b. Open the file and locate the test cases relevant to the functionality you want to change.
   c. Modify the test cases as needed to reflect the desired behavior or functionality changes.
   d. Save the file and run the tests using the Django management command `python manage.py test` to ensure that the changes do not introduce any regressions.

Use Case: Updating Property Validation Tests
----------------------------------------------
Sarah, a developer working on the Lettings application, needs to update the validation tests for property models. She locates the tests.py file in the properties app, modifies the relevant test cases to validate new property attributes, and ensures that all tests pass before committing the changes.

2. Modifying Build Procedure in Dockerfile and docker-compose
--------------------------------------------------------------
The Dockerfile and docker-compose.yml files define the build and deployment configurations for the Lettings application. Follow these steps to modify the build procedure:

   a. Open the Dockerfile and docker-compose.yml files located in the root directory of your project.
   b. Modify the Dockerfile to include additional dependencies or configurations required for the application.
   c. Update the docker-compose.yml file to reflect any changes in service configurations or dependencies.
   d. Save the changes and rebuild the Docker images using the `docker-compose build` command to ensure that the modifications are applied correctly.

Use Case: Adding a New Dependency to the Application
------------------------------------------------------
John, a DevOps engineer, needs to add a new Python library to the Lettings application. He updates the requirements.txt file with the new dependency, modifies the Dockerfile to install the library, and updates the docker-compose.yml file to rebuild the Docker images with the latest changes.

3. Modifying Deployment Procedure in circleci/config.yml
--------------------------------------------------------
The .circleci/config.yml file defines the deployment pipeline configuration for CircleCI. Follow these steps to modify the deployment procedure:

   a. Open the .circleci/config.yml file located in the root directory of your project.
   b. Locate the deployment section and modify the steps to include any additional tasks or configurations required for deployment.
   c. Save the changes and commit them to your repository to trigger the CircleCI pipeline and deploy the updated application.

Use Case: Adding Automated Testing to Deployment Pipeline
----------------------------------------------------------
Emily, a QA engineer, wants to add automated testing to the deployment pipeline in CircleCI. She modifies the .circleci/config.yml file to include test execution steps before deploying the application. After ensuring that all tests pass, she commits the changes to the repository, triggering the deployment pipeline.

This user guide provides step-by-step instructions for common use cases encountered while working with the Lettings application. Feel free to refer to this guide whenever you need assistance with modifying tests, build procedures, or deployment configurations.
