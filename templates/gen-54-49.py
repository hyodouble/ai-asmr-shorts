"""Generate Mochi #54 and Tofu #49 clip prompts (2026-11-26). Strict no pass-through wording."""
import pathlib
import re

W = pathlib.Path.home() / "Desktop/asmr_work/shorts"

# ---------------- Mochi #54: baby armadillo + mug ----------------
M_HEAD = ("Vertical 9:16 3D animated short film in a soft Pixar-like style, warm and cute, single continuous take, camera: {cam}, static; "
          "the character's motion stays at normal real-time speed even while the camera moves gently, everything moves at normal real-time speed, lively and quick, never slow motion. "
          "Wide, deep framing with real depth and a strong sense of space: the counter runs diagonally from the front of the frame back into the room, the window, the open shelf and the open air above the counter are all in view, with soft depth of field between the foreground and the background. ")
M_CHAR = ("The kitten is Mochi, a tiny fluffy cream-white kitten with a round head, big round blue-grey eyes, a small pink nose, soft peach-tinted ears, a short fluffy tail and a red knitted scarf with fringed ends. "
          "The armadillo is a tiny baby armadillo, a natural animal: a smooth rounded light grey-pink shell with soft bands across its back, a small pointed snout, small round upright ears, shiny black eyes, four short legs and a short tapered tail, about half as long as Mochi; when it curls up it becomes one smooth round banded ball. ")
M_KITCHEN = ("The scene is always the same cozy sunlit kitchen: a light wooden counter, white square wall tiles, a wooden-framed window on the left with a green plant in a sage-green pot on the sill, "
             "a white crock of wooden spoons and a mint-green kettle at the back of the counter, an open wooden shelf above, warm morning light from the window on the left. ")
M_MUG = ("On the counter on the right there is exactly one big round plain blue ceramic mug with one handle, about as tall as Mochi, with thick hard opaque walls, a solid bottom and a round open mouth; "
         "it has no picture, print or pattern, it is never see-through, and its walls, rim, bottom and handle always stay whole, hard and the same size; they never bend, stretch, melt, crack or open. ")
M_SOLID = ("Every solid thing is truly solid: the mug, the counter, the kettle, the crock, the wall and the window are hard and opaque, and no animal, paw, snout, ear, tail, shell or object ever passes through, sinks into, clips into or overlaps with any of them. "
           "The armadillo only ever goes into or comes out of the mug through the mug's round open mouth, never through its walls, bottom or handle. "
           "Mochi's paws only ever touch the outside of the mug and the outside of the armadillo's shell; Mochi's paws never go inside the mug. "
           "Both animals always stand on top of the counter and never sink into it. Nothing in the kitchen moves except the two animals and the mug they touch; the shelf, kettle, crock and plant pot stay perfectly still. "
           "Gravity is real: anything that falls only ever falls down, and nothing ever rolls uphill or floats. "
           "Mochi always stays on the left of the armadillo and the armadillo always stays on the right of Mochi; they never pass each other or swap sides. ")
M_TAIL = ("No music, no spoken words, no narration, no letters, no words, no speech bubbles. "
          "Every object in the kitchen keeps the same place, size and count from the first frame to the last: exactly one kettle, one crock of spoons, one plant pot, one open wooden shelf, one window and one blue mug, and nothing new ever appears, vanishes or duplicates. "
          "Exactly two animals in the whole scene, Mochi and the armadillo; no other animals, no humans. There is only one Mochi and one armadillo; neither ever splits, doubles or gets a copy. "
          "No text, no captions, no logos, no jump cuts, no morphing; Mochi keeps the exact same look, colors and red scarf the whole time, and the armadillo keeps the same look.")

