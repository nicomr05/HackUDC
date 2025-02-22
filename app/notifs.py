from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.clock import Clock
from plyer import notification
import random
import time


class NotificationScheduler:
    '''
    Clase para programar y enviar notificaciones en horas aleatorias.
    '''
    def __init__(self, num_notificaciones=2):
        self.num_notificaciones = num_notificaciones
        self.schedule_notifications()


    def schedule_notifications(self):
        now = time.localtime()
        current_hour = now.tm_hour
        current_minutes = now.tm_min

        for _ in range(self.num_notificaciones):
            rand_hour = random.randint(current_hour, 20)
            rand_minute = random.randint(current_minutes, 59)

            # Calcular segundos hasta la notificación
            target_time = rand_hour * 3600 + rand_minute * 60
            now_time = current_hour * 3600 + current_minutes * 60 + now.tm_sec
            delay = target_time - now_time
            
            assert delay > 0

            if delay > 0:
                Clock.schedule_once(self.send_notification, delay)


    def send_notification(self, dt):
        notification.notify(
            title="📸 ¡Hora de tomar una foto!",
            message="Abre la app y captura tu foto.",
            timeout=10
        )

if __name__ == "__main__":
    notif = NotificationScheduler()
    print(notif.num_notificaciones)
