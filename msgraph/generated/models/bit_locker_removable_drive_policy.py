from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bit_locker_encryption_method import BitLockerEncryptionMethod

@dataclass
class BitLockerRemovableDrivePolicy(AdditionalDataHolder, BackedModel, Parsable):
    """
    BitLocker Removable Drive Policies.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # This policy setting determines whether BitLocker protection is required for removable data drives to be writable on a computer.
    block_cross_organization_write_access: Optional[bool] = None
    # Select the encryption method for removable  drives. Possible values are: aesCbc128, aesCbc256, xtsAes128, xtsAes256.
    encryption_method: Optional[BitLockerEncryptionMethod] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether to block write access to devices configured in another organization.  If requireEncryptionForWriteAccess is false, this value does not affect.
    require_encryption_for_write_access: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BitLockerRemovableDrivePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BitLockerRemovableDrivePolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BitLockerRemovableDrivePolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .bit_locker_encryption_method import BitLockerEncryptionMethod

        from .bit_locker_encryption_method import BitLockerEncryptionMethod

        fields: Dict[str, Callable[[Any], None]] = {
            "blockCrossOrganizationWriteAccess": lambda n : setattr(self, 'block_cross_organization_write_access', n.get_bool_value()),
            "encryptionMethod": lambda n : setattr(self, 'encryption_method', n.get_enum_value(BitLockerEncryptionMethod)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requireEncryptionForWriteAccess": lambda n : setattr(self, 'require_encryption_for_write_access', n.get_bool_value()),
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
        writer.write_bool_value("blockCrossOrganizationWriteAccess", self.block_cross_organization_write_access)
        writer.write_enum_value("encryptionMethod", self.encryption_method)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_bool_value("requireEncryptionForWriteAccess", self.require_encryption_for_write_access)
        writer.write_additional_data_value(self.additional_data)
    

