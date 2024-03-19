import frappe
import pyfcm
from pyfcm import FCMNotification
import json
from bs4 import BeautifulSoup

firebase_server_key = "AAAAGQDDHc4:APA91bFpku7zTPv_Cp1C3ZHNGuFKuYc4KPmrXqgzVdpbF2_qd3f7uOhbpCi_g0jAjc43wrDoNSr4naeM6ZQpJiQc5Sq1e58VmknfXTxoY6OkIvu591VSkDiLYFf3gn0i8NO6wCWJZPJm"

def send_notification_via_firebase(registration_token, information, realtime_type, platform = None ,title = None, body = None, same_user = None):
    info = convert_to_string_values(information)   
    push_service = FCMNotification(api_key=firebase_server_key)
    
    if realtime_type in ["typing", "update_sub_channel_for_last_message"] or same_user == 1:
        try:
            push_service.notify_single_device(
                registration_id= registration_token,
                message_title= None,
                message_body=None,
                data_message= {"route" : str(info) , "realtime_type" : realtime_type, "content_available": True},
                content_available=True
            )
        except Exception as e:
            frappe.log_error(f"Error in sending notifications: {str(e)}")   
    else:           
        if platform == "ios":
            try:
                if info.get("is_voice_clip") == "1":
                    soup = BeautifulSoup(info["content"], 'html.parser')
                    voice_clip_containers = soup.find_all('div', class_='voice-clip-container')
                    for container in voice_clip_containers:
                        for child in container.find_all('button', recursive=False):
                            child.decompose()
                    info["content"] = str(soup)
                
                push_service.notify_single_device(
                    registration_id= registration_token,
                    message_title= None,
                    message_body=None,
                    data_message= {"route" : str(info) , "realtime_type" : realtime_type, "notification_title" : title ,"notification_body": body, "no_duplicate" : "true", "content_available": True},
                    content_available=True
                )

                push_service.notify_single_device(
                    registration_id= registration_token,
                    message_title= title,
                    message_body=body,
                    data_message= {"route" : str(info) , "realtime_type" : realtime_type, "notification_title" : title ,"notification_body": body},
                    sound = "default"
                )

                
            except Exception as e:
                frappe.log_error(f"Error in sending notifications: {str(e)}")
        else:            
            try:
                push_service.notify_single_device(
                    registration_id= registration_token,
                    data_message= {"route" : str(info) , "realtime_type" : realtime_type, "notification_title" : title ,"notification_body": body},
                )
            except Exception as e:
                frappe.log_error(f"Error in sending notifications: {str(e)}")

# # ============================================================================
def convert_to_string_values(data):
    return {key: str(value) for key, value in data.items()}
# ============================================================================
