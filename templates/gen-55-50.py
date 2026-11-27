"""Generate Mochi #55 and Tofu #50 clip prompts (2026-11-28). Same fixed blocks as gen-54-49.py."""
import pathlib
import re

W = pathlib.Path.home() / "Desktop/asmr_work/shorts"

# ---------------- Mochi #55: baby chihuahua that never stops shivering ----------------
M_HEAD = ("Vertical 9:16 3D animated short film in a soft Pixar-like style, warm and cute, single continuous take, camera: {cam}, static; "
          "the character's motion stays at normal real-time speed even while the camera moves gently, everything moves at normal real-time speed, lively and quick, never slow motion. "
          "Wide, deep framing with real depth and a strong sense of space: the counter runs diagonally from the front of the frame back into the room, the window, the open shelf and the open air above the counter are all in view, with soft depth of field between the foreground and the background. ")
M_CHAR = ("The kitten is Mochi, a tiny fluffy cream-white kitten with a round head, big round blue-grey eyes, a small pink nose, soft peach-tinted ears, a short fluffy tail and a red knitted scarf with fringed ends. "
          "The puppy is a tiny baby chihuahua puppy, a natural animal with bare short smooth fawn-tan fur, a little round apple-shaped head, two very big upright pointed ears, huge shiny dark eyes, a tiny black nose, thin little legs and a thin tail, about as tall as Mochi. "
          "The puppy trembles all over the whole time, in every frame, a fast tiny constant shiver from its ears to its tail, like all chihuahuas do; it never stops trembling. ")
M_KITCHEN = ("The scene is always the same cozy sunlit kitchen: a light wooden counter, white square wall tiles, a wooden-framed window on the left with a green plant in a sage-green pot on the sill, "
             "a white crock of wooden spoons and a mint-green kettle at the back of the counter, an open wooden shelf above, warm morning light from the window on the left. ")
M_CLOTH = ("On the counter there is exactly one soft thick square of plain light-blue fleece cloth, about as wide as Mochi is long, with no print or pattern; it is the only cloth in the scene, it keeps the same size and color, and it never tears, splits or doubles. ")
M_SOLID = ("Every solid thing is truly solid: the counter, the kettle, the crock, the wall and the window are hard and opaque, and no animal, paw, ear, tail or cloth ever passes through, sinks into, clips into or overlaps with any of them. "
           "The fleece cloth only ever lies on the counter or rests on top of the puppy's back; it never goes through either animal. "
           "Both animals always stand or sit on top of the counter and never sink into it. Nothing in the kitchen moves except the two animals and the fleece cloth; the shelf, kettle, crock and plant pot stay perfectly still. "
           "Gravity is real: anything that falls only ever falls down, and nothing ever floats. "
           "Mochi always stays on the left of the puppy and the puppy always stays on the right of Mochi; they never pass each other or swap sides. ")
M_TAIL = ("No music, no spoken words, no narration, no letters, no words, no speech bubbles. "
          "Every object in the kitchen keeps the same place, size and count from the first frame to the last: exactly one kettle, one crock of spoons, one plant pot, one open wooden shelf, one window and one light-blue fleece cloth, and nothing new ever appears, vanishes or duplicates. "
          "Exactly two animals in the whole scene, Mochi and the puppy; no other animals, no humans. There is only one Mochi and one puppy; neither ever splits, doubles or gets a copy. "
          "No text, no captions, no logos, no jump cuts, no morphing; Mochi keeps the exact same look, colors and red scarf the whole time, and the puppy keeps the same look.")

