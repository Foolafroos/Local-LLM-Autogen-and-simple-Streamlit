import asyncio

import streamlit as st
from autogen import AssistantAgent, UserProxyAgent

st.write("""# Talk with your Autogen Agent""")


class TrackableAssistantAgent(AssistantAgent):
    def _process_received_message(self, message, sender, silent):
        with st.chat_message(sender.name):
            st.markdown(message)
        return super()._process_received_message(message, sender, silent)


class TrackableUserProxyAgent(UserProxyAgent):
    def _process_received_message(self, message, sender, silent):
        with st.chat_message(sender.name):
            st.markdown(message)
        return super()._process_received_message(message, sender, silent)


selected_model = None
selected_key = None
with st.sidebar:
    st.image("Foolafroos.png",)
    st.header("Made with Love",)


# for message in st.session_state["messages"]:
#    st.markdown(message)

user_input = st.chat_input("Type something...")
if user_input:
    llm_config = {
        "config_list": [
            {
                "base_url": "http://localhost:1234/v1",
                "api_key": "NULL",
            },
        ],
    }
    # create an AssistantAgent instance named "assistant"
    assistant = TrackableAssistantAgent(name="assistant", llm_config=llm_config)

    # create a UserProxyAgent instance named "user"
    user_proxy = TrackableUserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: x.get("content", "")
        .rstrip()
        .endswith("TERMINATE"),
        code_execution_config={"work_dir": "web"},
        llm_config=llm_config,
        system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
    )

    # Create an event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Define an asynchronous function
    async def initiate_chat():
        await user_proxy.a_initiate_chat(
            assistant,
            message=user_input,
        )

    # Run the asynchronous function within the event loop
    loop.run_until_complete(initiate_chat())
