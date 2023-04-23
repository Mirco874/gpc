import json

def load_all_cameras_state():
    cameras_state_file=open("./data/cameras_state.json","r");
    cameras_json=json.loads(cameras_state_file.read());
    cameras_state_file.close();
    return cameras_json;

def save_camera_state(cameras_json):
    cameras_state_file=open("./data/cameras_state.json","w");
    overwritten_cameras_json=json.dumps(cameras_json,indent=4);
    cameras_state_file.write(overwritten_cameras_json)
    cameras_state_file.close();
    return overwritten_cameras_json;

def read_camera_state(camera):
    return load_all_cameras_state()[camera]

def disable_camera(camera):
    cameras_json=load_all_cameras_state();
    if( cameras_json[camera]["state"]=="connected"):
        cameras_json[camera]["name"]=""
        cameras_json[camera]["model"]=""
        cameras_json[camera]["state"]="disconnected"
    save_camera_state(cameras_json)


def activate_camera(name, model , camera):
    cameras_json=load_all_cameras_state();
    if(cameras_json[camera]["state"]=="disconnected"):
        cameras_json[camera]["name"]=name
        cameras_json[camera]["model"]=model
        cameras_json[camera]["state"]="connected"

    save_camera_state(cameras_json)
