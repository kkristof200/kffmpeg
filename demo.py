from kffmpeg import ffmpeg

p_in = '/Users/kristofk/Downloads/in.mp4'
p_trm = 'trimmed.mp4'

ffmpeg.trim(p_in, p_trm, duration=5)

for e in [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]:
    p='_{}.mp4'.format(e)
    print(p)
    print(ffmpeg.rotate_video(p_trm, p, e, debug=True))