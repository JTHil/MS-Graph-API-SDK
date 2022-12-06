from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_rights_request = lazy_import('msgraph.generated.models.subject_rights_request')

class Privacy(AdditionalDataHolder, Parsable):
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
        Instantiates a new Privacy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The subjectRightsRequests property
        self._subject_rights_requests: Optional[List[subject_rights_request.SubjectRightsRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Privacy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Privacy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Privacy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "subject_rights_requests": lambda n : setattr(self, 'subject_rights_requests', n.get_collection_of_object_values(subject_rights_request.SubjectRightsRequest)),
        }
        return fields
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("subjectRightsRequests", self.subject_rights_requests)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subject_rights_requests(self,) -> Optional[List[subject_rights_request.SubjectRightsRequest]]:
        """
        Gets the subjectRightsRequests property value. The subjectRightsRequests property
        Returns: Optional[List[subject_rights_request.SubjectRightsRequest]]
        """
        return self._subject_rights_requests
    
    @subject_rights_requests.setter
    def subject_rights_requests(self,value: Optional[List[subject_rights_request.SubjectRightsRequest]] = None) -> None:
        """
        Sets the subjectRightsRequests property value. The subjectRightsRequests property
        Args:
            value: Value to set for the subjectRightsRequests property.
        """
        self._subject_rights_requests = value
    

