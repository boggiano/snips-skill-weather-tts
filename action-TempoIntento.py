#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):
    sentence = 'Hai chiesto '

    #Il nome dell' intento contiene anche "boggiano:"
    if intent_message.intent.intent_name == 'boggiano:TempoIntento':
        print('TempoIntento')
        sentence += 'il tempo '
#    elif intent_message.intent.intent_name == 'searchWeatherForecastTemperature':
#        print('searchWeatherForecastTemperature')
#        sentence += 'the temperature '
#    elif intent_message.intent.intent_name == 'searchWeatherForecastCondition':
#        print('searchWeatherForecastCondition')
#        sentence += 'the weather condition '
#    elif intent_message.intent.intent_name == 'searchWeatherForecastItem':
#        print('searchWeatherForecastItem')
#        sentence += 'the weather '
    else:
        return

    quando_slot = intent_message.slots.quando.first()
    citta_slot = intent_message.slots.citta.first()
    previsioni_slot = intent_message.slots.previsioni.first()

    if citta_slot is not None:
        sentence += 'a ' + citta_slot.value
        print ("[Dove] :  {}".format(citta_slot.value))
        
    if previsioni_slot is not None:
        sentence += 'in ' + previsioni_slot.value
        print ("[Cosa] :  {}".format(previsioni_slot.value))
    if quando_slot is not None :
        sentence += ' ' + quando_slot.raw_value
        print ("[Quando] :  {}".format(quando_slot.value))

    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
