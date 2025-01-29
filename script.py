from kubernetes import client, config

# Load kubeconfig to connect to the Kubernetes cluster
config.load_kube_config()

def check_pod_status(namespace="default"):
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace)

    for pod in pods.items:
        pod_name = pod.metadata.name
        pod_status = pod.status.phase

        if pod_status != "Running":
            print(f"Pod '{pod_name}' is not running (Status: {pod_status})")
            log_file = f"{pod_name}-logs.txt"
            logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)
            with open(log_file, "w") as file:
                file.write(logs)
            print(f"Logs saved to '{log_file}'")

if __name__ == "__main__":
    namespace = input("Enter the namespace (default is 'default'): ") or "default"
    check_pod_status(namespace)

