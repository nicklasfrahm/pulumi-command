import * as command from "@pulumi/command";
import * as random from "@pulumi/random";
import { interpolate } from "@pulumi/pulumi";

const cluster = new aws.eks.Cluster("cluster", {});

// We might want to use `RemoteCommand` to run this from within a node in the cluster
const cleanupKubernetesNamespaces = new command.Command("cleanupKubernetesNamespaces", {
    // This will run before the clsuter is destroyed.  Everything else will need to depend on this resource to ensure this cleanup doesn't happen too early.
    delete: "kubectl delete --all namespaces",
    environment: {
        KUBECONFIG: cluster.kubeconfig,
    },
});