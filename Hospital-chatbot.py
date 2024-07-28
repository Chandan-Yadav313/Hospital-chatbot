import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("/content/hospital-chatbot.xml")
kernel.respond("load hospital chatbot")

# Press CTRL-C to break this loop
while True:
        input_txt= input(">You: ")
        response =kernel.respond(input_txt)    
        print(">Bot: "+response)