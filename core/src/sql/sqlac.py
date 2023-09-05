from sqlalchemy.orm import sessionmaker
import logging
import sql.dialogue_sql
from sql.dialogue_sql import Dialogue

logger = logging.getLogger(__name__)
Session = sessionmaker(bind=sql.dialogue_sql.engine)


def insert_dialogue(id, conv_id, dialogue_state, system_action, response, event_ts):
    """

    :param id: id of the user
    :param conv_id: chat ID
    :param dialogue_state: the latest dialogue state
    :param system_action: the latest system dialogue action
    :param response: the latest system response
    :param event_ts: time stamp of the event
    :return:
    """

    session = Session()
    dlg = Dialogue()
    dlg.user_id = id
    dlg.conversation_id = conv_id
    dlg.dialogue_state = dialogue_state
    dlg.system_action = system_action
    dlg.response = response
    dlg.event_ts = event_ts

    session.add(dlg)
    session.commit()
    session.close()


def update_dialogue(id, conv_id, dialogue_state, system_action, response, event_ts):
    """
    update the dialogue record with a specific user ID
    :param id: id of the user
    :param conv_id: chat ID
    :param dialogue_state: the latest dialogue state
    :param system_action: the latest system dialogue action
    :param response: the latest system response
    :param event_ts: time stamp of the event
    :return:
    """
    session = Session()

    session.query(Dialogue).filter(Dialogue.user_id == id).update({
        "conversation_id": conv_id,
        "dialogue_state": dialogue_state,
        "system_action": system_action,
        "response": response,
        "event_ts": event_ts},
        synchronize_session='evaluate')

    session.commit()
    session.close()


def show_dialogues():
    """
    search for all dialogues in record
    :return: all dialogue records
    """
    session = Session()
    data = session.query(Dialogue).all()
    session.close()
    for dialogue in data:
        logger.info('get dialogue data: {id}'.format(id=dialogue.user_id))
    return data


def find_record_by_id(id):
    """
    find the dialogue record that the current user is using
    :param id: id of the user
    :return: the specific dialogue state
    """
    session = Session()
    data = session.query(Dialogue).filter(Dialogue.user_id == id)

    if data.count():
        dialogue_record = data.one()
        logger.info('id: {id}'.format(id=dialogue_record.user_id))
        logger.info('dialogue_state: {dialogue_state}'.format(dialogue_state=dialogue_record.dialogue_state))
        logger.info('system_action: {system_action}'.format(system_action=dialogue_record.system_action))
        logger.info('response: {response}'.format(response=dialogue_record.response))

        session.close()
        return data.one()

    logger.info('Can\'t find a record')
    session.close()
    return None


def delete_dialogue(id):
    """
    delete a user dialogue state by user id
    :param id: id of the user
    :return:
    """
    session = Session()
    session.query(Dialogue).filter(Dialogue.user_id == id). \
        delete(synchronize_session=False)
    session.commit()
    session.close()


def delete_all_dialogues():
    """
    delete all rows in the dialogues table
    :param conn: Connection to the SQLite database
    :return:
    """
    session = Session()
    session.query(Dialogue). \
        delete(synchronize_session=False)
    session.commit()
    session.close()


if __name__ == "__main__":
    find_record_by_id('UAFQN2YP3--')

    insert_dialogue('UAFQN2YP3', 'UAFQN2YP3', '{}', 'startConversation()', '{}', '1527166060.000005')
    logger.info(show_dialogues())

    update_dialogue('UAFQN2YP3', 'UAFQN2YP3', '{}', 'startConversation()', '{}', '1527166060')
    logger.info(show_dialogues())

    insert_dialogue('UAFQN2YP3--', 'UAFQN2YP3', '{}', 'startConversation()', '{}', '1527166060.000005')
    insert_dialogue('12345', 'UAFQN2YP3', '{}', 'startConversation()', '{}', '1527166060.000005')
    logger.info(show_dialogues())

    find_record_by_id('UAFQN2YP3--')

    delete_dialogue('UAFQN2YP3--')
    logger.info(show_dialogues())

    delete_all_dialogues()
    logger.info(show_dialogues())
