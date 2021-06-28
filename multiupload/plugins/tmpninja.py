import asyncio, json, os
from multiupload import anjana
from telethon.sync import events

@anjana.on(events.NewMessage(pattern='/tmpninja'))
async def tmpninja(e):
	amjana = await e.get_reply_message()
	pamka = "./downloads/"
	noize = amjana.file.name
	snd = await anjana.send_message(e.chat_id, 'Start Downloading')
	file_name = await anjana.download_media(amjana, pamka)
	path = pamka+noize
	await snd.edit('Success !!\n Path: '+path)
    await asyncio.sleep(3)
	await snd.edit('Now uploading to TmpNinja')
	anonul = await asyncio.create_subprocess_shell(f"curl -i -F files[]=@{path} https://tmp.ninja/upload.php", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
	stdout, strderr = await anonul.communicate()
	kek = json.loads(stdout)
	dlurl = kek["files"]["url"]
	filesiz = kek["files"]["size"]
	filname = kek["files"]["name"]
	hmm = f'''File Uploaded successfully !!
**File name** = __{filname}__
**File size** = __{filesiz}__

**Download Link**: __{dlurl}__'''
	await snd.edit(hmm)
	os.remove(f'{path}')   
	os.system("ls")