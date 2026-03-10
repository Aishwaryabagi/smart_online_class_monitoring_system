import asyncio
import edge_tts
import pygame
import time
import os

pygame.mixer.init()

async def speak(text):

    filename = f"speech_{int(time.time())}.mp3"

    communicate = edge_tts.Communicate(text, "en-IN-NeerjaNeural")
    await communicate.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    os.remove(filename)