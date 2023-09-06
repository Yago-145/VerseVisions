import os
from generate_imgs import generate_imgs


def generate_streamlit_imgs(prompts_list, output_dir):
    cont = 0
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for prompt in prompts_list:
        generate_imgs(prompt, num_imgs=1, cont=cont, output_dir=output_dir)
        cont += 1

    return