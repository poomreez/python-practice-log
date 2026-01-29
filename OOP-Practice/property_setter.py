class GameSetting:

    def __init__(self):
        self._graphic = "medium"

    @property
    def graphic(self):
        return self._graphic
    
    @graphic.setter
    def graphic(self, value):
        allowed = ["low", "medium", "high"]
        if value not in allowed:
            raise ValueError("graphic must be low / medium / high")
        self._graphic = value

settings = GameSetting()

settings.graphic = "high"
print(settings._graphic)