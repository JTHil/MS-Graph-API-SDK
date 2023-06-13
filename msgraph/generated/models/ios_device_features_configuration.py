from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_device_features_configuration_base, ios_home_screen_item, ios_home_screen_page, ios_notification_settings

from . import apple_device_features_configuration_base

@dataclass
class IosDeviceFeaturesConfiguration(apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase):
    odata_type = "#microsoft.graph.iosDeviceFeaturesConfiguration"
    # Asset tag information for the device, displayed on the login window and lock screen.
    asset_tag_template: Optional[str] = None
    # A list of app and folders to appear on the Home Screen Dock. This collection can contain a maximum of 500 elements.
    home_screen_dock_icons: Optional[List[ios_home_screen_item.IosHomeScreenItem]] = None
    # A list of pages on the Home Screen. This collection can contain a maximum of 500 elements.
    home_screen_pages: Optional[List[ios_home_screen_page.IosHomeScreenPage]] = None
    # A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.
    lock_screen_footnote: Optional[str] = None
    # Notification settings for each bundle id. Applicable to devices in supervised mode only (iOS 9.3 and later). This collection can contain a maximum of 500 elements.
    notification_settings: Optional[List[ios_notification_settings.IosNotificationSettings]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosDeviceFeaturesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosDeviceFeaturesConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosDeviceFeaturesConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_device_features_configuration_base, ios_home_screen_item, ios_home_screen_page, ios_notification_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "assetTagTemplate": lambda n : setattr(self, 'asset_tag_template', n.get_str_value()),
            "homeScreenDockIcons": lambda n : setattr(self, 'home_screen_dock_icons', n.get_collection_of_object_values(ios_home_screen_item.IosHomeScreenItem)),
            "homeScreenPages": lambda n : setattr(self, 'home_screen_pages', n.get_collection_of_object_values(ios_home_screen_page.IosHomeScreenPage)),
            "lockScreenFootnote": lambda n : setattr(self, 'lock_screen_footnote', n.get_str_value()),
            "notificationSettings": lambda n : setattr(self, 'notification_settings', n.get_collection_of_object_values(ios_notification_settings.IosNotificationSettings)),
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
        writer.write_str_value("assetTagTemplate", self.asset_tag_template)
        writer.write_collection_of_object_values("homeScreenDockIcons", self.home_screen_dock_icons)
        writer.write_collection_of_object_values("homeScreenPages", self.home_screen_pages)
        writer.write_str_value("lockScreenFootnote", self.lock_screen_footnote)
        writer.write_collection_of_object_values("notificationSettings", self.notification_settings)
    