M = [
 ("low wide three-quarter shot of the counter from just above counter height, the blue mug standing upright on the right close to the camera, Mochi a little further back on the left",
  "In the very first frame the blue mug already stands upright on the right, and the armadillo is already curled into a ball and wedged tight in the mug's round open mouth: only the top of its banded shell and the tip of its tail show above the rim, and the shell fits the rim exactly. "
  "Mochi already stands on the counter on the left, behind the mug, looking at it. The armadillo squeaks and wiggles, the tip of its tail flicks and the whole mug wobbles a little on its solid bottom, but the shell stays stuck in the mouth of the mug. "
  "Mochi's eyes go wide; it takes two small steps toward the mug and tilts its head. At the end of the clip the armadillo ball is still stuck in the mug's mouth, the mug stands upright on the right, and Mochi stands close on the left, worried.",
  "Audio: tiny worried armadillo squeaks, the ceramic mug softly rocking on the wooden counter, a curious kitten mew, quiet kitchen room tone, already audible in the very first frame."),
 ("medium two-shot at counter height, Mochi on the left and the upright blue mug with the stuck armadillo ball on the right",
  "In the very first frame the mug stands upright on the right with the armadillo ball stuck in its round open mouth, and Mochi stands close on the left. "
  "Mochi puts both front paws on the outside of the mug's wall and slowly, carefully tips the mug over onto its side so it lies on the counter with its open mouth facing left toward Mochi and its solid bottom facing right; the mug does not roll, it stays still on its side. "
  "Now the round banded shell of the armadillo is clearly seen filling the open mouth of the lying mug, facing Mochi. Mochi pats the outside of the shell gently with one paw, tap, tap; the shell does not move. "
  "At the end of the clip the mug lies still on its side on the right with its mouth facing left, the armadillo ball still stuck in the mouth, and Mochi sits on the left in front of the mouth, thinking.",
  "Audio: the ceramic mug gently tipping onto the wooden counter with a soft knock, soft paw taps on a smooth shell, a tiny muffled squeak, quiet kitchen room tone, already audible in the very first frame."),
 ("medium close shot at counter height of Mochi on the left and the mouth of the lying blue mug on the right",
  "In the very first frame the blue mug already lies on its side on the right with its open mouth facing left, the armadillo ball stuck in the mouth, and Mochi sits on the left right in front of the mouth. "
  "Mochi puts both front paws on the outside of the shell, leans back and pulls with a determined little face; Mochi's paws stay outside the mug the whole time. "
  "With a soft pop the round armadillo ball comes out of the mug's mouth toward Mochi and rolls a short way along the flat counter; Mochi stops it gently between its two front paws. The mug stays lying still in its same place on the right. "
  "At the end of the clip Mochi sits on the left holding the round banded ball between its front paws on the counter, the ball on the right side of Mochi, and the empty mug lies on its side behind them on the right.",
  "Audio: a little straining kitten mew, a soft pop of the shell coming free from the ceramic mug, a short soft roll on wood, a surprised kitten mew, quiet kitchen room tone, already audible in the very first frame."),
 ("medium close two-shot at counter height, Mochi on the left and the armadillo ball on the right, the empty blue mug lying on its side in the background on the right",
  "In the very first frame Mochi sits on the left with its front paws resting beside the round banded armadillo ball, which sits on the counter on the right of Mochi. "
  "Mochi lifts its paws away. The ball slowly uncurls on the counter: first the pointed snout peeks out, then the small round ears and shiny black eyes, then the four short legs and the tail, until the baby armadillo stands on all four feet on the counter, its shell on its back. "
  "The armadillo blinks, shakes its head and gives a happy little squeak; it sniffs the air toward Mochi. Mochi smiles proudly and its tail swishes. "
  "At the end of the clip the armadillo stands uncurled on the counter on the right, Mochi sits smiling on the left, and the empty mug still lies on its side behind them on the right.",
  "Audio: soft shell clicks as the armadillo uncurls, a happy little armadillo squeak, a pleased kitten purr, quiet kitchen room tone, already audible in the very first frame."),
 ("medium two-shot at counter height, Mochi on the left, the armadillo in the middle and the blue mug lying on its side on the right with its open mouth facing left",
  "In the very first frame the armadillo already stands uncurled on the counter on the right of Mochi, and the empty mug lies on its side on the right with its open mouth facing left toward the armadillo. "
  "The armadillo touches its snout to Mochi's front paw for a moment as a thank-you, then turns its head and looks at the open mouth of the mug. Its eyes light up and it does a happy little hop in place on the counter. "
  "Mochi tilts its head, puzzled, and watches. At the end of the clip the armadillo stands facing the mug's open mouth on the right, Mochi sits on the left looking puzzled, and the mug lies still on its side.",
  "Audio: a soft little snout sniff, a happy armadillo squeak, a tiny hop on wood, a puzzled kitten mew, quiet kitchen room tone, already audible in the very first frame."),
 ("medium two-shot at counter height, Mochi on the left and the blue mug lying on its side on the right with its open mouth facing left, the armadillo between them in front of the mouth",
  "In the very first frame the armadillo stands on the counter right in front of the mug's open mouth, and Mochi sits on the left. "
  "The armadillo trots straight into the mug through its round open mouth, its body going in only through the open mouth and never through the wall, until only its shell back and its tail show in the opening. "
  "Inside the mouth it curls up into a round banded ball again and lets out a tiny content sigh; the ball fits the opening snugly, exactly like before, and the mug does not move. "
  "Mochi stares at it with a completely flat, deadpan face, its ears slowly drooping sideways, and stays perfectly still. At the end of the clip the armadillo ball sits snug in the mouth of the lying mug on the right, and Mochi sits on the left, deadpan.",
  "Audio: little armadillo footsteps on ceramic, a soft shell click, a tiny content sigh, one flat little kitten mew, quiet kitchen room tone, already audible in the very first frame."),
]

