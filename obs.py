import socket
import time
import sys

import obspython as obs

lastScene = None
def script_tick(seconds):
    global lastScene
    currentScene = obs.obs_frontend_get_current_scene()
    if currentScene != lastScene :
        sendSCTE("15")        
        lastScene = currentScene

def script_defaults(settings):
    obs.obs_data_set_default_string(settings, "15secondScene", "")
    obs.obs_data_set_default_string(settings, "30secondScene", "")   

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(props, "15secondScene", "15 Second Scene Name", obs.OBS_TEXT_DEFAULT)
    list = obs.obs_properties_add_list(props,"30secondScene","30 Second Scene Name", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    create_scene_selection(list)
    return props

#def script_update(settigns):

def create_scene_selection(scene_list):

    obs.obs_property_list_clear(scene_list)
    obs.obs_property_list_add_string(scene_list,"","")
    for scene in obs.obs_frontend_get_scene_names():
        obs.obs_property_list_add_string(scene_list, scene, scene)


def sendSCTE(seconds):
    
    UDP_IP = "127.0.0.1"
    UDP_PORT = 1000
    buf = 1024

    data = '''<?xml version="1.0" encoding="UTF-8"?>
    <tsduck>
        <splice_information_table>      
            <splice_insert splice_event_id="10" unique_program_id="1" out_of_network="true" splice_immediate="false">
                <break_duration auto_return="true" duration="'''+seconds+'''"></break_duration>
            </splice_insert>
        </splice_information_table>      
    </tsduck>'''
    
    dataToSend = str.encode(data)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(dataToSend, (UDP_IP, UDP_PORT))
    sock.close()
    
