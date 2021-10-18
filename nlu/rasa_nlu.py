from utils.local_logger import Logger


class RasaIntent():
    """ Represents the SPRING intent."""

    def __init__(self):
        self.type = None
        self.confidence = None
        self.entities = []
        self.ranking = None

    def __str__(self):
        return str(self.__dict__)


class RasaNLU():
    """ Sends SPRING intent returned by SPRING Rasa to the Reception bot.
    """

    def __init__(self):
        pass

    @staticmethod
    def process_user_sentence(request_data):
        """ Processes user sentence.
        Arguments:
            request_data [dict] -- Object with Mercury NLU annotations.
        Returns:
            intent [SPRINGIntent] -- Intent recognized by SPRING Rasa.
        """
        print('request_data: {}'.format(request_data))
        rasa_data = request_data.get("current_state.state.nlu.annotations.spring_rasa")

        intent = RasaIntent()

        if not rasa_data:
            intent.type = 'EMPTY'
            return intent
        else:
            intent.type = rasa_data.get("intent.name")
            intent.confidence = rasa_data.get("intent.confidence")
            entities = {item.get('entity'): item.get('value') for item in rasa_data.get("entities")}
            intent.entities = entities
            intent.ranking = rasa_data.get("intent_ranking")
            return intent
