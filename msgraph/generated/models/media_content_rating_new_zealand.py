from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import rating_new_zealand_movies_type, rating_new_zealand_television_type

class MediaContentRatingNewZealand(AdditionalDataHolder, Parsable):
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
        Instantiates a new mediaContentRatingNewZealand and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Movies rating labels in New Zealand
        self._movie_rating: Optional[rating_new_zealand_movies_type.RatingNewZealandMoviesType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # TV content rating labels in New Zealand
        self._tv_rating: Optional[rating_new_zealand_television_type.RatingNewZealandTelevisionType] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MediaContentRatingNewZealand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MediaContentRatingNewZealand
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MediaContentRatingNewZealand()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "movie_rating": lambda n : setattr(self, 'movie_rating', n.get_enum_value(rating_new_zealand_movies_type.RatingNewZealandMoviesType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tv_rating": lambda n : setattr(self, 'tv_rating', n.get_enum_value(rating_new_zealand_television_type.RatingNewZealandTelevisionType)),
        }
        return fields

    @property
    def movie_rating(self,) -> Optional[rating_new_zealand_movies_type.RatingNewZealandMoviesType]:
        """
        Gets the movieRating property value. Movies rating labels in New Zealand
        Returns: Optional[rating_new_zealand_movies_type.RatingNewZealandMoviesType]
        """
        return self._movie_rating

    @movie_rating.setter
    def movie_rating(self,value: Optional[rating_new_zealand_movies_type.RatingNewZealandMoviesType] = None) -> None:
        """
        Sets the movieRating property value. Movies rating labels in New Zealand
        Args:
            value: Value to set for the movieRating property.
        """
        self._movie_rating = value

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
        writer.write_enum_value("movieRating", self.movie_rating)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("tvRating", self.tv_rating)
        writer.write_additional_data_value(self.additional_data)

    @property
    def tv_rating(self,) -> Optional[rating_new_zealand_television_type.RatingNewZealandTelevisionType]:
        """
        Gets the tvRating property value. TV content rating labels in New Zealand
        Returns: Optional[rating_new_zealand_television_type.RatingNewZealandTelevisionType]
        """
        return self._tv_rating

    @tv_rating.setter
    def tv_rating(self,value: Optional[rating_new_zealand_television_type.RatingNewZealandTelevisionType] = None) -> None:
        """
        Sets the tvRating property value. TV content rating labels in New Zealand
        Args:
            value: Value to set for the tvRating property.
        """
        self._tv_rating = value

