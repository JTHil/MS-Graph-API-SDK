from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_fill import WorkbookChartFill

from .entity import Entity

@dataclass
class WorkbookChartPointFormat(Entity):
    # Represents the fill format of a chart, which includes background formating information. Read-only.
    fill: Optional[WorkbookChartFill] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartPointFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartPointFormat
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartPointFormat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_fill import WorkbookChartFill

        from .entity import Entity
        from .workbook_chart_fill import WorkbookChartFill

        fields: Dict[str, Callable[[Any], None]] = {
            "fill": lambda n : setattr(self, 'fill', n.get_object_value(WorkbookChartFill)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("fill", self.fill)
    

