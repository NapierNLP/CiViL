class State:

    def __init__(self, state_config: {}):
        self.state_config = state_config

        print('state_config: {}'.format(state_config))
        self.state = {name: "" for name, config in state_config.items() if config['type'] != "unfeaturized"}

    def get(self, state_name: str = ""):
        return self.state.get(state_name)

    def add(self, state_name: str = "", state_value = None):
        if state_name and state_value and state_name in self.state.keys():
            self.state[state_name] = state_value

    def clear(self):
        self.state.clear()

    def __str__(self):
        return str(self.state)

    def __len__(self):
        return len(self.state)

