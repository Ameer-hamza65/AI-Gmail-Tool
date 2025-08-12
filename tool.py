from langchain_google_community.gmail.send_message import GmailSendMessage
from langchain_google_community.gmail.create_draft import GmailCreateDraft
from langchain_google_community.gmail.get_message import GmailGetMessage
from langchain_google_community.gmail.search import GmailSearch

tool1= GmailSendMessage()
tool2=GmailSearch()
tool3=GmailCreateDraft()
tool4=GmailGetMessage()
tools=[tool1, tool2, tool3, tool4]
