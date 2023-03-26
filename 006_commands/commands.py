import abc


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self): ...

    @abc.abstractmethod
    def undo(self): ...


class NoCommand(Command):
    def execute(self): ...

    def undo(self): ...


class Light:
    def __init__(self, location: str):
        self.location = location

    def on(self):
        print(f"Light is on in {self.location}")

    def off(self):
        print(f"Light is off in {self.location}")


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class RemoteControlWithUndo:
    def __init__(self) -> None:
        self.on_commands = [NoCommand() for _ in range(7)]
        self.off_commands = [NoCommand() for _ in range(7)]
        self.undo_command = NoCommand()

    def set_command(self, i: int, on_command: Command, off_command: Command):
        self.on_commands[i] = on_command
        self.off_commands[i] = off_command

    def on_button_was_pushed(self, i):
        self.on_commands[i].execute()
        self.undo_command = self.on_commands[i]

    def off_button_was_pushed(self, i):
        self.off_commands[i].execute()
        self.undo_command = self.off_commands[i]

    def undo_button_was_pushed(self):
        self.undo_command.undo()

    def __str__(self) -> str:
        buffer = []
        buffer.append("\n------ Remote Control -------\n")
        for i, (on_command, off_command) in enumerate(zip(self.on_commands, self.off_commands)):
            buffer.append(
                f"[slot {i}] {on_command.__class__.__name__}"
                + f"    {off_command.__class__.__name__}\n"
            )
        buffer.append(f"[undo] {self.undo_command.__class__.__name__}\n")
        return "".join(buffer)


if __name__ == "__main__":
    remoteControl = RemoteControlWithUndo()
    living_room_light = Light("Living Room")
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    remoteControl.set_command(0, living_room_light_on, living_room_light_off)

    remoteControl.on_button_was_pushed(0)
    remoteControl.off_button_was_pushed(0)
    print(remoteControl)
    remoteControl.undo_button_was_pushed()
    remoteControl.off_button_was_pushed(0)
    remoteControl.on_button_was_pushed(0)
    print(remoteControl)
    remoteControl.undo_button_was_pushed()
