oc create secret generic mysql-credentials `
  --from-literal=MYSQL_ROOT_PASSWORD=RootPass#123 `
  --from-literal=MYSQL_USER=appuser `
  --from-literal=MYSQL_PASSWORD=AppPass#123 `
  --from-literal=MYSQL_DATABASE=mydb

oc set env deployment/mysql --from=secret/mysql-credentials


oc apply -f infrastructure/k8s/mysql-pvc.yaml


oc set volume deployment/mysql `
  --add `
  --name=mysql-storage `
  --mount-path=/var/lib/mysql `
  --claim-name=mysql-pvc


docker build -t eligil/fastapi-mysql:0.4 .


docker push eligil/fastapi-mysql:0.4


oc new-app eligil/fastapi-mysql:0.4 --name=data-loader-app

oc set env deployment/data-loader-app --from=secret/mysql-credentials

oc expose deployment/data-loader-app --port=8080

oc expose service/data-loader-app


oc exec -it mysql-75f5fdf69f-rg7fr -- \
  sh -c "mysql -u$(oc get secret mysql-credentials -o jsonpath='{.data.MYSQL_USER}' | base64 -d) \
             -p$(oc get secret mysql-credentials -o jsonpath='{.data.MYSQL_PASSWORD}' | base64 -d) \
             $(oc get secret mysql-credentials -o jsonpath='{.data.MYSQL_DATABASE}' | base64 -d) \
             < /tmp/create_data.sql"

oc exec -it mysql-75f5fdf69f-rg7fr -- \
sh -c "mysql -u$(oc get secret mysql-credentials -o jsonpath='{.data.MYSQL_USER}' | base64 -d) \
         -p$(oc get secret mysql-credentials -o jsonpath='{.data.MYSQL_PASSWORD}' | base64 -d) \
         $(oc get secret mysql-credentials -o jsonpath='{.data.MYSQL_DATABASE}' | base64 -d) \
         < /tmp/insert_data.sql"

oc delete all -l app=data-loader-app
