from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip,afx, CompositeAudioClip, concatenate_audioclips

number_of_videos = 3
video_clips = []
video_audios = []

for i in range(1,number_of_videos+1):
    video_clip = VideoFileClip(f"{i}.mp4").fx(vfx.fadein,1).fx(vfx.fadeout,1)
    video_clips.append(video_clip)
    video_audios.append(video_clip.audio)

combined_audio = concatenate_audioclips(video_audios)
print(combined_audio.duration)

background_audio = AudioFileClip("audio.mp3").fx(afx.audio_fadein, 1).fx(afx.volumex, 0.002)
print(background_audio.duration)

audio_repetation_count = int(combined_audio.duration/background_audio.duration)

last_audio_duration = (combined_audio.duration - (audio_repetation_count * background_audio.duration))
print(audio_repetation_count, last_audio_duration)

original_audios = []

for i in range(audio_repetation_count):
    original_audios.append(background_audio)

original_audios.append(AudioFileClip("audio.mp3").subclip(0,last_audio_duration)).fx(afx.audio_fadein, 1).fx(afx.volumex, 0.002)

final_audio = concatenate_audioclips(original_audios)
print(final_audio.duration)

final_audio = CompositeAudioClip([combined_audio, final_audio])

combined_clips = concatenate_videoclips(video_clips)
combined_clips.audio = CompositeAudioClip([final_audio])
combined_clips.write_videofile("output2.mp4", audio_codec='aac')