# ---------------- Tofu #49: baby chipmunk + burrow ----------------
T_HEAD = ("Pixar-style 3D animation, warm and cozy, vertical 9:16, camera: {cam}, static; the character's motion stays at normal real-time speed even while the camera moves gently, "
          "everything moves at normal real-time speed, never slow motion, single continuous take. ")
T_PARK = ("A quiet snowy park at dusk, with a wooden bench on the left, one tall pine tree in the middle and warm glowing street lamps; light snow falls gently from the sky at its natural speed the whole time; "
          "the bench and the pine are visible from the first frame to the last and never appear or disappear. ")
T_CHAR = ("Tofu is a tiny round baby penguin with fluffy grey-and-white down, big shiny dark eyes and a small orange beak, wearing a yellow knitted beanie with a pompom and a mustard-yellow knitted scarf. "
          "The chipmunk is a tiny baby chipmunk, a natural wild animal with bare soft fur: reddish-brown fur with dark-and-cream stripes down its back, a cream belly, a fluffy tail, small round ears and shiny black eyes, about as tall as Tofu. ")
T_HOLE = ("At the foot of the one tall pine tree there is a low smooth rounded bank of snow about twice as tall as Tofu, and in the middle of its vertical front face, facing the camera, there is exactly one small round dark burrow hole at ground level, one burrow hole only; there is no hole anywhere in the flat snow on the ground, and the bank and the hole keep the same place and shape in every frame except where Tofu widens the hole. "
          "The pine trunk and its roots are hard wood and stay whole; the burrow hole is in the snow just in front of the trunk. ")
T_SOLID = ("Every solid thing is truly solid: the pine trunk, its roots, the bench and the lamp posts are hard and opaque, and no animal, flipper, foot, tail or seed ever passes through, sinks into, clips into or overlaps with any of them. "
           "The chipmunk only ever goes into or comes out of the burrow through the round open hole in the snow bank; it never goes through the snow wall, the roots or the trunk, and no part of its body ever shows through the snow. "
           "Tofu's feet always stay on top of the snow; he never sinks in. "
           "Gravity is real: anything that falls only ever falls down, and snow only falls down. "
           "Tofu always stays on the left of the chipmunk and the chipmunk always stays on the right of Tofu; they never pass each other or swap sides. ")
