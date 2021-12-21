Sparing Quad Scheduler

This is a scheduler out-of-tree plugin in order to  asssign different types of applications to servers hoping for good socket fits.

It implements the sparing algorithm of matching as many "bad" pairs together between contensious applications before allowing "good" fits to happen.

In order to run:

   1. cd to root directory and type *make*
   2. wait for the build to happen
   3. *optional* docker push the docker image to your hub if you want
   4. docker container exec and transfer the sparingquad-config.yml file to /etc/kubernetes and the kube-scheduler.yml file to /etc/kubernetes/manifests folder.
   5. validate the plugin with the proposed Pod template.
