#!/bin/bash
if [[ "$UID" –ne "$ROOT_UID" ]] ; then
    echo "It must be root to run this bash script."
    exit $E_NOTROOT
else
    rm /var/www/django/contatoproj/templates/index.html
fi

