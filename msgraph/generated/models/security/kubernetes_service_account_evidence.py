from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

from .alert_evidence import AlertEvidence

@dataclass
class KubernetesServiceAccountEvidence(AlertEvidence):
    odata_type = "#microsoft.graph.security.kubernetesServiceAccountEvidence"
    # The name property
    name: Optional[str] = None
    # The namespace property
    namespace: Optional[KubernetesNamespaceEvidence] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> KubernetesServiceAccountEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KubernetesServiceAccountEvidence
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return KubernetesServiceAccountEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

        from .alert_evidence import AlertEvidence
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_object_value(KubernetesNamespaceEvidence)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("name", self.name)
        writer.write_object_value("namespace", self.namespace)
    

