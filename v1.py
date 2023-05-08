import argparse
from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Function to create secret
def create_secret(secret_name, secret_data, secret_type):
    # Load Kubernetes configuration
    config.load_kube_config()

    # Create Kubernetes client object
    v1 = client.CoreV1Api()

    # Create secret object
    metadata = client.V1ObjectMeta(name=secret_name)
    secret = client.V1Secret(metadata=metadata, data=secret_data, type=secret_type)

    try:
        # Create secret in Kubernetes
        v1.create_namespaced_secret(namespace='default', body=secret)
        print("Secret created successfully.")

    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespaced_secret: %s\n" % e)

# Function to retrieve secret
def get_secret(secret_name):
    # Load Kubernetes configuration
    config.load_kube_config()

    # Create Kubernetes client object
    v1 = client.CoreV1Api()

    try:
        # Get secret from Kubernetes
        secret = v1.read_namespaced_secret(name=secret_name, namespace='default')
        print("Secret data:")
        print(secret.data)

    except ApiException as e:
        print("Exception when calling CoreV1Api->read_namespaced_secret: %s\n" % e)

# Function to update secret
def update_secret(secret_name, secret_data):
    # Load Kubernetes configuration
    config.load_kube_config()

    # Create Kubernetes client object
    v1 = client.CoreV1Api()

    try:
        # Get existing secret from Kubernetes
        secret = v1.read_namespaced_secret(name=secret_name, namespace='default')

        # Update secret data
        secret.data = secret_data

        # Update secret in Kubernetes
        v1.replace_namespaced_secret(name=secret_name, namespace='default', body=secret)
        print("Secret updated successfully.")

    except ApiException as e:
        print("Exception when calling CoreV1Api->read_namespaced_secret or replace_namespaced_secret: %s\n" % e)

# Function to delete secret
def delete_secret(secret_name):
    # Load Kubernetes configuration
    config.load_kube_config()

    # Create Kubernetes client object
    v1 = client.CoreV1Api()

    try:
        # Delete secret from Kubernetes
        v1.delete_namespaced_secret(name=secret_name, namespace='default', body=client.V1DeleteOptions())
        print("Secret deleted successfully.")

    except ApiException as e:
        print("Exception when calling CoreV1Api->delete_namespaced_secret: %s\n" % e)

# Function to main menu
def main_menu():
    print("1. Create secret")
    print("2. Retrieve secret")
    print("3. Update secret")
    print("4. Delete secret")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script for managing Kubernetes secrets")
    parser.add_argument("-c", "--create", action="store_true", help="Create secret")
    parser.add_argument("-r", "--retrieve", action="store_true", help="Retrieve secret")
    parser.add_argument("-u", "--update", action="store_true", help="Update secret")
    parser.add_argument("-d", "--delete", action="store_true", help="Delete secret")
    args = parser.parse_args()

    if args.create:
        secret_name = input("Enter secret name: ")
        secret_data = input("Enter secret data: ")
        secret_type = input("Enter secret type
