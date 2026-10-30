# Tofu — fixed character (2026-10-30)

On 2026-10-30 the user deleted **every Tofu Flow project** on both nwgreen1024 (/u/3) and nwgreen1026 (/u/4). The old project URLs (2763963f..., 03c974fe...) are gone, and nothing about Tofu survives inside Flow. This folder is now the only source of Tofu's look. The next episode starts in a **new project** on each account.

Tofu was always pure text-to-video (no Flow Character). His look stayed stable for #1-#22 because the same description sentence was pasted word for word into every clip. Keep doing that.

## Reference images (from Tofu #21, raw Flow clips, no overlays)
- `tofu_ref_crop.png` — Tofu alone, side-front view (s3 at 4 s, cropped).
- `tofu_ref_scene.png` — full 720x1280 frame: Tofu + the park (bench left, pine, lamps).
- `tofu_ref_closeup.png` — close two-shot (s6 at 9 s), hat/scarf knit detail.

Use them only to check a new clip by eye. Do not attach them to prompts unless the user decides to switch Tofu to a Flow Character (see the end).

## Fixed description (paste exactly, every clip)
Tofu is a tiny round baby penguin with fluffy grey-and-white down, big shiny dark eyes and a small orange beak, wearing a yellow knitted beanie with a pompom and a mustard-yellow knitted scarf.

- Grey back and flippers, white face and belly, black cap of feathers under the beanie, orange feet.
- Beanie: mustard-yellow, ribbed knit, one round pompom on top. Scarf: same mustard yellow, chunky knit, ends hang down the front.
- He never speaks. Pronoun in prompts: "he". Size: side animals are "about as tall as Tofu".
- Never give the beanie or scarf away or take them off; props drift between clips (#1 lost the scarf mid-episode).

## Fixed background (paste exactly, every clip)
A quiet snowy park at dusk, with a wooden bench on the left, one tall pine tree in the middle and warm glowing street lamps; light snow falls gently from the sky at its natural speed the whole time; the bench and the pine are visible from the first frame to the last and never appear or disappear.

Episode props (pond, stream, snowdrift, den hole...) are added to this sentence, never replace it.

## Fixed prompt frame
Start: `Pixar-style 3D animation, warm and cozy, vertical 9:16, camera: <one camera sentence>; the character's motion stays at normal real-time speed even while the camera moves gently, everything moves at normal real-time speed, never slow motion, single continuous take.`

Then background, Tofu sentence, side-animal sentence, `In the very first frame ...` (both animals already in place), action, `At the end of the clip ...` (= next clip's first frame), `Sounds: ...`.

End (always):
Absolutely no music of any kind: no background music, no score, no soundtrack, no melody, no instruments, only the natural sound effects described. No spoken words, no narration. Every object in the park keeps the same place and the same count from the first frame to the last: exactly one bench, one tall pine tree, and nothing new ever appears, vanishes or duplicates. Tofu's feet always stay on top of the packed snow; he never sinks in. Exactly two animals in the whole scene, Tofu and the <friend>; no other animals, and neither of them ever fades, vanishes or duplicates. No text, no captions, no jump cuts, no morphing, no extra limbs, the animals keep the same look in every frame.

Full working example: `templates/story-tofu-22.txt`.

## Rules learned (#1-#22)
- Side animal = "a natural wild animal with bare soft fluffy <color> fur". Never write clothing words, even negated (hat/scarf makes them wear one).
- Tofu is in the first frame of every clip. A lone baby fawn in frame 1 was blocked ("서드 파티 콘텐츠 제공업체의 이견").
- A hole/den/box prop: say it is empty, nobody inside, or Flow puts a copy of the character there.
- Food that gets eaten starts already in the eater's mouth/beak.
- Flow can't draw "sunk up to her chest in snow"; write "lies on her tummy with legs tucked under her and buried".
- "no antlers" grows antlers; describe the head instead.
- "round snowdrift" is drawn as a snowman; write "one big round mound of piled snow shaped like a single giant snowball, not a snowman: no head, no face, no second ball" (#23).
- "disappears behind X" is not drawn; send a prop out of the frame edge instead (#23).
- Never write bell/chime. Props never span a container wall.

## Production setup (unchanged)
- nwgreen1024 /u/3: s1-s3, nwgreen1026 /u/4: s4-s6 (or 5 clips if asked). Remakes on hoohihi123123 /u/1.
- Current projects (from 2026-10-30): nwgreen1024 /u/3 bd7aa60c-2826-4d90-b2aa-f633d2e80d13, nwgreen1026 /u/4 a1916773-b245-4911-b9ea-debff1aa96d7, remakes hoohihi123123 /u/1 b9144382-172a-4215-839c-e9772a41e18e.
- New project per account, agent auto-generate "안 함" (no approval card).
- 1.2x speed, Flow Music BGM, captions per scene, ENDHOLD=2.

## Optional: lock with a Flow Character (like Mochi)
If Tofu starts drifting, register a Character `Tofu` in each new project: Characters, Upload `tofu_ref_crop.png`, name `Tofu`, info text = the fixed description above + "Tofu never speaks and lives in the same snowy park at dusk. Always keep this exact look, colors, beanie and scarf." Then `@` → Tofu (캐릭터) → 프롬프트에 추가 before each prompt. Upload steps: `characters/mochi/README.md`.
