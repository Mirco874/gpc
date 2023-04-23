import json;

def get_reports():
    reports_file = open("./data/reports.json","r");
    reports_json = json.loads(reports_file.read());
    reports_file.close();
    return reports_json;

def add_report(camera, location, timestamp, detection, image):
    new_report = {camera+"-"+timestamp:{
        "camera": camera,
        "location": location,
        "timestamp": timestamp,
        "detection": detection,
        "image":image
    }};
    reports_file = open("./data/reports.json","r");
    reports_json = json.loads(reports_file.read());

    new_report_to_string=json.dumps (new_report,indent=4)
    saved_reports_to_string=json.dumps(reports_json,indent=4)
    reports_file.close()

    write_file=open("./data/reports.json","w");

    if(saved_reports_to_string=="{}" or saved_reports_to_string=="" or saved_reports_to_string==" "):
        write_file.write(new_report_to_string[0:len(new_report_to_string)]);
    else:
        merge = saved_reports_to_string[0:len(saved_reports_to_string)-1]+","+new_report_to_string[1:len(new_report_to_string)]
        write_file.write(merge);
    write_file.close();

def delete_report(report):
    try:
        reports_file=open("./data/reports.json","r");
        reports=json.loads(reports_file.read());
        reports_file.close();
        del reports[report];

        writing_file=open("./data/reports.json","w");
        writing_file.write(json.dumps(reports));
        writing_file.close();
    except:
        pass
