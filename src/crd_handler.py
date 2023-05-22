from kubernetes import client, watch
from aws_auth_handler import AWSAuthHandler


class CRDHandler:
    def __init__(self):
        self.api = client.CustomObjectsApi()
        self.aws_auth_handler = AWSAuthHandler()

    def handle_awsauth_event(self, event_type, awsauth):
        namespace = awsauth['metadata']['namespace']

        if event_type == 'ADDED' or event_type == 'MODIFIED':
            if 'mapRoles' in awsauth['spec']:
                # Update aws-auth ConfigMap with mapRoles data
                roles_data = awsauth['spec']['mapRoles']
                self.aws_auth_handler.update_awsauth_configmap(namespace, data=roles_data)
            elif 'mapUsers' in awsauth['spec']:
                # Update aws-auth ConfigMap with mapUsers data
                users_data = awsauth['spec']['mapUsers']
                self.aws_auth_handler.update_awsauth_configmap(namespace, data=users_data)
            else:
                print("Error: Invalid AWSAuth specification.")

        elif event_type == 'DELETED':
            # Remove mapRoles or mapUsers data from aws-auth ConfigMap
            self.aws_auth_handler.update_awsauth_configmap(namespace, data={})

    def watch_awsauth(self, namespace):
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

                self.handle_awsauth_event(event_type, awsauth)

            if not stream.is_open():
                print("Connection closed. Restarting watch...")
                break
