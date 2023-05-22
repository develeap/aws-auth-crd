from kubernetes import client


class AWSAuthHandler:
    def __init__(self):
        self.api = client.CoreV1Api()

    def update_awsauth_configmap(self, namespace, data):
        # Get the current aws-auth ConfigMap
        config_map_name = 'aws-auth'
        config_map = self.api.read_namespaced_config_map(name=config_map_name, namespace=namespace)

        # Update the data section of the ConfigMap
        config_map.data = data

        # Update the aws-auth ConfigMap
        updated_config_map = self.api.replace_namespaced_config_map(name=config_map_name, namespace=namespace,
                                                                    body=config_map)
        return updated_config_map
