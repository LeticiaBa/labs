class Television:
    """""
    Class to represent the Television objects.
    """""
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """""
        Method to set the default state of the TV
        """""
        self.__tv_channel: int = Television.MIN_CHANNEL
        self.__tv_volume: int = Television.MIN_VOLUME
        self.__tv_status: bool = False

    def power(self) -> None:
        """""
        Method to turn the TV on and off.
        """""
        self.__tv_status = not self.__tv_status

    def channel_up(self) -> None:
        """""
        Method to turn the TV channel up.
        """""
        if self.__tv_status:
            if self.__tv_channel == Television.MAX_CHANNEL:
                self.__tv_channel = Television.MIN_CHANNEL
            else:
                self.__tv_channel += 1

    def channel_down(self) -> None:
        """""
        Method to turn the TV channel down.
        """""
        if self.__tv_status:
            if self.__tv_channel == Television.MIN_CHANNEL:
                self.__tv_channel = Television.MAX_CHANNEL
            else:
                self.__tv_channel -= 1

    def volume_up(self) -> None:
        """""
        Method to turn the TV Volume up.
        """""
        if self.__tv_status:
            if self.__tv_volume == Television.MAX_VOLUME:
                self.__tv_volume = Television.MAX_VOLUME
            else:
                self.__tv_volume += 1

    def volume_down(self) -> None:
        """""
        Method to turn the TV Volume down.
        """""
        if self.__tv_status:
            if self.__tv_volume == Television.MIN_VOLUME:
                self.__tv_volume = Television.MIN_VOLUME
            else:
                self.__tv_volume -= 1

    def __str__(self) -> str:
        """""
        Method to output the string of Television

        :return: The string that is being formatted.
        """""

        return f'TV status: Is on = {self.__tv_status}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}'
