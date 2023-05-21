# The conversation with ChatGPT

Me: Play the role of python developer.
Chat: Sure
Me: As a python developer you need to write kubernetes crd handler. Make a task list for the application.
Chat: Sure! Here's a task list for developing a Kubernetes Custom Resource Definition (CRD) handler in Python:
Me: Start from step 4. Write a basic structure.
Chat: Sure.
Me: Define how will crd look for interacting with aws-auth ConfigMap.
Chat: To interact with the aws-auth ConfigMap in Kubernetes, you would typically define a Custom Resource Definition (CRD) that represents the desired state of the aws-auth ConfigMap. Here's an example of how the CRD might look.
In this example, the CRD is defined with the following attributes:

* apiVersion: Specifies the API version for the CustomResourceDefinition.
* kind: Specifies the kind of the CustomResourceDefinition.
* metadata: Contains metadata about the CustomResourceDefinition, such as its name.
* group: Specifies the API group that the CRD belongs to.
* versions: Specifies the versions of the CRD that are available.
* scope: Defines the scope of the CRD, which can be either Namespaced or Cluster.
* names: Specifies the names used for the CustomResourceDefinition, including the plural, singular, and kind.

Once the CRD is defined, you can create instances of the AWSAuth resource to represent the desired state of the aws-auth ConfigMap. Here's an example of how an AWSAuth resource might look: