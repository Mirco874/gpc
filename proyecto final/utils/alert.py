from pygame import mixer

def sound_alert():
    mixer.init();
    mixer.music.load("./assets/sounds/alert_sound.mp3");
    mixer.music.play(loops=1);
