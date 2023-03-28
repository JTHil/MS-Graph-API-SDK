from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class MdurationPostRequestBody(AdditionalDataHolder, Parsable):
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
    
    @property
    def basis(self,) -> Optional[json.Json]:
        """
        Gets the basis property value. The basis property
        Returns: Optional[json.Json]
        """
        return self._basis
    
    @basis.setter
    def basis(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the basis property value. The basis property
        Args:
            value: Value to set for the basis property.
        """
        self._basis = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new mdurationPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The basis property
        self._basis: Optional[json.Json] = None
        # The coupon property
        self._coupon: Optional[json.Json] = None
        # The frequency property
        self._frequency: Optional[json.Json] = None
        # The maturity property
        self._maturity: Optional[json.Json] = None
        # The settlement property
        self._settlement: Optional[json.Json] = None
        # The yld property
        self._yld: Optional[json.Json] = None
    
    @property
    def coupon(self,) -> Optional[json.Json]:
        """
        Gets the coupon property value. The coupon property
        Returns: Optional[json.Json]
        """
        return self._coupon
    
    @coupon.setter
    def coupon(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the coupon property value. The coupon property
        Args:
            value: Value to set for the coupon property.
        """
        self._coupon = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MdurationPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MdurationPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MdurationPostRequestBody()
    
    @property
    def frequency(self,) -> Optional[json.Json]:
        """
        Gets the frequency property value. The frequency property
        Returns: Optional[json.Json]
        """
        return self._frequency
    
    @frequency.setter
    def frequency(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the frequency property value. The frequency property
        Args:
            value: Value to set for the frequency property.
        """
        self._frequency = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "basis": lambda n : setattr(self, 'basis', n.get_object_value(json.Json)),
            "coupon": lambda n : setattr(self, 'coupon', n.get_object_value(json.Json)),
            "frequency": lambda n : setattr(self, 'frequency', n.get_object_value(json.Json)),
            "maturity": lambda n : setattr(self, 'maturity', n.get_object_value(json.Json)),
            "settlement": lambda n : setattr(self, 'settlement', n.get_object_value(json.Json)),
            "yld": lambda n : setattr(self, 'yld', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def maturity(self,) -> Optional[json.Json]:
        """
        Gets the maturity property value. The maturity property
        Returns: Optional[json.Json]
        """
        return self._maturity
    
    @maturity.setter
    def maturity(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the maturity property value. The maturity property
        Args:
            value: Value to set for the maturity property.
        """
        self._maturity = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("basis", self.basis)
        writer.write_object_value("coupon", self.coupon)
        writer.write_object_value("frequency", self.frequency)
        writer.write_object_value("maturity", self.maturity)
        writer.write_object_value("settlement", self.settlement)
        writer.write_object_value("yld", self.yld)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def settlement(self,) -> Optional[json.Json]:
        """
        Gets the settlement property value. The settlement property
        Returns: Optional[json.Json]
        """
        return self._settlement
    
    @settlement.setter
    def settlement(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the settlement property value. The settlement property
        Args:
            value: Value to set for the settlement property.
        """
        self._settlement = value
    
    @property
    def yld(self,) -> Optional[json.Json]:
        """
        Gets the yld property value. The yld property
        Returns: Optional[json.Json]
        """
        return self._yld
    
    @yld.setter
    def yld(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the yld property value. The yld property
        Args:
            value: Value to set for the yld property.
        """
        self._yld = value
    

