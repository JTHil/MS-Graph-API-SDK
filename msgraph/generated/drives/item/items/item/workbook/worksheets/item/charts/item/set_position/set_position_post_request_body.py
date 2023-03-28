from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class SetPositionPostRequestBody(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new setPositionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The endCell property
        self._end_cell: Optional[json.Json] = None
        # The startCell property
        self._start_cell: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetPositionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SetPositionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SetPositionPostRequestBody()
    
    @property
    def end_cell(self,) -> Optional[json.Json]:
        """
        Gets the endCell property value. The endCell property
        Returns: Optional[json.Json]
        """
        return self._end_cell
    
    @end_cell.setter
    def end_cell(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the endCell property value. The endCell property
        Args:
            value: Value to set for the end_cell property.
        """
        self._end_cell = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "endCell": lambda n : setattr(self, 'end_cell', n.get_object_value(json.Json)),
            "startCell": lambda n : setattr(self, 'start_cell', n.get_object_value(json.Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("endCell", self.end_cell)
        writer.write_object_value("startCell", self.start_cell)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_cell(self,) -> Optional[json.Json]:
        """
        Gets the startCell property value. The startCell property
        Returns: Optional[json.Json]
        """
        return self._start_cell
    
    @start_cell.setter
    def start_cell(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the startCell property value. The startCell property
        Args:
            value: Value to set for the start_cell property.
        """
        self._start_cell = value
    

