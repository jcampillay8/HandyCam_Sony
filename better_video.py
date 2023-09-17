import cv2

# Cargar el video de baja resolución
video_path = 'C:/Users/Jaime/Videos/Extractos/video_recortado.mp4'
cap = cv2.VideoCapture(video_path)

# Obtener la resolución original del video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Definir la nueva resolución deseada (por ejemplo, 4K)
new_width = 2560
new_height = 1080

# Crear un objeto VideoWriter para guardar el video mejorado
output_path = 'output_high_resolution_video.mp4'
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (new_width, new_height))

# Bucle para leer cada fotograma del video y redimensionarlo a la nueva resolución
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionar el fotograma utilizando interpolación bilineal
    resized_frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Escribir el fotograma redimensionado en el nuevo video
    out.write(resized_frame)

    # Mostrar el video redimensionado en tiempo real (opcional)
    cv2.imshow('High Resolution Video', resized_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los objetos y cerrar las ventanas
cap.release()
out.release()
cv2.destroyAllWindows()
