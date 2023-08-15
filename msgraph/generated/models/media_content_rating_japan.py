from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .rating_japan_movies_type import RatingJapanMoviesType
    from .rating_japan_television_type import RatingJapanTelevisionType

@dataclass
class MediaContentRatingJapan(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Movies rating labels in Japan
    movie_rating: Optional[RatingJapanMoviesType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # TV content rating labels in Japan
    tv_rating: Optional[RatingJapanTelevisionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MediaContentRatingJapan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MediaContentRatingJapan
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MediaContentRatingJapan()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .rating_japan_movies_type import RatingJapanMoviesType
        from .rating_japan_television_type import RatingJapanTelevisionType

        from .rating_japan_movies_type import RatingJapanMoviesType
        from .rating_japan_television_type import RatingJapanTelevisionType

        fields: Dict[str, Callable[[Any], None]] = {
            "movieRating": lambda n : setattr(self, 'movie_rating', n.get_enum_value(RatingJapanMoviesType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tvRating": lambda n : setattr(self, 'tv_rating', n.get_enum_value(RatingJapanTelevisionType)),
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
        writer.write_enum_value("movieRating", self.movie_rating)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("tvRating", self.tv_rating)
        writer.write_additional_data_value(self.additional_data)
    

