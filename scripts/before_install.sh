#!/bin/bash
# if [[ "$UID" –ne "$ROOT_UID" ]] ; then
#    echo "It must be root to run this bash script."
#    exit 1
#else
mv /var/www/django/contatoproj/templates/index.html /var/www/django/contatoproj/templates/indexBKP_$(date +%F-%T).html
exit 0
#fi
