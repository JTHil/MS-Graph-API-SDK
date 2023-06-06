from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_identity, user_identity

@dataclass
class AuditActivityInitiator(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # If the resource initiating the activity is an app, this property indicates all the app related information like appId, Name, servicePrincipalId, Name.
    app: Optional[app_identity.AppIdentity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If the resource initiating the activity is a user, this property Indicates all the user related information like userId, Name, UserPrinicpalName.
    user: Optional[user_identity.UserIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditActivityInitiator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuditActivityInitiator
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuditActivityInitiator()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_identity, user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "app": lambda n : setattr(self, 'app', n.get_object_value(app_identity.AppIdentity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(user_identity.UserIdentity)),
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
        writer.write_object_value("app", self.app)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

