from rasa_core.actions import Action

class ActionDescricaoSanduiche(Action):
    def name(self):
        return 'action_descricao_sanduiche'

    def run(self, dispatcher, tracker, domain):
        sanduiche = tracker.get_slot('sanduiche_frango')
        q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
        result = db.query(q)

        return [SlotSet("descricao", result if result is not None else [])]

# 98406-5385