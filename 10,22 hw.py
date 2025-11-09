import requests
from PIL import Image
from io import BytesIO
HF_API_KEY="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"
URL="https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"

def generate_image(prompt:str)->Image.Image:
    headers={"Authorization": f"Bearer {HF_API_KEY}"}
    payload={"inputs": prompt}

    try:
        response=requests.post(URL, headers=headers, json=payload, timeout=30)
        if "image" in response.headers.get('Content-Type', ""):
            image=Image.open(BytesIO(response.content))
            return image
        else:
            raise Exception ("the response is not an image")
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
    


def main():
    print("Welcome to Text-image generator, type exit to quit program")
    while True:
        prompt=input("enter desc. for image you want to generate.").strip()
        if prompt.lower()=="exit":
            print("good bye...")
            break
        print("generating...")
        try:
            image=generate_image(prompt)
            image.show()

            save_option=input("do u want to save this file (yes.no)").strip()
            if save_option=="yes":
                file_name="".john(c for  c in file_name if c.isalnum() or c in ("_", "-")).strip()
                image.save(f"{file_name}.png")
                print("saved")
        except Exception as e:
            print ("an error occured", e)
        print("-"*80)

if __name__=="__main__":
    main()

