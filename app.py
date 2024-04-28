import os, shutil

#directory paths
destination = '/workspaces/File-Manager/destination'
source_folder = os.getcwd()
audio_folder = os.path.join(destination, 'audio_folder')
images_folder = os.path.join(destination,'images_folder')
videos_folder = os.path.join(destination, 'videos_folder')
text_folder = os.path.join(destination, 'text_folder')

#file formats
audio_file_format = ['mp3', 'wav']
text_file_format = [ 'doc', 'docx', 'pdf', 'txt']
image_file_format = ['jpg', 'jpeg', 'png']
video_file_format = ['mp4', 'avi', 'wmv']
files = os.listdir(source_folder)

for file in files: 
    ext = file.split('.')[-1]
    
    print(os.getcwd()+file)
    print(file, os.path.exists(os.path.join(source_folder, file)))
    if ext in audio_file_format:
        shutil.move(os.path.join(source_folder, file), os.path.join(audio_folder, file))
    elif ext in image_file_format:
        shutil.move(os.path.join(source_folder, file), os.path.join(images_folder, file))
    elif ext in video_file_format:
        shutil.move(os.path.join(source_folder, file), os.path.join(videos_folder, file))
    elif ext in text_file_format:
        shutil.move(os.path.join(source_folder, file), os.path.join(text_folder, file))
        
    # filename = file.split('.')[0]