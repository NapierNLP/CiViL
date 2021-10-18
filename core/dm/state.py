class State:

    def __init__(self, state_config: {}):
        self.state_config = state_config

        print('state_config: {}'.format(state_config))
        self._state = {name: "" for name, config in state_config.items() if config['type'] != "unfeaturized"}

    def get(self, state_name: str = ""):
        if state_name and state_name in self._state.keys():
            return self._state.get('state_name')

    def add(self, state_name: str = "", state_value = None):
        if state_name and state_value and state_name in self._state.keys():
            self._state[state_name] = state_value

    def clear(self):
        self._state.clear()

    def __str__(self):
        return str(self._state)

