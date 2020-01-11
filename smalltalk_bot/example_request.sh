Request:

curl  -X POST \
-d '{"from":"Vlad", "channel_name":"random", "msg":"Hello, how are you?"}' \
http://localhost:8080

Response:

{
    "suggestions":[
        "Consider adding please to your questions to be more polite."
        ]
}