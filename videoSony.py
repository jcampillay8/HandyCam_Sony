from moviepy.editor import VideoFileClip
import os
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def recortar_video(nombre_archivo, minuto_inicio, minuto_fin):
    video = VideoFileClip(nombre_archivo)
    duracion_total = video.duration
    duracion_recorte = (minuto_fin - minuto_inicio) * 60
    if minuto_inicio >= 0 and minuto_fin <= duracion_total / 60:
        inicio = minuto_inicio * 60
        fin = inicio + duracion_recorte
        video_recortado = video.subclip(inicio, fin)
        carpeta_extractos = "C:/Users/Jaime/Videos/Extractos"  # Ruta de la carpeta de extractos
        os.makedirs(carpeta_extractos, exist_ok=True)
        ruta_video_recortado = os.path.join(carpeta_extractos, "video_recortado2.mp4")
        fps = video.fps if video.fps is not None else 30
        video_recortado.write_videofile(ruta_video_recortado, fps=fps, codec="libx264")
        video_recortado.close()
        print(f"El video ha sido recortado y guardado en: {ruta_video_recortado}")
    else:
        print("Los minutos de inicio o fin están fuera del rango del video.")

app.layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label("Nombre del archivo"),
                                dbc.Input(id="input-nombre-archivo", type="text", placeholder="Ingrese el nombre del archivo"),
                            ],
                            width=6,
                        ),
                        dbc.Col(
                            [
                                dbc.Label("Minuto de inicio"),
                                dbc.Input(id="input-minuto-inicio", type="number", placeholder="Ingrese el minuto de inicio"),
                            ],
                            width=3,
                        ),
                        dbc.Col(
                            [
                                dbc.Label("Minuto final"),
                                dbc.Input(id="input-minuto-fin", type="number", placeholder="Ingrese el minuto final"),
                            ],
                            width=3,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label("Carpeta de extractos"),
                                dbc.Input(id="input-carpeta-extractos", type="text", placeholder="Ingrese la carpeta de extractos"),
                            ],
                            width=12,
                        ),
                    ]
                ),
                dbc.Button("Recortar video", id="btn-recortar-video", color="primary", className="mt-3"),
                html.Div(id="output-message", className="mt-3"),
            ],
            className="mt-5",
        ),
    ]
)


@app.callback(
    dash.dependencies.Output("output-message", "children"),
    dash.dependencies.Input("btn-recortar-video", "n_clicks"),
    dash.dependencies.State("input-nombre-archivo", "value"),
    dash.dependencies.State("input-minuto-inicio", "value"),
    dash.dependencies.State("input-minuto-fin", "value"),
    dash.dependencies.State("input-carpeta-extractos", "value"),
)
def recortar_video_callback(n_clicks, nombre_archivo, minuto_inicio, minuto_fin, carpeta_extractos):
    if n_clicks and nombre_archivo and minuto_inicio is not None and minuto_fin is not None and carpeta_extractos:
        try:
            minuto_inicio = int(minuto_inicio)
            minuto_fin = int(minuto_fin)
            recortar_video(nombre_archivo, minuto_inicio, minuto_fin)
            return f"El video ha sido recortado y guardado en: {carpeta_extractos}/video_recortado2.mp4"
        except Exception as e:
            return f"Error al recortar el video: {str(e)}"
    return ""


if __name__ == "__main__":
    app.run_server(debug=True)