M = [
 ("low wide three-quarter shot of the counter from just above counter height, the trembling puppy on the right close to the camera, Mochi a little further back on the left, the folded fleece cloth lying flat on the counter between them",
  "In the very first frame the puppy already sits on the counter on the right, close to the camera, trembling hard all over, its big ears quivering and its tiny teeth chattering, hugging its thin front legs to its chest. "
  "Mochi already sits on the counter further back on the left and looks at the puppy; the fleece cloth lies flat on the counter between them. "
  "Mochi's eyes go wide with worry; it stands up and takes two small steps toward the puppy. At the end of the clip the puppy still sits trembling on the right, the cloth lies flat between them, and Mochi stands on the left, worried.",
  "Audio: tiny fast teeth chattering, small shaky puppy whimpers, a worried kitten mew, quiet kitchen room tone, already audible in the very first frame."),
 ("medium two-shot at counter height, Mochi on the left, the fleece cloth lying flat on the counter in front of Mochi, the trembling puppy on the right",
  "In the very first frame Mochi stands on the left with the flat fleece cloth on the counter right in front of its paws, and the puppy sits trembling on the right. "
  "Mochi gently bites one corner of the cloth and drags it along the counter toward the puppy, walking backward a little to the left side of the cloth; the cloth slides flat on the counter and stays one single piece. "
  "Mochi stops with the cloth lying flat right next to the puppy, then looks up proudly. The puppy keeps trembling and blinks its huge eyes at the cloth. "
  "At the end of the clip the cloth lies flat on the counter right beside the puppy, Mochi stands on the left holding one corner in its mouth, and the puppy sits trembling on the right.",
  "Audio: soft fleece sliding on a wooden counter, a little effort mew, tiny teeth chattering, quiet kitchen room tone, already audible in the very first frame."),
 ("medium close two-shot at counter height of Mochi on the left and the trembling puppy on the right with the fleece cloth beside it",
  "In the very first frame Mochi stands on the left holding one corner of the fleece cloth in its mouth, the cloth lying flat beside the puppy, and the puppy sits trembling on the right. "
  "Mochi lifts the corner and drapes the soft cloth over the puppy's back and shoulders like a little blanket, then pats it down with one paw, tuck, tuck; only the puppy's head with its big ears and its thin tail stay out. "
  "The cloth rests on top of the puppy's back the whole time and never goes through it. Mochi sits back with a satisfied smile. Under the cloth the puppy is still trembling, and the cloth trembles with it. "
  "At the end of the clip the puppy sits wrapped in the blue cloth on the right, still trembling, and Mochi sits on the left, smiling.",
  "Audio: soft fleece rustling, two gentle paw pats, a pleased kitten purr, tiny teeth chattering, quiet kitchen room tone, already audible in the very first frame."),
 ("medium close two-shot at counter height, Mochi on the left and the puppy wrapped in the blue cloth on the right",
  "In the very first frame the puppy sits on the right wrapped in the blue fleece cloth, only its head and big ears out, still trembling all over, and Mochi sits on the left. "
  "Mochi's smile fades; it tilts its head and stares at the trembling cloth. It reaches out one paw and gently tucks the edge of the cloth tighter around the puppy. The puppy keeps trembling exactly the same. "
  "Mochi blinks, puzzled, its ears turning sideways. At the end of the clip the puppy still sits trembling in the cloth on the right, and Mochi sits on the left, puzzled.",
  "Audio: a soft fleece rustle, tiny teeth chattering, a puzzled little kitten mew, quiet kitchen room tone, already audible in the very first frame."),
 ("medium close two-shot at counter height, Mochi on the left pressed against the puppy wrapped in the blue cloth on the right",
  "In the very first frame the puppy sits wrapped in the blue fleece cloth on the right, trembling, and Mochi sits close on its left. "
  "Mochi scoots in and presses its fluffy side against the puppy's left side to warm it, closing its eyes and purring; Mochi stays on the left of the puppy the whole time. "
  "The puppy closes its huge eyes and smiles, looking warm, cozy and happy, but its whole body keeps trembling, and Mochi trembles along with it from the contact. "
  "At the end of the clip the two sit pressed together side by side, the puppy smiling and trembling on the right, and Mochi on the left with its eyes closed, purring.",
  "Audio: a deep soft kitten purr, tiny teeth chattering, a happy little puppy sigh, quiet kitchen room tone, already audible in the very first frame."),
 ("medium close two-shot at counter height, Mochi on the left and the puppy wrapped in the blue cloth on the right",
  "In the very first frame Mochi sits pressed against the left side of the puppy, and the puppy sits on the right wrapped in the cloth, smiling and trembling. "
  "The puppy opens its eyes, looks at Mochi with a big happy grin and wags its thin tail; it is totally warm and happy, and it is still trembling all over, just like always. "
  "Mochi slowly leans away, looks at the trembling happy puppy, and stares at it with a completely flat, deadpan face, its ears drooping sideways, perfectly still. "
  "At the end of the clip the puppy sits on the right grinning and trembling in the cloth, and Mochi sits on the left, deadpan.",
  "Audio: a happy little puppy yip, tiny teeth chattering, a soft tail wag on fleece, one flat little kitten mew, quiet kitchen room tone, already audible in the very first frame."),
]

# ---------------- Tofu #50: baby husky stuck in a snowdrift, fetch fail ----------------
T_HEAD = ("Pixar-style 3D animation, warm and cozy, vertical 9:16, camera: {cam}, static; the character's motion stays at normal real-time speed even while the camera moves gently, "
          "everything moves at normal real-time speed, never slow motion, single continuous take. ")
