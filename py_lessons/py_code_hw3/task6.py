class TV:
    def __init__(self,
                 channel_num: int = None,
                 volume: int = None):
        if (channel_num is not None) and (channel_num > 0):
            self._channel_num = channel_num
        else:
            self._channel_num = 0
        if (volume is not None) and (0 <= volume <= 10):
            self._volume = volume
        else:
            self._volume = 0
        self._channel_name = ''
        self._channels = []
    
    def tvset(self,
              channel_num: int = None,
              volume: int = None):
        if (channel_num is not None) and (0 < channel_num <= len(self._channels)):
            self._channel_num = channel_num
            if self._channels:
                self._channel_name = self._channels[channel_num-1]
        if (volume is not None) and (0 <= volume <= 10):
            self._volume = volume
    
    def tvget(self):
        return [self._channel_num, 
                self._channel_name, 
                self._channels, 
                self._volume]
    
    def add_channel(self, channel_name: str):
        self._channels.append(channel_name)
    
    def delete_channel(self, channel_name: str):
        if channel_name in self._channels:
            self._channels.remove(channel_name)
            if channel_name == self._channel_name:
                self.tvset(channel_num=self._channel_num-1)
    
    def boost_tone(self):
        self.tvset(volume=(self._volume + 1))
    
    def channel_name(self, i: int):
        if 0 < i <= len(self._channels):
            return self._channels[i-1]
