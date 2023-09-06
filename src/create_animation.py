from stability_sdk import api
from stability_sdk.utils import create_video_from_frames
from stability_sdk.animation import AnimationArgs, Animator
import tqdm

STABILITY_HOST = "grpc.stability.ai:443"
STABILITY_KEY = 'sk-kpQB5PiV36LBzY83lpVOcBCX6LrAKGCSojGNFTQP2ngGNQIp' 

context = api.Context(STABILITY_HOST, STABILITY_KEY)

def create_animation(animation_prompts, max_frames, out_dir, video_name):

    # Configure the animation
    args = AnimationArgs()
    args.interpolate_prompts = True
    args.locked_seed = True
    args.max_frames = max_frames
    args.seed = 42
    args.strength_curve = "0:(0)"
    args.diffusion_cadence_curve = "0:(4)"
    args.cadence_interp = "film"

    negative_prompt = "blurry, low resolution, bad quality"

    # Create Animator object to orchestrate the rendering
    animator = Animator(
        api_context=context,
        animation_prompts=animation_prompts,
        negative_prompt=negative_prompt,
        args=args,
        out_dir=out_dir
    )

    for _ in tqdm.tqdm(animator.render(), total=args.max_frames):
        pass

    create_video_from_frames(animator.out_dir, video_name, fps=12) # CAMBIAR FPS AQUÍ

    return