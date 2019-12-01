from flask import Flask
import Fuzzy
import DB_Data

app = Flask(__name__)

# example:  http://localhost/5000/view/rina

@app.route("/view/<username_in>")
def view_player(username_in):
    data = DB_Data.retrieve(str(username_in))
    return {
        'data': data
    }

# auditory_score_in && auditory_durationIn is when user yg input value from endpoitn url
# example:  http://localhost/5000/finish/rina/10/20/30/40   ---username tak boleh ade space, and case sensitive

@app.route("/finish/<username_in>/<auditory_score_in>/<auditory_duration_in>/<visual_duration_in>/<visual_score_in>")
def game_completed(username_in, auditory_score_in, auditory_duration_in, visual_duration_in, visual_score_in):

    auditory_final_result = Fuzzy.calcAuditory(auditory_score_in, auditory_duration_in, False)
    visual_final_result = Fuzzy.calcVisual(visual_score_in, visual_duration_in, False)
    wmi_final_result = Fuzzy.calcWMI(visual_final_result, auditory_final_result, False)

    # After got auditory index, visual index and working memory index
    # Insert data (username, auditory_score_in, auditory_duration_in, auditory_index, etc)

    DB_Data.insert(username_in, auditory_duration_in, auditory_duration_in, str(auditory_final_result), visual_score_in, visual_duration_in, str(visual_final_result), str(wmi_final_result))
    return {
        'username': username_in,
        'auditoryScore': auditory_score_in,
        'auditoryDuration': auditory_duration_in,
        'result_for_auditory': auditory_final_result,
        'visualScore': visual_score_in,
        'visualDuration': visual_duration_in,
        'result_for_visual': visual_final_result,
        'working_memory_index': wmi_final_result
    }

if __name__ == "__main__":
    app.run()