T_TAIL = ("Absolutely no music of any kind: no background music, no score, no soundtrack, no melody, no instruments, only the natural sound effects described. "
          "No spoken words, no narration, no letters, no words, no speech bubbles. "
          "Every object in the park keeps the same place and the same count from the first frame to the last: exactly one bench, one tall pine tree and one burrow hole, and nothing new ever appears, vanishes or duplicates. "
          "Exactly two animals in the whole scene, Tofu and one chipmunk; no other animals, and neither of them ever fades, vanishes or duplicates. "
          "There is only one penguin, Tofu, and one chipmunk; neither ever splits, doubles or gets a copy. "
          "No text, no captions, no jump cuts, no morphing, no extra limbs, the animals keep the same look in every frame.")

FULL = "its two cheeks hugely puffed out like two big round balloons on each side of its face, clearly visible, stuffed full of seeds, so its head is much wider than the burrow hole"
T = [
 ("medium shot at snow level of the snow bank with the small burrow hole in the middle, the chipmunk on the right close to the camera and Tofu on the left",
  f"In the very first frame the chipmunk already stands on the snow right in front of the burrow hole, {FULL}. "
  "It pushes its face toward the hole, but its fat round cheeks bump against the edge of the hole, boing, and it bounces back onto the snow; it tries again, bump, and bounces back again. The edge of the hole stays firm and the chipmunk's head never goes in. "
  "It sits down on the snow, its puffed cheeks wobbling, and lets out a sad little squeak. Tofu already stands on the snow on the left and watches with worried eyes, then waddles one step closer. "
  "At the end of the clip the chipmunk sits sadly on the right in front of the small hole with its cheeks still puffed, and Tofu stands on the left close to the hole, worried.",
  "Sounds: soft little bumps of fur against packed snow, tiny sad chipmunk squeaks, a worried penguin peep, soft winter wind."),
 ("medium close two-shot at snow level of Tofu on the left and the chipmunk on the right with the small burrow hole between them",
  f"In the very first frame Tofu stands on the snow on the left of the burrow hole and the chipmunk sits on the snow on the right of the hole, {FULL}. "
  "Tofu leans forward and peeks at the small round hole, then looks at the chipmunk's big puffed cheeks, then back at the hole. His eyes light up with an idea and he lifts one flipper. "
  "The chipmunk blinks at him hopefully, its cheeks still puffed. At the end of the clip Tofu stands on the left of the hole with one flipper raised, and the chipmunk sits on the right of the hole, hopeful.",
  "Sounds: a curious penguin peep, a tiny hopeful chipmunk squeak, soft footsteps on snow, soft winter wind."),
 ("medium close shot at snow level of the burrow hole in the snow bank, Tofu on the left beside it and the chipmunk on the right",
  f"In the very first frame Tofu stands on the snow on the left right beside the small burrow hole and the chipmunk sits on the right of the hole, {FULL}. "
  "Tofu scoops soft snow from the rim of the hole with both flippers, again and again, scoop, scoop, scoop, and tosses each scoop of snow to the left, where it falls down onto the ground. His flippers only touch the soft snow at the rim of the hole and never go through the snow bank. "
  "Little by little the round hole becomes wider, until it is clearly wider than the chipmunk's puffed head; the pine trunk and roots behind it stay whole and untouched. "
  "At the end of the clip the burrow hole is round and much wider, Tofu stands on the left with snow on his flippers, and the chipmunk sits on the right, amazed.",
  "Sounds: soft scoops of powdery snow, little puffs of snow landing on the ground, happy penguin peeps, soft winter wind."),
 ("medium shot at snow level of the snow bank with the now wide round burrow hole in the middle, Tofu on the left and the chipmunk on the right",
  f"In the very first frame the burrow hole is already wide and round, Tofu stands on the left of it, and the chipmunk sits on the right of it, {FULL}. "
  "The chipmunk scurries to the hole and slips straight into it through the open hole, its puffed head going in without bumping; its body follows only through the open hole, and last its fluffy tail disappears into the hole. "
  "No part of the chipmunk ever shows through the snow wall. Tofu cheers, flapping both flippers and hopping on the snow. "
  "At the end of the clip the chipmunk is inside its burrow and out of sight, the wide round hole is dark and empty at the front, and Tofu stands happily on the left of the hole.",
  "Sounds: quick tiny paw patters on snow, a happy chipmunk squeak echoing softly from inside the burrow, cheerful penguin peeps and flapping, soft winter wind."),
 ("medium close two-shot at snow level of Tofu on the left and the wide burrow hole on the right",
  "In the very first frame Tofu stands on the snow on the left of the wide round burrow hole, and the hole is dark and empty at the front. "
  f"The chipmunk's head pops back out of the hole through the open hole, {FULL} again, and it climbs out onto the snow on the right of the hole and of Tofu. "
  "It looks up at Tofu with big grateful eyes and does a happy little wiggle, its puffed cheeks wobbling. Tofu smiles proudly. "
  "At the end of the clip the chipmunk stands on the snow on the right with its cheeks still puffed, looking up at Tofu, and Tofu stands on the left, smiling.",
  "Sounds: a soft rustle at the burrow hole, a happy chipmunk chirp, a proud penguin peep, soft winter wind."),
 ("medium close two-shot at snow level of Tofu on the left and the chipmunk on the right, the wide burrow hole behind them",
  f"In the very first frame Tofu stands on the snow on the left and the chipmunk stands on the low snow bank on the right, a little higher than Tofu, {FULL}. "
  "As a thank-you the chipmunk leans over Tofu's head and spits out all the seeds from its cheeks, ptoo-ptoo-ptoo; a little shower of striped sunflower seeds falls down onto the top of Tofu's yellow beanie and piles up there in a small heap, and its cheeks become small and flat. "
  "The seeds only land on the outside of the beanie and stay on top of it; the beanie stays on Tofu's head the whole time. "
  "Tofu stands perfectly still with a completely flat, deadpan face, the heap of seeds on his beanie, while the chipmunk chirps happily. At the end of the clip Tofu stands deadpan on the left with seeds piled on his beanie, and the chipmunk sits on the snow bank on the right with flat cheeks, proud.",
  "Sounds: quick little ptoo spitting sounds, tiny seeds pattering on knitted wool, a happy chipmunk chirp, one flat little penguin peep, soft winter wind."),
]


