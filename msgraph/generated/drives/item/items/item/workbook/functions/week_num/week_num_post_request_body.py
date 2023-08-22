from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class WeekNumPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The returnType property
    return_type: Optional[Json] = None
    # The serialNumber property
    serial_number: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WeekNumPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WeekNumPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WeekNumPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "returnType": lambda n : setattr(self, 'return_type', n.get_object_value(Json)),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_object_value(Json)),
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
        writer.write_object_value("returnType", self.return_type)
        writer.write_object_value("serialNumber", self.serial_number)
        writer.write_additional_data_value(self.additional_data)
    

