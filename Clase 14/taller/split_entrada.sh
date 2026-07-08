#!/usr/bin/bash
mkdir -p splits
# El parámetro -n l/4 divide por cantidad de líneas en 4 partes equitativas
split -n l/4 -d acceso.log splits/part_ --additional-suffix=.txt
