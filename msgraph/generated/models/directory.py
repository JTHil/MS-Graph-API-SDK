from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import administrative_unit, attribute_set, custom_security_attribute_definition, directory_object, entity, identity_provider_base, on_premises_directory_synchronization

from . import entity

@dataclass
class Directory(entity.Entity):
    # Conceptual container for user and group directory objects.
    administrative_units: Optional[List[administrative_unit.AdministrativeUnit]] = None
    # Group of related custom security attribute definitions.
    attribute_sets: Optional[List[attribute_set.AttributeSet]] = None
    # Schema of a custom security attributes (key-value pairs).
    custom_security_attribute_definitions: Optional[List[custom_security_attribute_definition.CustomSecurityAttributeDefinition]] = None
    # Recently deleted items. Read-only. Nullable.
    deleted_items: Optional[List[directory_object.DirectoryObject]] = None
    # Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
    federation_configurations: Optional[List[identity_provider_base.IdentityProviderBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A container for on-premises directory synchronization functionalities that are available for the organization.
    on_premises_synchronization: Optional[List[on_premises_directory_synchronization.OnPremisesDirectorySynchronization]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Directory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Directory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Directory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import administrative_unit, attribute_set, custom_security_attribute_definition, directory_object, entity, identity_provider_base, on_premises_directory_synchronization

        fields: Dict[str, Callable[[Any], None]] = {
            "administrativeUnits": lambda n : setattr(self, 'administrative_units', n.get_collection_of_object_values(administrative_unit.AdministrativeUnit)),
            "attributeSets": lambda n : setattr(self, 'attribute_sets', n.get_collection_of_object_values(attribute_set.AttributeSet)),
            "customSecurityAttributeDefinitions": lambda n : setattr(self, 'custom_security_attribute_definitions', n.get_collection_of_object_values(custom_security_attribute_definition.CustomSecurityAttributeDefinition)),
            "deletedItems": lambda n : setattr(self, 'deleted_items', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "federationConfigurations": lambda n : setattr(self, 'federation_configurations', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
            "onPremisesSynchronization": lambda n : setattr(self, 'on_premises_synchronization', n.get_collection_of_object_values(on_premises_directory_synchronization.OnPremisesDirectorySynchronization)),
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
        writer.write_collection_of_object_values("administrativeUnits", self.administrative_units)
        writer.write_collection_of_object_values("attributeSets", self.attribute_sets)
        writer.write_collection_of_object_values("customSecurityAttributeDefinitions", self.custom_security_attribute_definitions)
        writer.write_collection_of_object_values("deletedItems", self.deleted_items)
        writer.write_collection_of_object_values("federationConfigurations", self.federation_configurations)
        writer.write_collection_of_object_values("onPremisesSynchronization", self.on_premises_synchronization)
    

