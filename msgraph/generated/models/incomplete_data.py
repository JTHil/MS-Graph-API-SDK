from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class IncompleteData(AdditionalDataHolder, Parsable):
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
        Instantiates a new incompleteData and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The service does not have source data before the specified time.
        self._missing_data_before_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Some data was not recorded due to excessive activity.
        self._was_throttled: Optional[bool] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IncompleteData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IncompleteData
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IncompleteData()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "missing_data_before_date_time": lambda n : setattr(self, 'missing_data_before_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "was_throttled": lambda n : setattr(self, 'was_throttled', n.get_bool_value()),
        }
        return fields

    @property
    def missing_data_before_date_time(self,) -> Optional[datetime]:
        """
        Gets the missingDataBeforeDateTime property value. The service does not have source data before the specified time.
        Returns: Optional[datetime]
        """
        return self._missing_data_before_date_time

    @missing_data_before_date_time.setter
    def missing_data_before_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the missingDataBeforeDateTime property value. The service does not have source data before the specified time.
        Args:
            value: Value to set for the missingDataBeforeDateTime property.
        """
        self._missing_data_before_date_time = value

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
        writer.write_datetime_value("missingDataBeforeDateTime", self.missing_data_before_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("wasThrottled", self.was_throttled)
        writer.write_additional_data_value(self.additional_data)

    @property
    def was_throttled(self,) -> Optional[bool]:
        """
        Gets the wasThrottled property value. Some data was not recorded due to excessive activity.
        Returns: Optional[bool]
        """
        return self._was_throttled

    @was_throttled.setter
    def was_throttled(self,value: Optional[bool] = None) -> None:
        """
        Sets the wasThrottled property value. Some data was not recorded due to excessive activity.
        Args:
            value: Value to set for the wasThrottled property.
        """
        self._was_throttled = value


