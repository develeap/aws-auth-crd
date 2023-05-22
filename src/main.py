from src.crd_handler import CRDHandler

def main():
    crd_handler = CRDHandler()

    # Watch for changes and deletions of AWSAuth resources in the specified namespace
    crd_handler.watch_awsauth("kube-system")

if __name__ == "__main__":
    main()
