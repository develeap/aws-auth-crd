from kubernetes import client, watch

class CRDHandler:
    def __init__(self):
        # Initialize the Kubernetes API client
        self.api = client.CustomObjectsApi()

    def watch_awsauth(self, namespace):
        # Watch for changes and deletions of AWSAuth resources in the specified namespace
        # Use self.api.list_namespaced_custom_object() with watch=True to interact with the API
        resource_version = ''
        while True:
            stream = watch.Watch().stream(
                self.api.list_namespaced_custom_object,
                group="stable.example.com",
                version="v1",
                namespace=namespace,
                plural="awsauths",
                resource_version=resource_version,
                watch=True
            )
            for event in stream:
                event_type = event['type']
                awsauth = event['object']
                resource_version = awsauth['metadata']['resourceVersion']

                if event_type == 'ADDED':
                    print(f"Added AWSAuth: {awsauth}")
                elif event_type == 'MODIFIED':
                    print(f"Modified AWSAuth: {awsauth}")
                elif event_type == 'DELETED':
                    print(f"Deleted AWSAuth: {awsauth}")

            if not stream.is_open():
                print("Connection closed. Restarting watch...")
                break
