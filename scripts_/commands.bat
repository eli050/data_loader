oc delete project eligil-dev

oc new-project eligil-dev

oc new-app mysql-persistent --name mysql

oc exec -it mysql-1-dmvzl -- /bin/bash