T_PARK = ("A quiet snowy park at dusk, with a wooden bench on the left, one tall pine tree in the middle and warm glowing street lamps; light snow falls gently from the sky at its natural speed the whole time; "
          "the bench and the pine are visible from the first frame to the last and never appear or disappear. ")
T_CHAR = ("Tofu is a tiny round baby penguin with fluffy grey-and-white down, big shiny dark eyes and a small orange beak, wearing a yellow knitted beanie with a pompom and a mustard-yellow knitted scarf. "
          "The husky is a tiny baby husky puppy, a natural animal with bare fluffy fur: grey-and-white fur with a white face mask, bright blue eyes, small triangle ears, big soft paws and a fluffy curled tail, about as tall as Tofu. ")
T_DRIFT = ("At the foot of the one tall pine tree, on the right, there is one big soft mound of piled plain white snow, one single low wide dome like one giant snowball half-buried in the ground, wider than it is tall and about twice as tall as Tofu, not a snowman: no head, no face, no second ball, never two balls stacked; we call it the snowdrift, and it keeps the same place and shape in every frame. "
           "One short straight plain brown stick, about as long as Tofu is tall, lies on the snow on the right near the snowdrift; it is the only stick in the scene, and it never breaks, bends, splits or doubles. ")
T_SOLID = ("Every solid thing is truly solid: the pine trunk, its roots, the bench and the lamp posts are hard and opaque, and no animal, flipper, paw, tail or stick ever passes through, sinks into, clips into or overlaps with any of them. "
           "The husky only goes into or comes out of the snowdrift from its front side, and no part of its body ever shows through the snow. "
           "Tofu's feet always stay on top of the snow; he never sinks in. "
           "Gravity is real: anything that falls only ever falls down, and snow only falls down. "
           "Tofu always stays on the left of the husky and the husky always stays on the right of Tofu; they never pass each other or swap sides. ")
T_TAIL = ("Absolutely no music of any kind: no background music, no score, no soundtrack, no melody, no instruments, only the natural sound effects described. "
          "No spoken words, no narration, no letters, no words, no speech bubbles. "
          "Every object in the park keeps the same place and the same count from the first frame to the last: exactly one bench, one tall pine tree, one snowdrift and one stick, and nothing new ever appears, vanishes or duplicates. "
          "Exactly two animals in the whole scene, Tofu and one husky puppy; no other animals, and neither of them ever fades, vanishes or duplicates. "
          "There is only one penguin, Tofu, and one husky; neither ever splits, doubles or gets a copy. "
          "No text, no captions, no jump cuts, no morphing, no extra limbs, the animals keep the same look in every frame.")

STUCK = ("the husky is stuck head-first deep in the front of the snowdrift: its head, front legs and chest are buried inside the snow and out of sight, and only its fluffy back half shows outside, "
         "its two back legs kicking on the snow and its fluffy curled tail wagging fast")
