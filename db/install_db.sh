#!/bin/bash


#this is hte shell command for installing jammin_db
#pls first ensure that you have MySQL installed

sql_file=jammin_db.sql

set -x

if [ $# -gt 0 ]; then
  case $1 in
    "remove")
      sql_file=remove_jammin_db.sql
      ;;
    *)
      echo "unknown command: $1"
      exit 1
  esac
fi


mysql -u root -p < ${sql_file}
