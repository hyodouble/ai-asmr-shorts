# Mochi — fixed character (2026-10-20)

Mochi's look drifted from clip to clip and episode to episode (cream vs orange fur, ginger ear patch on/off, body shape, scarf texture) because every clip was text-to-video from a written description.

Fix: a Flow **Character** named `Mochi` is registered in both Mochi projects:
- gksgytjr1027: `flow.google.com/u/0/project/b4b28eeb-fc43-42c7-a978-2b0d9feac28e` (character 3d869370)
- supergiantapple: `flow.google.com/u/2/project/e9990f1d-feb7-4345-bf63-d17b6b351a3b` (character 44ad6638)

Source: `mochi_ref.png` (frame from Mochi #14 clip 1). Flow turned it into `mochi_character_portrait.jpg`; the second account was created from that portrait so both match.

## How to use in every Mochi clip
1. In the agent box type `@`, pick **Mochi (캐릭터)**, click **프롬프트에 추가**, then paste the clip prompt after it.
2. Do NOT add "text-to-video only, without using any image..." to Mochi prompts (that line is Tofu-only).
3. Describe Mochi in the prompt exactly like the character, nothing else:
   "Mochi, a tiny fluffy cream-white kitten with a round head, big round blue-grey eyes, a small pink nose, soft peach-tinted ears, a short fluffy tail and a red knitted scarf with fringed ends"
   (the old "one ginger patch over its left ear" is dropped: the reference has none, and the conflict caused drift).
4. Projects for a new account (e.g. hoohihi123123 remakes) need the same character: Characters, Upload `mochi_character_portrait.jpg`, name it `Mochi`, paste the info text below.

Character info text:
Mochi is a tiny fluffy cream-white kitten in soft Pixar-like 3D style: round head, big round blue-grey eyes, small pink nose, soft peach-tinted ears, short fluffy tail, chubby little body, and a red knitted scarf with fringed ends. Mochi is curious and playful, never speaks, and lives in the same cozy sunlit kitchen. Always keep this exact look, colors and scarf.

Upload tip: Flow's 업로드 button opens a native picker. Patch `HTMLInputElement.prototype.click` in the page so a file input is appended to the DOM instead, then use the browser file_upload tool on it. A rights notice ("이 이미지를 사용할 권리") appears once per account; the user approved accepting it on 2026-10-20.
