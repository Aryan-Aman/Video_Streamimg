from flask import Flask,render_template,Response
#Response->represents the HTTP response sent back to client(web browser)
import cv2
app=Flask(__name__)
camera=cv2.VideoCapture(0)#access webcam

def gen_frames():#read above camera
    while True:
        success,frame=camera.read()
        if not success:
            break
        else:
            retrn,buffer=cv2.imencode('.png',frame)
            frame=buffer.tobytes()
        yield(b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/video_feed') #for img src
def video_feed():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')#whenever need to pass some funcn ,need to set mimetype

if __name__=="__main__":
    app.run(debug=True)







