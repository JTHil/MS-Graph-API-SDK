from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .date_time_time_zone import DateTimeTimeZone
    from .locale_info import LocaleInfo

@dataclass
class AutomaticRepliesMailTips(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The automatic reply message.
    message: Optional[str] = None
    # The language that the automatic reply message is in.
    message_language: Optional[LocaleInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time that automatic replies are set to end.
    scheduled_end_time: Optional[DateTimeTimeZone] = None
    # The date and time that automatic replies are set to begin.
    scheduled_start_time: Optional[DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AutomaticRepliesMailTips:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomaticRepliesMailTips
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AutomaticRepliesMailTips()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .date_time_time_zone import DateTimeTimeZone
        from .locale_info import LocaleInfo

        from .date_time_time_zone import DateTimeTimeZone
        from .locale_info import LocaleInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "messageLanguage": lambda n : setattr(self, 'message_language', n.get_object_value(LocaleInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scheduledEndTime": lambda n : setattr(self, 'scheduled_end_time', n.get_object_value(DateTimeTimeZone)),
            "scheduledStartTime": lambda n : setattr(self, 'scheduled_start_time', n.get_object_value(DateTimeTimeZone)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("message", self.message)
        writer.write_object_value("messageLanguage", self.message_language)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("scheduledEndTime", self.scheduled_end_time)
        writer.write_object_value("scheduledStartTime", self.scheduled_start_time)
        writer.write_additional_data_value(self.additional_data)
    

