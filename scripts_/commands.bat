oc delete project eligil-dev

oc new-project eligil-dev

oc apply -f mysql-secret.yaml

oc apply -f mysql-pv.yaml

oc apply -f mysql-pvc.yaml

oc apply -f mysql-deployment.yaml


