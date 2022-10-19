
import pytube
import whisper

youtubeID = 'https://www.youtube.com/watch?v=5G38wWGyO10'
model = whisper.load_model('small')  #choose the model
letterVideoYT = pytube.YouTube(youtubeID) #upload the video
audio = letterVideoYT.streams.get_audio_only() #get the sound
audio.download(filename='tmp.mp4') #download the audio

result = model.transcribe('ffmpeg') #Result

print(result["text"]) #write the result