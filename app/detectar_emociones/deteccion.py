from deepface import DeepFace
import math 

def calcular_nivel_estres(emotions):
    # Coeficientes de estrés para cada emoción
    stress_coefficients = {
        "angry": 2.36,
        "disgust": 7.27,
        "fear": 1.76,
        "happy": -7.56,
        "sad": 2.85,
        "surprise": 2.45,
        "neutral": 5.05
    }

    
    total_stress = 0
    for emotion, value in emotions.items():
        # Calcular el nivel de estrés basado en el coeficiente y el valor de la emoción
        stress_value = stress_coefficients[emotion] * (math.log(value * 100 + 1))
        total_stress += stress_value
    
    return total_stress

#crear funcion que si las emociones negativas son mayores a las positivas, entonces la persona esta estresada
def clasificar_estres(emotions):
    
    emociones_negativas = ["angry","disgust","fear","sad"]
    emociones_positivas = ["happy","surprise","neutral"]

    total_emociones_negativas = 0
    total_emociones_positivas = 0

    #sumar los valores de las emociones negativas
    for emotion in emociones_negativas:
        total_emociones_negativas += emotions[emotion]
    #sumar los valores de las emociones positivas
    for emotion in emociones_positivas:
        total_emociones_positivas += emotions[emotion]

    #clasificar el nivel de estrés en función del nivel de estrés
    nivel_estres = "No estresado"
    if total_emociones_negativas > total_emociones_positivas:
        nivel_estres = "Estresado"
    return nivel_estres

def sumar_emociones(emotions):
    total_emociones = 0
    for emotion, value in emotions.items():
        total_emociones += value
    return total_emociones

def clasificar_estres_version_2(imagen):
    # Analizar la imagen para detectar emociones
    try:
        resultados = DeepFace.analyze(imagen, actions=['emotion'])
        emocion_predominante = max(resultados[0]['emotion'], key=resultados[0]['emotion'].get)
        # Obtener todas las emociones detectadas con sus coeficientes
        emociones = resultados[0]['emotion']
        #sumar todas las emociones
        total_emociones = sumar_emociones(emociones)
        # Calcular el nivel de estrés basado en todas las emociones detectadas
        promedio_coeficientes = calcular_nivel_estres(emociones)
        #clasificar el nivel de estrés en función del nivel de estrés
        nivel_estres = clasificar_estres(emociones)
        return nivel_estres,promedio_coeficientes,emocion_predominante, emociones,total_emociones
    except Exception as e:
        print("Error al analizar la imagen:", e)
        nivel_estres = "No se pudo analizar la imagen"
        promedio_coeficientes = 0
        emocion_predominante = "neutral"
        emociones = {}
        total_emociones = 0
        return nivel_estres,promedio_coeficientes,emocion_predominante, emociones,total_emociones
     
    


def clasificar_estres_version_3(imagen):
    resultados = DeepFace.analyze(imagen, actions=['emotion'])
    emocion_predominante = max(resultados[0]['emotion'], key=resultados[0]['emotion'].get)
    # Obtener todas las emociones detectadas con sus coeficientes
    emociones = resultados[0]['emotion']
    # Calcular el nivel de estrés basado en todas las emociones detectadas

    #ordenar las emociones de mayor a menor
    emociones_ordenadas = sorted(emociones.items(), key=lambda x: x[1], reverse=True)
    #obtener las 3 emociones con mayor coeficiente
    coeficientes = []
    for i in range(3):
        coeficientes.append(emociones_ordenadas[i])
    
    return emociones_ordenadas,coeficientes,emocion_predominante

 
