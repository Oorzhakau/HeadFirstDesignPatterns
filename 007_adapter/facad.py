"""
Паттерн Фасад.
Паттерн обеспечивает логическую изоляцию клиента от подсистемы, состоящей из множества компонент, и
упрощает ее интерфейс.
"""
from subclasses import *


class HomeTheaterFacade:

    def __init__(self, amp, tuner, player, projector, screen, lights, popper):
        self.amp = amp
        self.tuner = tuner
        self.player = player
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_streaming_player(self.player)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.player.on()
        self.player.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()

    def listen_to_radio(self, frequency):
        print("Tuning in the airwaves...")
        self.tuner.on()
        self.tuner.setFrequency(frequency)
        self.amp.on()
        self.amp.setVolume(5)
        self.amp.setTuner(self.tuner)

    def end_radio(self):
        print("Shutting down the tuner...")
        self.tuner.off()
        self.amp.off()


if __name__ == "__main__":
    amp = Amplifier("Amplifier")
    tuner = Tuner("AM/FM Tuner", amp)
    player = StreamingPlayer("Streaming Player", amp)
    projector = Projector("Projector", player)
    lights = TheaterLights("Theater Ceiling Lights")
    screen = Screen("Theater Screen")
    popper = PopcornPopper("Popcorn Popper")

    home_theater = HomeTheaterFacade(amp, tuner, player, projector, screen, lights, popper)

    home_theater.watch_movie("Raiders of the Lost Ark")
    home_theater.end_movie()
