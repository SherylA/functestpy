ROOT_GITHUB = "https://raw.githubusercontent.com/SherylA/PythonFCE/master/Datos/"
NUMBER_EXERCISES = 5 
ROOT_FOR_EXERCISES = [ROOT_GITHUB + f'Datos_Ejercicio{i}/' for i in range(NUMBER_EXERCISES)]


###################### CHECK_DATA ######################################
PARAMS_00 = {
    "slope" : [ 0.13990557,  0.9871224 , 50.03588815, 47.06105197, 33.87407988, 49.82422904],
    "intercept": [19.01972647, 13.2165551 , 38.10707111, 62.86886669, 66.21730317, 13.06513052]
}

NAMES_TEST_0 = ["Crear una función", "La pendiente es correcta, ", "El intercepto con el eje y es correcto, "]

