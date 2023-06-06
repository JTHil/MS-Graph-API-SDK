from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import container_filter, group_filter, object_mapping, string_key_string_value_pair

@dataclass
class SynchronizationRule(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The containerFilter property
    container_filter: Optional[container_filter.ContainerFilter] = None
    # The editable property
    editable: Optional[bool] = None
    # The groupFilter property
    group_filter: Optional[group_filter.GroupFilter] = None
    # The id property
    id: Optional[str] = None
    # The metadata property
    metadata: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]] = None
    # The name property
    name: Optional[str] = None
    # The objectMappings property
    object_mappings: Optional[List[object_mapping.ObjectMapping]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The priority property
    priority: Optional[int] = None
    # The sourceDirectoryName property
    source_directory_name: Optional[str] = None
    # The targetDirectoryName property
    target_directory_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import container_filter, group_filter, object_mapping, string_key_string_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "containerFilter": lambda n : setattr(self, 'container_filter', n.get_object_value(container_filter.ContainerFilter)),
            "editable": lambda n : setattr(self, 'editable', n.get_bool_value()),
            "groupFilter": lambda n : setattr(self, 'group_filter', n.get_object_value(group_filter.GroupFilter)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(string_key_string_value_pair.StringKeyStringValuePair)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "objectMappings": lambda n : setattr(self, 'object_mappings', n.get_collection_of_object_values(object_mapping.ObjectMapping)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "sourceDirectoryName": lambda n : setattr(self, 'source_directory_name', n.get_str_value()),
            "targetDirectoryName": lambda n : setattr(self, 'target_directory_name', n.get_str_value()),
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
        writer.write_object_value("containerFilter", self.container_filter)
        writer.write_bool_value("editable", self.editable)
        writer.write_object_value("groupFilter", self.group_filter)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("objectMappings", self.object_mappings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("sourceDirectoryName", self.source_directory_name)
        writer.write_str_value("targetDirectoryName", self.target_directory_name)
        writer.write_additional_data_value(self.additional_data)
    

