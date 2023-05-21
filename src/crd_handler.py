from kubernetes import client

class CRDHandler:
    def __init__(self):
        # Initialize the Kubernetes API client
        self.api = client.CustomObjectsApi()

    def create_awsauth(self, namespace, awsauth_body):
        # Create an AWSAuth resource in the specified namespace
        # Use self.api.create_namespaced_custom_object() to interact with the API
        return self.api.create_namespaced_custom_object(
            group="stable.example.com",
            version="v1",
            namespace=namespace,
            plural="awsauths",
            body=awsauth_body
        )

    def get_awsauth(self, namespace, name):
        # Get an AWSAuth resource by name in the specified namespace
        # Use self.api.get_namespaced_custom_object() to interact with the API
        return self.api.get_namespaced_custom_object(
            group="stable.example.com",
            version="v1",
            namespace=namespace,
            plural="awsauths",
            name=name
        )

    def update_awsauth(self, namespace, name, awsauth_body):
        # Update an AWSAuth resource in the specified namespace
        # Use self.api.replace_namespaced_custom_object() to interact with the API
        return self.api.replace_namespaced_custom_object(
            group="stable.example.com",
            version="v1",
            namespace=namespace,
            plural="awsauths",
            name=name,
            body=awsauth_body
        )

    def delete_awsauth(self, namespace, name):
        # Delete an AWSAuth resource in the specified namespace
        # Use self.api.delete_namespaced_custom_object() to interact with the API
        return self.api.delete_namespaced_custom_object(
            group="stable.example.com",
            version="v1",
            namespace=namespace,
            plural="awsauths",
            name=name,
            body=client.V1DeleteOptions()
        )
