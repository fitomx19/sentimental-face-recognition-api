import cv2

def main():
    cap = cv2.VideoCapture(0)  # Abre la cámara con el índice 0 (puede que necesites cambiar este valor dependiendo de tu configuración)

    while True:
        ret, frame = cap.read()  # Lee un frame de la cámara

        if not ret:  # Si no se pudo leer el frame, termina el bucle
            break

        cv2.imshow('Cámara', frame)  # Muestra el frame en una ventana con el título "Cámara"

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Espera por la tecla 'q' para salir del bucle
            break

    cap.release()  # Libera la cámara
    cv2.destroyAllWindows()  # Cierra todas las ventanas

if __name__ == "__main__":
    main()
