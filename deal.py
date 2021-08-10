import os
import json

outgroup={"groups":[]}
def main():
    tdlist=os.listdir('public/voices/')
    tdlist.remove('星风.mp3')
    for folders in tdlist:
        folderlist=os.listdir('public/voices/'+folders+'/')
        foldergroup={"name": folders,"translation": {"Chinese": folders}, "voicelist": []}
        for j in folderlist:
            i=j.replace('.mp3','')
            foldergroup["voicelist"].append({"name": i,"path": folders+"/"+i+".mp3","translation": {"Chinese": i}})
        outgroup["groups"].append(foldergroup)
    outdata=json.dumps(outgroup,ensure_ascii=False,indent=4)
    with open('src/assets/voices.json','w') as fout:
        fout.write(outdata)

if __name__ == '__main__':
  main()
