package main

import (
	"github.com/dimitrisdol/sparingquadScheduler/sparingquad"

	"k8s.io/klog/v2"
	sched "k8s.io/kubernetes/cmd/kube-scheduler/app"
)

func main() {
	cmd := sched.NewSchedulerCommand(
		sched.WithPlugin(sparingquad.Name, sparingquad.New),
	)
	if err := cmd.Execute(); err != nil {
		klog.Fatalf("failed to execute %q: %v", sparingquad.Name, err)
	}
}
