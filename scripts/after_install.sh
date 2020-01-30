#!/bin/bash
#How can I remove the BOM from a UTF-8 file?
#O BOM 'detona' o arquivo e impede que o webserver renderize corretamente o html
sed -i '1s/^\xEF\xBB\xBF//' /var/www/django/contatoproj/templates/index.html
exit 0
