# samepy
A SAME encoder written in python


## What is SAME?
 SAME stands for Specific Area Message Encoding (see https://en.wikipedia.org/wiki/Specific_Area_Message_Encoding) that is used to encode messages in EAS and NWR transmissions. 
SAME-encoded data is presented as a pair of AFSK data bursts, one a message header encoding the essentials of the alert, and the other being the End of Message. The SAME messages contain ASCII bytes that contain info on alerts such as the type, how long will it be in effect, and where the affected location is. Due to SAME not being capable of error correction, the header and EOM are repeated 3 times for a decoder to pick the best two out of three.

The text of the header is a fixed format:
`<Preamble>ZCZC-ORG-EEE-PSSCCC+TTTT-JJJHHMM-LLLLLLLL-`

1. Preamble is a binary of 10101011 (0xAB in hex, or 171 in decimal) that is repeated 16 times for receiver calibration
2. The text `ZCZC` is an attention message to the decoder.
3. `ORG` Originator code, this is programmed per unit when put into operation. Weather related alerts would originate from WXR for example.
4. `EEE` Event code; programmed at the time of the event.
5. `PSSCCC` Location code.
6. `TTTT` Purge time of the event, format is HHMM
7. `JJJHHMM` Date and time of the event in UTC.
8. `LLLLLLLL` Eight character station callsign.
