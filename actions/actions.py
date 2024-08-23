from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
import datetime

class ActionCheckAvailability(Action):
    def name(self) -> Text:
        return "action_check_availability"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        appointment_time = tracker.get_slot("appointment_time")
        appointment_date = tracker.get_slot("appointment_date")
        
        # Check if the time is within office hours (Monday to Friday, 8 AM to 5 PM)
        date_obj = datetime.datetime.strptime(appointment_date, "%Y-%m-%d")
        time_obj = datetime.datetime.strptime(appointment_time, "%H:%M")
        if date_obj.weekday() < 5 and 8 <= time_obj.hour < 17:
            dispatcher.utter_message(response="utter_suggest_appointment", appointment_date=appointment_date, appointment_time=appointment_time)
        else:
            dispatcher.utter_message(response="utter_out_of_office")
        
        return []

class ActionSaveAppointment(Action):
    def name(self) -> Text:
        return "action_save_appointment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        service = tracker.get_slot("service")
        appointment_time = tracker.get_slot("appointment_time")
        appointment_date = tracker.get_slot("appointment_date")
        full_name = tracker.get_slot("full_name")

        # Save the appointment (this could be saving to a database, sending an email, etc.)
        # Here we'll just print it out or log it
        print(f"Appointment booked for {full_name} on {appointment_date} at {appointment_time} for {service}.")

        return []

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
