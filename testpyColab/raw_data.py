ROOT_GITHUB = "https://raw.githubusercontent.com/SherylA/PythonFCE/master/Datos/"
NUMBER_EXERCISES = 5 
ROOT_FOR_EXERCISES = [ROOT_GITHUB + f'Datos_Ejercicio{i}/' for i in range(NUMBER_EXERCISES)]


########################################## CHECK_DATA ######################################
NAMES_TEST_FUNC = ["Crear una función", 
                   "La pendiente es correcta, ", 
                   "El intercepto con el eje y es correcto, "]

def returnNamesTestTables(id_select):
    if id_select == '1a':
        names_test_tables = ["Crear una función que devuelva el diccionario correcto. ", 
                             "Comprobar que la función genera la información de los bonos." ]
    elif id_select == '1b':
        names_test_tables = ["Organizar el DataFrame por cliente y fecha. ",  
                             "Crear un DataFrame con información de los bonos. ", 
                             "Concaternar los datos de entrada y salida y crear un nuevo DataFrame. "]
    return names_test_tables



def returnParams(id_select):
    if id_select == 0:
        params = {
            "slope" : [ 0.13990557,  0.9871224 , 50.03588815, 47.06105197, 33.87407988, 49.82422904],
            "intercept": [19.01972647, 13.2165551 , 38.10707111, 62.86886669, 66.21730317, 13.06513052]
        }
    elif id_select == 1:
        params = {
            "list_keys_add": ['gen_purchase_voucher','val_purchase_voucher','acum_purchase_voucher']
        }
    return params

def select_voucher(acum):
  """
  Compras acumuladas de $500.000 - $700.000 bono $50.000
  Compras acumuladas de $700.001 - $999.999 bono $60.000
  Compras acumuladas de $1'000.000 - más bono $70.000
  """
  if 700000>=acum>=500000:
    return 50000
  elif 1000000>acum>700000:
    return 60000
  elif acum> 1000000:
    return 70000
  else:
    return 0

def count_down(small_df):
  cont,sum_val = 0,0
  res,res_val = [],[]
  values = small_df['purchase_total'].values
  condition = small_df['purchase_total']>=100000
  for i,v in enumerate(condition):
    if v:
      cont +=1
      sum_val += values[i]
      if cont==5:
        res.append(True)
        res_val.append(sum_val)
        cont,sum_val=0,0
      else:
        res.append(False)
        res_val.append(0)
    else:
      cont,sum_val=0,0
      res.append(False)
      res_val.append(0)
  return {'gen_purchase_voucher':res,
          'val_purchase_voucher': [select_voucher(s) for s in res_val],
          'acum_purchase_voucher':res_val}
