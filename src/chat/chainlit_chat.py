import chainlit as cl


@cl.on_message
async def chat(message: cl.Message):
    await cl.Message(content=f"{message.content}").send()
