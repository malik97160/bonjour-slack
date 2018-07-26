from slackclient import SlackClient
# id de maxime U03TYB40R
# id de jraby U1EDHP2LA
# id de sylvain U1CP6JZCM
# id du groupe GBX2YBGN4
slack_token = "xoxp-3948371181-3949249413-405061166576-3cd0f70f2e3ab9f5edaa1653992510a3"
sc = SlackClient(slack_token)
sc.api_call(
  "chat.postMessage",
  channel="GBX2YBGN4",
  text="Prem's https://78.media.tumblr.com/7657937ccdda01b61b44121090121b80/tumblr_pc22zokzqy1v1wvcuo1_1280.jpg",
  as_user=1
)