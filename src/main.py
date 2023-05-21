from my_crd_handler.crd_handler import CRDHandler

def main():
    crd_handler = CRDHandler()

    # Sample usage: create a resource
    resource_body = {
        "apiVersion": "your.crd.group/v1",
        "kind": "YourCRD",
        "metadata": {
            "name": "sample-resource"
        },
        "spec": {
            # Add your CRD-specific properties here
        }
    }
    crd_handler.create_resource(resource_body)

    # Sample usage: get a resource
    resource = crd_handler.get_resource("sample-resource")
    print(resource)

    # Sample usage: update a resource
    resource_body["spec"]["new_property"] = "updated value"
    crd_handler.update_resource("sample-resource", resource_body)

    # Sample usage: delete a resource
    crd_handler.delete_resource("sample-resource")

if __name__ == "__main__":
    main()
