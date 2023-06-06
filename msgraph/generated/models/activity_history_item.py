from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, status, user_activity

from . import entity

@dataclass
class ActivityHistoryItem(entity.Entity):
    # Optional. The duration of active user engagement. if not supplied, this is calculated from the startedDateTime and lastActiveDateTime.
    active_duration_seconds: Optional[int] = None
    # The activity property
    activity: Optional[user_activity.UserActivity] = None
    # Set by the server. DateTime in UTC when the object was created on the server.
    created_date_time: Optional[datetime] = None
    # Optional. UTC DateTime when the historyItem will undergo hard-delete. Can be set by the client.
    expiration_date_time: Optional[datetime] = None
    # Optional. UTC DateTime when the historyItem (activity session) was last understood as active or finished - if null, historyItem status should be Ongoing.
    last_active_date_time: Optional[datetime] = None
    # Set by the server. DateTime in UTC when the object was modified on the server.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Required. UTC DateTime when the historyItem (activity session) was started. Required for timeline history.
    started_date_time: Optional[datetime] = None
    # Set by the server. A status code used to identify valid objects. Values: active, updated, deleted, ignored.
    status: Optional[status.Status] = None
    # Optional. The timezone in which the user's device used to generate the activity was located at activity creation time. Values supplied as Olson IDs in order to support cross-platform representation.
    user_timezone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActivityHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ActivityHistoryItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ActivityHistoryItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, status, user_activity

        fields: Dict[str, Callable[[Any], None]] = {
            "activeDurationSeconds": lambda n : setattr(self, 'active_duration_seconds', n.get_int_value()),
            "activity": lambda n : setattr(self, 'activity', n.get_object_value(user_activity.UserActivity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "lastActiveDateTime": lambda n : setattr(self, 'last_active_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(status.Status)),
            "userTimezone": lambda n : setattr(self, 'user_timezone', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("activeDurationSeconds", self.active_duration_seconds)
        writer.write_object_value("activity", self.activity)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("lastActiveDateTime", self.last_active_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userTimezone", self.user_timezone)
    

