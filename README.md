## Artist Recommendation Using Sagemaker Custom Scikit-learn Code (KNN)

This repo contains code related to my final capstone project for the Udacity Machine Learning Engineer course. The goal of the project is to demonstrate how to leverage the AWS Sagemaker platform to train, host, and deploy a Scikit-learn algorithm using custom training and inference code. As part of this PoC I will build a simple music artist recommendation systems using custom Scikit-learn code (KNN).

A complete summary of this project can be found in the file summary.pdf in the resources directory.

The same summary is available in a more readable blog format here: [WordPress Blog](https://wordpress.com/post/connortphoenix.wordpress.com/340)

#### Dataingest.ipynb
Data ingestion script. Pulls and integrates raw datasources from source URL.
#### DataPrep.ipynb
Data prepartion script. Processes and explores data. Outputs matrix dataset to feed KNN model and several mapping dictionaries.
#### TrainKNN_topNartists.ipnyb
Trains and deploys model. Generates predictions.
#### SOURCE directory
Contains code for custom train (train.py) and inference (predict.py) code 
#### DATA directory
Contains training data output from DataPrep.iypnb. Data in this directory is uploaded to s3 for training.
#### DATASOURCES directory
Location for other raw and processed datasources
#### RESOURCES directory
- paper_Budiman_Giri: Academic paper describing similiar approach
- proposal.pdf: Proposal Document
- summary.pdf: Project summary (pdf version of [WordPress Blog](https://wordpress.com/post/connortphoenix.wordpress.com/340))
