sms_dict = {
    "uri": "https://platform.ringcentral.com/restapi/v1.0/account/401928394008/extension/401928394008/message-store?direction=Inbound&readStatus=Unread&availability=Alive&dateFrom=2018-09-17T12:53:00.000Z&page=1&perPage=2",
    "records": [
        {
            "uri": "https://platform.ringcentral.com/restapi/v1.0/account/401928394008/extension/401928394008/message-store/402406986008",
            "id": 402406986008,
            "to": [{"name": "Jane Smith"}],
            "from": {"phoneNumber": "+18888984591", "name": "RingCentral"},
            "type": "VoiceMail",
            "creationTime": "2018-09-18T09:24:04.000Z",
            "readStatus": "Unread",
            "priority": "Normal",
            "attachments": [
                {
                    "id": 402406986008,
                    "uri": "https://platform.ringcentral.com/restapi/v1.0/account/401928394008/extension/401928394008/message-store/402406986008/content/402406986008",
                    "type": "AudioRecording",
                    "contentType": "audio/x-wav",
                    "vmDuration": 42,
                }
            ],
            "direction": "Inbound",
            "availability": "Alive",
            "subject": "Welcome to RingCentral!",
            "messageStatus": "Received",
            "lastModifiedTime": "2018-09-18T09:24:04.102Z",
            "vmTranscriptionStatus": "NotAvailable",
        },
        {
            "uri": "https://platform.ringcentral.com/restapi/v1.0/account/401928394008/extension/401928394008/message-store/402406984008",
            "id": 402406984008,
            "to": [{"name": "Jane Smith"}],
            "from": {"phoneNumber": "+18442058517", "name": "RingCentral"},
            "type": "VoiceMail",
            "creationTime": "2018-09-18T09:24:03.000Z",
            "readStatus": "Unread",
            "priority": "Normal",
            "attachments": [
                {
                    "id": 402406984008,
                    "uri": "https://platform.ringcentral.com/restapi/v1.0/account/401928394008/extension/401928394008/message-store/402406984008/content/402406984008",
                    "type": "AudioRecording",
                    "contentType": "audio/x-wav",
                    "vmDuration": 25,
                }
            ],
            "direction": "Inbound",
            "availability": "Alive",
            "messageStatus": "Received",
            "lastModifiedTime": "2018-09-18T09:24:03.531Z",
            "vmTranscriptionStatus": "NotAvailable",
        },
    ],
    "paging": {
        "page": 1,
        "totalPages": 1,
        "perPage": 2,
        "totalElements": 2,
        "pageStart": 0,
        "pageEnd": 1,
    },
    "navigation": {
        "firstPage": {
            "uri": "https://platform.ringcentral.com/restapi/v1.0/account/401928394008/extension/401928394008/message-store?direction=Inbound&readStatus=Unread&availability=Alive&dateFrom=2018-09-17T12:53:00.000Z&page=1&perPage=2"
        },
        "lastPage": {
            "uri": "https://platform.ringcentral.com/restapi/v1.0/account/401928394008/extension/401928394008/message-store?direction=Inbound&readStatus=Unread&availability=Alive&dateFrom=2018-09-17T12:53:00.000Z&page=1&perPage=2"
        },
    },
}
