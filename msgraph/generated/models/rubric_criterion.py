from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import education_item_body

class RubricCriterion(AdditionalDataHolder, Parsable):
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
        Instantiates a new rubricCriterion and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The description of this criterion.
        self._description: Optional[education_item_body.EducationItemBody] = None
        # The OdataType property
        self._odata_type: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RubricCriterion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RubricCriterion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RubricCriterion()

    @property
    def description(self,) -> Optional[education_item_body.EducationItemBody]:
        """
        Gets the description property value. The description of this criterion.
        Returns: Optional[education_item_body.EducationItemBody]
        """
        return self._description

    @description.setter
    def description(self,value: Optional[education_item_body.EducationItemBody] = None) -> None:
        """
        Sets the description property value. The description of this criterion.
        Args:
            value: Value to set for the description property.
        """
        self._description = value

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_object_value(education_item_body.EducationItemBody)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields

    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type

    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("description", self.description)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)


