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

def clasificar_estres_version_2(imagen):
    # Analizar la imagen para detectar emociones
    print("Analizando imagen...")
    print(imagen)

    resultados = DeepFace.analyze(imagen, actions=['emotion'])
    
    emocion_predominante = max(resultados[0]['emotion'], key=resultados[0]['emotion'].get)
    # Obtener todas las emociones detectadas con sus coeficientes
    emociones = resultados[0]['emotion']
    
    # Calcular el nivel de estrés basado en todas las emociones detectadas
    promedio_coeficientes = calcular_nivel_estres(emociones)

    #clasificar el nivel de estrés en función del nivel de estrés
    
    nivel_estres = "No estresado"
    if promedio_coeficientes > 0 and promedio_coeficientes <= 20:
        nivel_estres = "Estresado"
    elif promedio_coeficientes > 20 and promedio_coeficientes <= 50:
        nivel_estres = "Muy estresado"
    elif promedio_coeficientes > 50:
        nivel_estres = "Extremadamente estresado"
    
    
    
    return nivel_estres,promedio_coeficientes,emocion_predominante

 
