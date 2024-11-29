import flet as ft
import pygame
import os
from mutagen.mp3 import MP3
import asyncio


class Song:
    def __init__(self, filename):
        self.filename = filename
        self.title = os.path.splitext(filename)[0]
        self.duration = self.get_duration()

    def get_duration(self):
        audio = MP3(os.path.join("musica", self.filename))
        return audio.info.length


async def main(page: ft.Page):
    page.title = "Reproductor de musica"
    page.bgcolor = ft.colors.GREY_800
    page.padding = 20

    titulo = ft.Text("Reproductor de musica", size=30, color=ft.colors.WHITE)

    pygame.mixer.init()
    playlist = [Song(f) for f in os.listdir("musica") if f.endswith(".mp3")]

    def load_song():
        pygame.mixer.music.load(
            os.path.join("musica", playlist[current_song_index].filename)
        )

    def play_pause(e):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            play_button.icon = ft.icons.PLAY_ARROW
        else:
            if pygame.mixer.music.get_pos() == -1:
                load_song()
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.unpause()
            play_button.icon = ft.icons.PAUSE
        page.update()

    def update_song_info():
        song = playlist[current_song_index]
        song_info.value = f"{song.title}"
        duration.value = format_time(song.duration)
        progress_bar.value = 0.0
        current_time_text.value = "00:00"
        page.update()

    def format_time(seconds):
        minutes, seconds = divmod(int(seconds), 60)
        return f"{minutes:02d}:{seconds:02d}"

    def change_song(delta):
        nonlocal current_song_index
        current_song_index = (current_song_index + delta) % len(playlist)
        load_song()
        pygame.mixer.music.play()
        update_song_info()
        play_button.icon = ft.icons.PAUSE
        page.update()

    async def update_progress():
        while True:
            if pygame.mixer.music.get_busy():
                current_time = pygame.mixer.music.get_pos() / 1000
                progress_bar.value = (
                    current_time / playlist[current_song_index].duration
                )
                current_time_text.value = format_time(current_time)

                page.update()
            await asyncio.sleep(1)

    current_song_index = 0
    song_info = ft.Text(size=20, color=ft.colors.WHITE)

    current_time_text = ft.Text("00:00", color=ft.colors.WHITE60)

    duration = ft.Text("00:00", color=ft.colors.WHITE60)

    progress_bar = ft.ProgressBar(value=0.0, width=300, color="white", bgcolor="red")

    # controles

    play_button = ft.IconButton(
        icon=ft.icons.PLAY_ARROW, icon_color=ft.colors.WHITE, on_click=play_pause
    )
    prev_button = ft.IconButton(
        icon=ft.icons.SKIP_PREVIOUS,
        icon_color=ft.colors.WHITE,
        on_click=lambda _: change_song(-1),
    )

    next_button = ft.IconButton(
        icon=ft.icons.SKIP_NEXT,
        icon_color=ft.colors.WHITE,
        on_click=lambda _: change_song(1),
    )

    controls = ft.Row(
        [prev_button, play_button, next_button], alignment=ft.MainAxisAlignment.CENTER
    )

    fila_reproductor = ft.Row(
        [current_time_text, progress_bar, duration],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    columna = ft.Column(
        [song_info, fila_reproductor, controls],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(columna)

    if playlist:
        load_song()
        update_song_info()
        page.update()
        await update_progress()
    else:
        song_info.value = "No hay canciones en la playlist"
        page.update()


ft.app(main)
