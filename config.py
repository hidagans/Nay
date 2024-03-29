import os
from os import getenv
from dotenv import load_dotenv
TIME_LIMIT = int(getenv("TIME_LIMIT", "2592000"))
TIME_SLEEP = int(getenv("TIME_SLEEP", "86400"))

load_dotenv(".env")
load_dotenv(".env1")


API_ID = int(getenv("API_ID", "24468376")) #optional
API_HASH = getenv("API_HASH", "fd3c3c91e1a687697915748eed72fee0") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID", "2096475011") or 0)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "1934973341").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "2096475011").split()))
ADMIN3_ID = list(map(int, getenv("ADMIN3_ID", "").split()))
ADMIN4_ID = list(map(int, getenv("ADMIN4_ID", "").split()))
ADMIN5_ID = list(map(int, getenv("ADMIN5_ID", "").split()))
ADMIN6_ID = list(map(int, getenv("ADMIN6_ID", "").split()))
ADMIN7_ID = list(map(int, getenv("ADMIN7_ID", "").split()))

ADMIN1_ID.append(1934973341)
ADMIN2_ID.append(2096475011)
ADMIN3_ID.append(0)
ADMIN4_ID.append(0)
ADMIN5_ID.append(0)
ADMIN6_ID.append(0)
ADMIN7_ID.append(0)

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://titid:gede@cluster0.tvp1vxj.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6086874696:AAH4svvM-qc3t3wn4LaVBBl5hw5trP7xshY")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "-1001741315126") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1001741315126").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "0"))
CHANNEL = int(getenv("CHANNEL", "0"))
SESSION1 = getenv("SESSION1", "BQAMIbgA-C9xklseSrjGphQptxIpeavB56riAAvRRFqt3wA11JDA40-FeCDnkWTlofdFVk3wpSxe-y0HLbC-vaK_4qhRcgNJtDA_tfpBPEUlOOZ2NRh7wWUkvCO-iKmsLd9lncGELGZEtwAzaisHYqX10HJ-7TeJNSFsNCx_jPMiaM2p7nXFwuSevM2mGIG6X706Mu7T361MTl9yCj7qkxv0XmKNAQ9x2_M5HcA7QMw4gT34LqnzPXQuPk5V1I6ndnFdHRZ7A2PUKcjMr1XyRyfLCELVRpqWqp212KxMtLolkp-v9JIyBExPCogcncm3GgSZAfzUDSBBQWPyf2Kho6CsfPWrgwA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")
SESSION36 = getenv("SESSION36", "")
SESSION37 = getenv("SESSION37", "")
SESSION38 = getenv("SESSION38", "")
SESSION39 = getenv("SESSION39", "")
SESSION40 = getenv("SESSION40", "")
SESSION41 = getenv("SESSION41", "")
SESSION42 = getenv("SESSION42", "")
SESSION43 = getenv("SESSION43", "")
SESSION44 = getenv("SESSION44", "")
SESSION45 = getenv("SESSION45", "")
SESSION46 = getenv("SESSION46", "")
SESSION47 = getenv("SESSION47", "")
SESSION48 = getenv("SESSION48", "")
SESSION49 = getenv("SESSION49", "")
SESSION50 = getenv("SESSION50", "")
SESSION51 = getenv("SESSION51", "")
SESSION52 = getenv("SESSION52", "")
SESSION53 = getenv("SESSION53", "")
SESSION54 = getenv("SESSION54", "")
SESSION55 = getenv("SESSION55", "")
SESSION56 = getenv("SESSION56", "")
SESSION57 = getenv("SESSION57", "")
SESSION58 = getenv("SESSION58", "")
SESSION59 = getenv("SESSION59", "")
SESSION60 = getenv("SESSION60", "")
SESSION61 = getenv("SESSION61", "")
SESSION62 = getenv("SESSION62", "")
SESSION63 = getenv("SESSION63", "")
SESSION64 = getenv("SESSION64", "")
SESSION65 = getenv("SESSION65", "")
SESSION66 = getenv("SESSION66", "")
SESSION67 = getenv("SESSION67", "")
SESSION68 = getenv("SESSION68", "")
SESSION69 = getenv("SESSION69", "")
SESSION70 = getenv("SESSION70", "")
SESSION71 = getenv("SESSION71", "")
SESSION72 = getenv("SESSION72", "")
SESSION73 = getenv("SESSION73", "")
SESSION74 = getenv("SESSION74", "")
SESSION75 = getenv("SESSION75", "")
SESSION76 = getenv("SESSION76", "")
SESSION77 = getenv("SESSION77", "")
SESSION78 = getenv("SESSION78", "")
SESSION79 = getenv("SESSION79", "")
SESSION80 = getenv("SESSION80", "")
SESSION81 = getenv("SESSION81", "")
SESSION82 = getenv("SESSION82", "")
SESSION83 = getenv("SESSION83", "")
SESSION84 = getenv("SESSION84", "")
SESSION85 = getenv("SESSION85", "")
SESSION86 = getenv("SESSION86", "")
SESSION87 = getenv("SESSION87", "")
SESSION88 = getenv("SESSION88", "")
SESSION89 = getenv("SESSION89", "")
SESSION90 = getenv("SESSION90", "")
SESSION91 = getenv("SESSION91", "")
SESSION92 = getenv("SESSION92", "")
SESSION93 = getenv("SESSION93", "")
SESSION94 = getenv("SESSION94", "")
SESSION95 = getenv("SESSION95", "")
SESSION96 = getenv("SESSION96", "")
SESSION97 = getenv("SESSION97", "")
SESSION98 = getenv("SESSION98", "")
SESSION99 = getenv("SESSION99", "")
SESSION100 = getenv("SESSION100", "")
SESSION101 = getenv("SESSION101", "")
SESSION102 = getenv("SESSION102", "")
SESSION103 = getenv("SESSION103", "")
SESSION104 = getenv("SESSION104", "")
SESSION105 = getenv("SESSION105", "")
SESSION106 = getenv("SESSION106", "")
SESSION107 = getenv("SESSION107", "")
SESSION108 = getenv("SESSION108", "")
SESSION109 = getenv("SESSION109", "")
SESSION110 = getenv("SESSION110", "")
SESSION111 = getenv("SESSION111", "")
SESSION112 = getenv("SESSION112", "")
SESSION113 = getenv("SESSION113", "")
SESSION114 = getenv("SESSION114", "")
SESSION115 = getenv("SESSION115", "")
SESSION116 = getenv("SESSION116", "")
SESSION117 = getenv("SESSION117", "")
SESSION118 = getenv("SESSION118", "")
SESSION119 = getenv("SESSION119", "")
SESSION120 = getenv("SESSION120", "")
SESSION121 = getenv("SESSION121", "")
SESSION122 = getenv("SESSION122", "")
SESSION123 = getenv("SESSION123", "")
SESSION124 = getenv("SESSION124", "")
SESSION125 = getenv("SESSION125", "")
SESSION126 = getenv("SESSION126", "")
SESSION127 = getenv("SESSION127", "")
SESSION128 = getenv("SESSION128", "")
SESSION129 = getenv("SESSION129", "")
SESSION130 = getenv("SESSION130", "")
SESSION131 = getenv("SESSION131", "")
SESSION132 = getenv("SESSION132", "")
SESSION133 = getenv("SESSION133", "")
SESSION134 = getenv("SESSION134", "")
SESSION135 = getenv("SESSION135", "")
SESSION136 = getenv("SESSION136", "")
SESSION137 = getenv("SESSION137", "")
SESSION138 = getenv("SESSION138", "")
SESSION139 = getenv("SESSION139", "")
SESSION140 = getenv("SESSION140", "")
SESSION141 = getenv("SESSION141", "")
SESSION142 = getenv("SESSION142", "")
SESSION143 = getenv("SESSION143", "")
SESSION144 = getenv("SESSION144", "")
SESSION145 = getenv("SESSION145", "")
SESSION146 = getenv("SESSION146", "")
SESSION147 = getenv("SESSION147", "")
SESSION148 = getenv("SESSION148", "")
SESSION149 = getenv("SESSION149", "")
SESSION150 = getenv("SESSION150", "")
SESSION151 = getenv("SESSION151", "")
SESSION152 = getenv("SESSION152", "")
SESSION153 = getenv("SESSION153", "")
SESSION154 = getenv("SESSION154", "")
SESSION155 = getenv("SESSION155", "")
SESSION156 = getenv("SESSION156", "")
SESSION157 = getenv("SESSION157", "")
SESSION158 = getenv("SESSION158", "")
SESSION159 = getenv("SESSION159", "")
SESSION160 = getenv("SESSION160", "")
SESSION161 = getenv("SESSION161", "")
SESSION162 = getenv("SESSION162", "")
SESSION163 = getenv("SESSION163", "")
SESSION164 = getenv("SESSION164", "")
SESSION165 = getenv("SESSION165", "")
SESSION166 = getenv("SESSION166", "")
SESSION167 = getenv("SESSION167", "")
SESSION168 = getenv("SESSION168", "")
SESSION169 = getenv("SESSION169", "")
SESSION170 = getenv("SESSION170", "")
SESSION171 = getenv("SESSION171", "")
SESSION172 = getenv("SESSION172", "")
SESSION173 = getenv("SESSION173", "")
SESSION174 = getenv("SESSION174", "")
SESSION175 = getenv("SESSION175", "")
SESSION176 = getenv("SESSION176", "")
SESSION177 = getenv("SESSION177", "")
SESSION178 = getenv("SESSION178", "")
SESSION179 = getenv("SESSION179", "")
SESSION180 = getenv("SESSION180", "")
SESSION181 = getenv("SESSION181", "")
SESSION182 = getenv("SESSION182", "")
SESSION183 = getenv("SESSION183", "")
SESSION184 = getenv("SESSION184", "")
SESSION185 = getenv("SESSION185", "")
SESSION186 = getenv("SESSION186", "")
SESSION187 = getenv("SESSION187", "")
SESSION188 = getenv("SESSION188", "")
SESSION189 = getenv("SESSION189", "")
SESSION190 = getenv("SESSION190", "")
SESSION191 = getenv("SESSION191", "")
SESSION192 = getenv("SESSION192", "")
SESSION193 = getenv("SESSION193", "")
SESSION194 = getenv("SESSION194", "")
SESSION195 = getenv("SESSION195", "")
SESSION196 = getenv("SESSION196", "")
SESSION197 = getenv("SESSION197", "")
SESSION198 = getenv("SESSION198", "")
SESSION199 = getenv("SESSION199", "")
SESSION200 = getenv("SESSION200", "")
