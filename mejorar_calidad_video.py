import cv2

def mejorar_calidad_video(video_path, output_path, brillo=1.2, contraste=1.2):
    # Abrir el archivo de video
    video_capture = cv2.VideoCapture(video_path)

    # Obtener las propiedades del video (ancho, alto y FPS)
    video_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_fps = int(video_capture.get(cv2.CAP_PROP_FPS))

    # Crear un objeto VideoWriter para escribir el video de salida
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, video_fps, (video_width, video_height))

    while True:
        # Leer un fotograma del video
        ret, frame = video_capture.read()

        if not ret:
            break

        # Aplicar el filtro de mejora de color al fotograma actual
        frame_mejorado = cv2.addWeighted(frame, brillo, frame, 0, contraste)

        # Escribir el fotograma mejorado en el video de salida
        output_video.write(frame_mejorado)

        # Mostrar el fotograma original y el mejorado (opcional, solo para visualización)
        cv2.imshow('Video Original', frame)
        cv2.imshow('Video Mejorado', frame_mejorado)

        # Detener la reproducción si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar los objetos de video
    video_capture.release()
    output_video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Ruta del video que deseas mejorar
    video_path = "C:/Users/Jaime/Videos/Varios/Hspital Chuqui Abril 98.mp4"

    # Ruta del video de salida mejorado
    output_path = "video_mejorado_v2.mp4"

    # Llamar a la función para mejorar el video
    mejorar_calidad_video(video_path, output_path, brillo=1.5, contraste=1.5)


'''
from moviepy.editor import VideoFileClip

def mejorar_calidad_video(input_path, output_path, resolution=(2560, 1080), audio_volume=1.5):
    # Cargar el video
    video = VideoFileClip(input_path)
    
    # Aumentar la resolución del video
    video = video.resize(resolution)
    
    # Ajustar el volumen del audio
    video = video.volumex(audio_volume)
    
    # Guardar el video mejorado en un nuevo archivo
    video.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    input_video = "C:/Users/Jaime/Videos/Varios/Hspital Chuqui Abril 98.mp4"
    output_video = "output_mejorado3.mp4"
    nueva_resolucion = (2560, 1080)  # Cambia esta resolución según lo que desees
    nuevo_volumen = 1.5  # Ajusta el volumen del audio según lo que desees
    
    mejorar_calidad_video(input_video, output_video, nueva_resolucion, nuevo_volumen)
'''