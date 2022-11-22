from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class PasswordCredential(AdditionalDataHolder, Parsable):
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
        Instantiates a new passwordCredential and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Do not use.
        self._custom_key_identifier: Optional[bytes] = None
        # Friendly name for the password. Optional.
        self._display_name: Optional[str] = None
        # The date and time at which the password expires represented using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        self._end_date_time: Optional[datetime] = None
        # Contains the first three characters of the password. Read-only.
        self._hint: Optional[str] = None
        # The unique identifier for the password.
        self._key_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Read-only; Contains the strong passwords generated by Azure AD that are 16-64 characters in length. The generated password value is only returned during the initial POST request to addPassword. There is no way to retrieve this password in the future.
        self._secret_text: Optional[str] = None
        # The date and time at which the password becomes valid. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        self._start_date_time: Optional[datetime] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PasswordCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PasswordCredential
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PasswordCredential()

    @property
    def custom_key_identifier(self,) -> Optional[bytes]:
        """
        Gets the customKeyIdentifier property value. Do not use.
        Returns: Optional[bytes]
        """
        return self._custom_key_identifier

    @custom_key_identifier.setter
    def custom_key_identifier(self,value: Optional[bytes] = None) -> None:
        """
        Sets the customKeyIdentifier property value. Do not use.
        Args:
            value: Value to set for the customKeyIdentifier property.
        """
        self._custom_key_identifier = value

    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Friendly name for the password. Optional.
        Returns: Optional[str]
        """
        return self._display_name

    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Friendly name for the password. Optional.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value

    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The date and time at which the password expires represented using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        Returns: Optional[datetime]
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The date and time at which the password expires represented using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custom_key_identifier": lambda n : setattr(self, 'custom_key_identifier', n.get_bytes_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "hint": lambda n : setattr(self, 'hint', n.get_str_value()),
            "key_id": lambda n : setattr(self, 'key_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "secret_text": lambda n : setattr(self, 'secret_text', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        return fields

    @property
    def hint(self,) -> Optional[str]:
        """
        Gets the hint property value. Contains the first three characters of the password. Read-only.
        Returns: Optional[str]
        """
        return self._hint

    @hint.setter
    def hint(self,value: Optional[str] = None) -> None:
        """
        Sets the hint property value. Contains the first three characters of the password. Read-only.
        Args:
            value: Value to set for the hint property.
        """
        self._hint = value

    @property
    def key_id(self,) -> Optional[str]:
        """
        Gets the keyId property value. The unique identifier for the password.
        Returns: Optional[str]
        """
        return self._key_id

    @key_id.setter
    def key_id(self,value: Optional[str] = None) -> None:
        """
        Sets the keyId property value. The unique identifier for the password.
        Args:
            value: Value to set for the keyId property.
        """
        self._key_id = value

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

    @property
    def secret_text(self,) -> Optional[str]:
        """
        Gets the secretText property value. Read-only; Contains the strong passwords generated by Azure AD that are 16-64 characters in length. The generated password value is only returned during the initial POST request to addPassword. There is no way to retrieve this password in the future.
        Returns: Optional[str]
        """
        return self._secret_text

    @secret_text.setter
    def secret_text(self,value: Optional[str] = None) -> None:
        """
        Sets the secretText property value. Read-only; Contains the strong passwords generated by Azure AD that are 16-64 characters in length. The generated password value is only returned during the initial POST request to addPassword. There is no way to retrieve this password in the future.
        Args:
            value: Value to set for the secretText property.
        """
        self._secret_text = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("customKeyIdentifier", self.custom_key_identifier)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("hint", self.hint)
        writer.write_str_value("keyId", self.key_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("secretText", self.secret_text)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)

    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The date and time at which the password becomes valid. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        Returns: Optional[datetime]
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The date and time at which the password becomes valid. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value