def mochi(i):
    cam, act, audio = M[i]
    return M_HEAD.format(cam=cam) + M_CHAR + M_KITCHEN + M_MUG + M_SOLID + act + " " + audio + " " + M_TAIL


def tofu(i):
    cam, act, audio = T[i]
    return T_HEAD.format(cam=cam) + T_PARK + T_CHAR + T_HOLE + T_SOLID + act + " " + audio + " " + T_TAIL


if __name__ == "__main__":
    here = pathlib.Path(__file__).parent
    for name, fn, hdr, folder in [
        ("story-mochi-54.txt", mochi, '# Mochi #54 "He Was Stuck in the Mug... So Mochi Pulled Him Out" (2026-11-26). @Mochi on all. Twist: the armadillo walks right back into the mug and curls up; Mochi deadpan. Side animal: baby armadillo. One opaque blue ceramic mug.', "20261126_mochi54"),
        ("story-tofu-49.txt", tofu, '# Tofu #49 "He Couldn\'t Fit Into His Burrow... So Tofu Made It Bigger" (2026-11-26). Twist: the chipmunk spits all its cheek seeds onto Tofu\'s beanie as thanks; Tofu deadpan. Side animal: baby chipmunk.', "20261126_tofu49"),
    ]:
        out = [hdr, ""]
        for i in range(6):
            p = fn(i)
            low = p.lower()
            assert not re.search(r"\b(bells?|chimes?|ringing|hat|hats|clothing|clothes|sweater|wearing)\b", low.replace("wearing a yellow knitted beanie", "")), (name, i)
            out += [f"# s{i+1}", p, ""]
            (W / folder / f"p{i+1}.txt").write_text(p)
        (here / name).write_text("\n".join(out))
    print("ok")
