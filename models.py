import json
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from typing import Dict, Tuple, List

from dataclasses_json import dataclass_json, LetterCase, DataClassJsonMixin
from discord import TextChannel, Guild
from google.cloud import firestore
from google.cloud.firestore_v1 import Client as FSClient, DocumentReference


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ChannelDocument(DataClassJsonMixin):
    id: int
    guild: int
    name: str
    created_at: datetime


class FirestoreSpinoffModel:
    def __init__(self):

        # Project ID is determined by the GCLOUD_PROJECT environment variable
        cred_path = Path.cwd() / Path("SpinOffBot-f30ad158119a.json")
        self.firestore_db: FSClient = firestore.Client.from_service_account_json(
                                                       json_credentials_path=cred_path,
                                                       project="spinoffbot-299919")

    def store_spinoff_channel(self, channel: TextChannel):
        server: Guild = channel.guild
        collection_path: Tuple[str] = (f"{server.name}-{server.id}", )
        document_path: str = f"{channel.name}-{channel.id}"
        channel_store: DocumentReference = self.firestore_db.collection(collection_path).document(document_path)

        channel_doc: ChannelDocument = ChannelDocument(channel.id, channel.guild.id, channel.name, channel.created_at)

        channel_store.set(channel_doc.to_dict(encode_json=True), merge=True)

    def get_channels(self) -> List[ChannelDocument]:
        pass
