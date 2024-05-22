import json
from os import getenv
from whatsapp import WhatsApp
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    messenger = WhatsApp(token=getenv("TOKEN"),
                         phone_number_id=getenv("PHONE_NUMBER_ID"))



    def send_link(image_url: str, link_label: str, body: str | None, link: str, phone: str, footer: str | None = None) -> None:
        response = messenger.send_cta_url(
            recipient_id=phone,
            cta_url={
                "type": "cta_url",
                "header": {
                    "type": "image",
                    "image": {
                        "link": image_url
                    }
                },
                "body": {
                    "text": body
                },
                "footer": {
                    "text": footer
                },
                "action": {
                    "name": "cta_url",
                    "parameters": {
                        "display_text": link_label,
                        "url": link
                    }
                }                
            }
        )
        
        return response


    # res = send_link(header="Hello", body="World", buttons=[], phone=getenv("RECIPIENT_PHONE"), footer="Goodbye")
    
    res = send_link(
        image_url="https://firebasestorage.googleapis.com/v0/b/numichat.appspot.com/o/Raas%2FTemplate_images%2F2_ENG.jpg?alt=media&token=7a323913-8c57-4977-9147-3fb9b2a66d6a", 
        link_label="Book Now",
        body="Tap the button below to see available dates.", 
        link="https://www.google.com", 
        phone=getenv("RECIPIENT_PHONE"), 
        footer="Dates subject to change."
    )
    
    print(res)

    
