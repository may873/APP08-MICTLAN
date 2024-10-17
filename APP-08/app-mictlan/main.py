import flet as ft


def main(page: ft.Page):
#establecer tamaña de pantalla 

    page.window_width=200
    page.window_height=200
    
    page.bgcolor="black"
    page.title="Mictlan"
    page.fgcolor="gray"
    
    intro=ft.Audio(src="Intro.mp3",volume=1,balance=0)
    page.overlay.append(intro)
    
    Primer_nivel=ft.Audio(src="Primer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Primer_nivel)

    Segundo_nivel=ft.Audio(src="Segundo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Segundo_nivel)
    
    Tercer_nivel=ft.Audio(src="Tercer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Tercer_nivel)
    
    Cuarto_nivel=ft.Audio(src="Cuarto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Cuarto_nivel)
    
    Quinto_nivel=ft.Audio(src="Quinto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Quinto_nivel)
    
    Sexto_nivel=ft.Audio(src="Sexto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Sexto_nivel)
    
    Septimo_nivel=ft.Audio(src="Septimo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Septimo_nivel)
    
    Octavo_nivel=ft.Audio(src="Octavo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Octavo_nivel)
    
    Noveno_nivel=ft.Audio(src="Noveno_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Noveno_nivel)
    
#Se crea la interfaz 
    btnIntro=ft.FilledButton(text="Escucha el Intro",disabled=False)
    
    btnNivel1=ft.ElevatedButton(text="Primer nivel")
    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)

    btnNivel2=ft.ElevatedButton(text="Segundo nivel")
    img2=ft.Image(src="segundo-Nivel.jpeg",width=150,height=150)

    btnNivel3=ft.ElevatedButton(text="Tercer nivel")
    img3=ft.Image(src="Tercer-Nivel.png",width=150,height=150)

    btnNivel4=ft.ElevatedButton(text="Cuarto nivel")
    img4=ft.Image(src="Cuarto-Nivel.jpeg",width=150,height=150)

    btnNivel5=ft.ElevatedButton(text="Quinto nivel")
    img5=ft.Image(src="Quinto-Nivel.jpeg",width=150,height=150)

    btnNivel6=ft.ElevatedButton(text="Sexto nivel")
    img6=ft.Image(src="Sexto-Nivel.jpeg",width=150,height=150)

    btnNivel7=ft.ElevatedButton(text="Septimo nivel")
    img7=ft.Image(src="Septimo-Nivel.jpeg",width=150,height=150)

    btnNivel8=ft.ElevatedButton(text="Octavo nivel")
    img8=ft.Image(src="Octavo-Nivel.png",width=150,height=150)

    btnNivel9=ft.ElevatedButton(text="Noveno nivel")
    img9=ft.Image(src="Noveno-Nivel.jpeg",width=150,height=150)
    
    page.add(
        ft.Row(
            alignment="start",
            controls=[btnIntro]
            
        ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=[btnNivel1,img1]
                    ),
                ft.Column(
                    alignment="CENTER",
                    controls=[btnNivel2,img2]
                ),
                ft.Column(
                    alignment="CENTER",
                    controls=[btnNivel3,img3]
                )
                    
                ]
        )
        )
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
ft.app(main)
