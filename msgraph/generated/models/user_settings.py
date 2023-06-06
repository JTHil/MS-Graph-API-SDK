from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, shift_preferences

from . import entity

@dataclass
class UserSettings(entity.Entity):
    # The contributionToContentDiscoveryAsOrganizationDisabled property
    contribution_to_content_discovery_as_organization_disabled: Optional[bool] = None
    # The contributionToContentDiscoveryDisabled property
    contribution_to_content_discovery_disabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The shiftPreferences property
    shift_preferences: Optional[shift_preferences.ShiftPreferences] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, shift_preferences

        fields: Dict[str, Callable[[Any], None]] = {
            "contributionToContentDiscoveryAsOrganizationDisabled": lambda n : setattr(self, 'contribution_to_content_discovery_as_organization_disabled', n.get_bool_value()),
            "contributionToContentDiscoveryDisabled": lambda n : setattr(self, 'contribution_to_content_discovery_disabled', n.get_bool_value()),
            "shiftPreferences": lambda n : setattr(self, 'shift_preferences', n.get_object_value(shift_preferences.ShiftPreferences)),
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
        writer.write_bool_value("contributionToContentDiscoveryAsOrganizationDisabled", self.contribution_to_content_discovery_as_organization_disabled)
        writer.write_bool_value("contributionToContentDiscoveryDisabled", self.contribution_to_content_discovery_disabled)
        writer.write_object_value("shiftPreferences", self.shift_preferences)
    

