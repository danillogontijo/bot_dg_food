from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter

def train (data, config, model_dir):
    training_data = load_data(data)
    configuration = RasaNLUConfig(config)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')

def run():
   interpreter = Interpreter.load('./models/nlu/default/chat')
   #print(interpreter.parse('I want to order pizza'))
   print(interpreter.parse('me manda seu cardápio'))
   print(interpreter.parse('quero um de frango'))
   print(interpreter.parse('como é o madonna'))
   print(interpreter.parse('aceita cartão'))
   #print(interpreter.parse(u'What is the reivew for the movie Die Hard?'))

if __name__ == '__main__':
    train('./data/training_data.json', './config/config.json', './models/nlu')
    #run()
