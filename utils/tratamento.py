# Salve o código abaixo em um arquivo chamado tratamento.py dentro da pasta utils do seu workspace Databricks

import re
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def tratar_cnpj(cnpj):
    if cnpj is None:
        return None
    cnpj_num = re.sub(r'\D', '', cnpj)
    return f"{cnpj_num[:2]}.{cnpj_num[2:5]}.{cnpj_num[5:8]}/{cnpj_num[8:12]}-{cnpj_num[12:14]}" if len(cnpj_num) == 14 else ""

def tratar_string(valor):
    if valor is None:
        return None
    valor = valor.strip().upper()
    valor = re.sub(r'[^A-Z0-9 ]', '', valor)
    return valor

tratar_cnpj_udf = udf(tratar_cnpj, StringType())
tratar_string_udf = udf(tratar_string, StringType())