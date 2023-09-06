import os
import cv2

def generate_video(imagenes, salida, fps=30, espera=0, transicion=1):

    os.makedirs(os.path.dirname(salida), exist_ok=True)

    if os.path.exists(salida):
        os.remove(salida)

    altura, anchura, _ = cv2.imread(imagenes[0]).shape

    video = cv2.VideoWriter(salida, cv2.VideoWriter_fourcc(*'mp4v'), fps, (anchura, altura))

    fotogramas_espera = int(fps * espera)
    fotogramas_transicion = int(fps * transicion)

    for i, imagen in enumerate(imagenes):
        frame = cv2.imread(imagen)
        
        if i > 0:
            for j in range(fotogramas_transicion):
                alpha = j / fotogramas_transicion
                transicion_frame = cv2.addWeighted(frame_anterior, 1 - alpha, frame, alpha, 0)
                video.write(transicion_frame)

        for _ in range(fotogramas_espera + 1):
            video.write(frame)
        
        frame_anterior = frame

    video.release()

    