T = [
 ("medium shot at snow level of the big snowdrift on the right close to the camera with the stuck husky, and Tofu on the left",
  f"In the very first frame {STUCK}. Its back legs kick and paddle, but it cannot pull its head out, and a muffled little whimper comes from inside the snow. "
  "Tofu already stands on the snow on the left, his eyes wide with worry; he flaps his flippers and waddles two steps closer. "
  "At the end of the clip the husky is still stuck head-first in the snowdrift on the right, tail wagging, and Tofu stands close on the left, worried.",
  "Sounds: soft paws kicking powdery snow, a muffled puppy whimper from inside the snow, a worried penguin peep, soft winter wind."),
 ("medium close shot at snow level of the front of the snowdrift with the stuck husky on the right and Tofu on the left beside it",
  f"In the very first frame Tofu stands on the snow on the left right beside the snowdrift, and {STUCK}. "
  "Tofu scoops soft snow from around the husky's back with both flippers, again and again, scoop, scoop, scoop, and tosses each scoop of snow to the left, where it falls down onto the ground. "
  "His flippers only touch the soft snow and the husky's fur from the outside. Little by little more of the husky's back and shoulders show. "
  "At the end of the clip the husky's shoulders are out of the snow but its head is still inside, and Tofu stands on the left with snow on his flippers.",
  "Sounds: soft scoops of powdery snow, little puffs of snow landing on the ground, muffled puppy whimpers, busy penguin peeps, soft winter wind."),
 ("medium close two-shot at snow level, Tofu on the left and the husky in front of the snowdrift on the right",
  "In the very first frame Tofu stands on the left and the husky is stuck with only its head still inside the front of the snowdrift on the right, its shoulders and body out. "
  "Tofu scoops one last big scoop of snow; the husky gives one big push with its paws and its head pops out of the snow, pop, with a little puff of snow, a white snow cap on its nose. "
  "It shakes its head, blinks its bright blue eyes and sneezes a tiny sneeze. Tofu cheers, flapping both flippers. "
  "At the end of the clip the husky stands free on the snow on the right in front of the snowdrift, and Tofu stands on the left, happy.",
  "Sounds: a soft pop of snow, a tiny puppy sneeze, a happy little yip, cheerful penguin peeps, soft winter wind."),
 ("medium two-shot at snow level, Tofu on the left, the husky on the right and the brown stick lying on the snow on the right",
  "In the very first frame the husky stands free on the right, the brown stick lies on the snow on the right near its paws, and Tofu stands on the left. "
  "The husky licks Tofu's cheek once as a thank-you, then picks up the stick in its mouth, trots one step to Tofu and drops it on the snow right in front of Tofu's feet. "
  "It sits down on the snow, tail wagging fast, eyes shining, waiting to play fetch. Tofu looks at the stick and then at the husky. "
  "At the end of the clip the stick lies on the snow in front of Tofu on the left, and the husky sits eagerly on the right.",
  "Sounds: a quick puppy lick, a soft stick drop on snow, eager puppy panting, a curious penguin peep, soft winter wind."),
 ("medium wide shot at snow level, Tofu on the left holding the stick and the husky on the right, the open snowy park stretching far into the background on the right",
  "In the very first frame Tofu stands on the left holding the brown stick in one flipper, and the husky sits on the right, ready to run, tail wagging. "
  "Tofu winds up and throws the stick with all his might; but his flipper is tiny, the stick flips over once in the air and falls down onto the snow just in front of Tofu's own feet, barely past his beak. "
  "The husky has already jumped up to chase it, then stops; it looks at the stick lying right there, then at Tofu. "
  "At the end of the clip the stick lies on the snow right in front of Tofu on the left, and the husky stands on the right, frozen mid-step.",
  "Sounds: a determined penguin grunt, a soft whoosh, a small stick plop on snow, the puppy's quick paws stopping on snow, soft winter wind."),
 ("medium close two-shot at snow level of Tofu on the left and the husky on the right, the stick on the snow between them",
  "In the very first frame Tofu stands on the left with the stick lying on the snow right in front of his feet, and the husky stands on the right looking at it. "
  "The husky gives Tofu a completely flat, deadpan look, lets out a long little sigh, and slowly lies down on the snow with its chin on its front paws, its tail going still. "
  "Tofu looks at his own tiny flipper, then at the husky, and rubs the back of his yellow beanie, embarrassed. "
  "At the end of the clip the husky lies flat and deadpan on the right, and Tofu stands on the left, embarrassed, the stick still on the snow in front of him.",
  "Sounds: a long little puppy sigh, a soft flop onto snow, an awkward tiny penguin peep, soft winter wind."),
]


def mochi(i):
    cam, act, audio = M[i]
    return M_HEAD.format(cam=cam) + M_CHAR + M_KITCHEN + M_CLOTH + M_SOLID + act + " " + audio + " " + M_TAIL


def tofu(i):
    cam, act, audio = T[i]
    return T_HEAD.format(cam=cam) + T_PARK + T_CHAR + T_DRIFT + T_SOLID + act + " " + audio + " " + T_TAIL


if __name__ == "__main__":
    here = pathlib.Path(__file__).parent
    for name, fn, hdr, folder in [
        ("story-mochi-55.txt", mochi, '# Mochi #55 "He Was Shivering So Hard... So Mochi Warmed Him Up" (2026-11-28). @Mochi on all. Twist: warm and happy, the chihuahua still trembles, it is just a chihuahua; Mochi deadpan. Side animal: baby chihuahua. One light-blue fleece cloth.', "20261128_mochi55"),
        ("story-tofu-50.txt", tofu, '# Tofu #50 "He Was Stuck in the Snow... So Tofu Dug Him Out" (2026-11-28). Twist: the husky wants fetch, Tofu\'s throw lands at his own feet, the husky lies down deadpan. Side animal: baby husky. One stick.', "20261128_tofu50"),
    ]:
        (W / folder).mkdir(parents=True, exist_ok=True)
        out = [hdr, ""]
        for i in range(6):
            p = fn(i)
            low = p.lower()
            assert not re.search(r"\b(bells?|chimes?|ringing|hat|hats|clothing|clothes|sweater|wearing|slow-motion)\b", low.replace("wearing a yellow knitted beanie", "")), (name, i)
            out += [f"# s{i+1}", p, ""]
            (W / folder / f"p{i+1}.txt").write_text(p)
        (here / name).write_text("\n".join(out))
    print("ok")
