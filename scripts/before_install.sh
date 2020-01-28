#!/bin/bash
if [[ "$UID" –ne "$ROOT_UID" ]] ; then
    echo "It must be root to run this bash script."
    exit 1
else
    rm /var/www/django/contatoproj/templates/index.html
    exit 0
fi

