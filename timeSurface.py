from pickletools import uint8
import event_stream
import numpy as np
import PIL.Image

tau = 50000
window = 50
outputModulo = 100000
eventIndex = 0

decoder = event_stream.Decoder("recording_2022-08-16_11-14-37_cd.es")



ts = np.full((decoder.width, decoder.height), -np.inf, dtype=np.float64)
context = np.zeros((2*window+1, 2*window+1))
output = np.zeros((2*window+1, 2*window+1))



for chunk in decoder:
    for t, x, y, on in chunk:
        ts[(x, y)] = t

        if (
            x >= window
            and x < decoder.width - window
            and y >= window
            and y < decoder.height -window
        ):
            if eventIndex % outputModulo ==0:
                context = ts[(x-window):(x+window+1),(y-window):(y+window+1)]
                output = np.exp(-(np.float64(t) - context) / tau) * 255
                output = np.asarray(output, dtype=np.uint8)
                
                image = PIL.Image.fromarray(output, mode="L")
                image.save(f"frames\\{eventIndex}.png")
  
            eventIndex += 1

                

                

        