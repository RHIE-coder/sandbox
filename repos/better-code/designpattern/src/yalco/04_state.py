from __future__ import annotations
from typing import Protocol

class State(Protocol):
    def play(self, player:VideoPlayer):
        ...
    def stop(self, player:VideoPlayer):
        ...

class VideoPlayer:
    __state:State

    def __init__(self):
        self.__state = StoppedState()

    def set_state(self, state:State):
        self.__state = state
    
    def play(self):
        self.__state.play(self)
    
    def stop(self):
        self.__state.stop(self)

class StoppedState(State):
    def play(self, player:VideoPlayer):
        print("비디오 시작")
        player.set_state(PlayingState())
    
    def stop(self, player:VideoPlayer):
        print("!!! 비디오가 이미 중지되었습니다 !!!")

class PlayingState(State):
    def play(self, player:VideoPlayer):
        print("!!! 비디오가 이미 시작중입니다 !!!")
    
    def stop(self, player:VideoPlayer):
        print("비디오 잠시 멈춤")
        player.set_state(PausedState())

class PausedState(State):
    def play(self, player:VideoPlayer):
        print("비디오 재시작")
        player.set_state(PlayingState())
    
    def stop(self, player:VideoPlayer):
        print("비디오 중지")
        player.set_state(StoppedState())

if __name__ == "__main__":
    player = VideoPlayer()

    player.play() # -> PlayingState
    player.play() # "already"
    player.stop() # -> PausedState
    player.play() # -> PlayingState
    player.stop() # -> PausedState
    player.stop() # -> StoppedState
    player.stop() # "already"