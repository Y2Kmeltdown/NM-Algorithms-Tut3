import event_stream
import numpy as np
import PIL.Image



decoder = event_stream.Decoder("recording_2022-08-16_11-14-37_cd.es")


nextFrame = 0
frameDuration = 100000


outputArray = np.zeros((decoder.width, decoder.height), dtype=np.uint8)
outputArray.fill(127)


for chunk in decoder:
    for t, x, y, on in chunk:
        outputArray[(x, y)] = on*255
        

        if t >= nextFrame:
            
            image = PIL.Image.fromarray(outputArray, mode="L")
            image.save(f"frames\\{nextFrame}.png")
            outputArray.fill(127)
            nextFrame += frameDuration
            
            

