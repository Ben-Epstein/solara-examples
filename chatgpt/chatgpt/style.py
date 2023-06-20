# Base Page component
main_css = """
    .main {
        width: 100%;
        height: 100%;
        max-width: 1200px;
        margin: auto;
        padding: 1em;
    }
"""


chat_css = """
    .chat-input {
        max-width: 800px;
    })
"""


chatbox_css = """
.message {
    max-width: 450px;
    width: 100%;
}

.system-message, .system-message > * {
    background-color: #ffffff !important;
}

.user-message, .user-message > * {
    background-color: #f0f0f0 !important;
}

.assistant-message, .assistant-message > * {
    background-color: #9ab2e9 !important;
}

.avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 2px solid transparent;
  overflow: hidden;
  display: flex;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
"""
