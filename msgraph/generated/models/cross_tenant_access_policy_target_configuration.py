from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_access_policy_target import CrossTenantAccessPolicyTarget
    from .cross_tenant_access_policy_target_configuration_access_type import CrossTenantAccessPolicyTargetConfigurationAccessType

@dataclass
class CrossTenantAccessPolicyTargetConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Defines whether access is allowed or blocked. The possible values are: allowed, blocked, unknownFutureValue.
    access_type: Optional[CrossTenantAccessPolicyTargetConfigurationAccessType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies whether to target users, groups, or applications with this rule.
    targets: Optional[List[CrossTenantAccessPolicyTarget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyTargetConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyTargetConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantAccessPolicyTargetConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_access_policy_target import CrossTenantAccessPolicyTarget
        from .cross_tenant_access_policy_target_configuration_access_type import CrossTenantAccessPolicyTargetConfigurationAccessType

        from .cross_tenant_access_policy_target import CrossTenantAccessPolicyTarget
        from .cross_tenant_access_policy_target_configuration_access_type import CrossTenantAccessPolicyTargetConfigurationAccessType

        fields: Dict[str, Callable[[Any], None]] = {
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(CrossTenantAccessPolicyTargetConfigurationAccessType)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(CrossTenantAccessPolicyTarget)),
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
        writer.write_enum_value("accessType", self.access_type)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_additional_data_value(self.additional_data)
    

