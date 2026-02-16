"""FMFeatureDecomposition AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFeatureDecomposition(ARObject):
    """AUTOSAR FMFeatureDecomposition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "category": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # category
        "features": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FMFeature,
        ),  # features
        "max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # max
        "min": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # min
    }

    def __init__(self) -> None:
        """Initialize FMFeatureDecomposition."""
        super().__init__()
        self.category: Optional[CategoryString] = None
        self.features: list[FMFeature] = []
        self.max: Optional[PositiveInteger] = None
        self.min: Optional[PositiveInteger] = None


class FMFeatureDecompositionBuilder:
    """Builder for FMFeatureDecomposition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureDecomposition = FMFeatureDecomposition()

    def build(self) -> FMFeatureDecomposition:
        """Build and return FMFeatureDecomposition object.

        Returns:
            FMFeatureDecomposition instance
        """
        # TODO: Add validation
        return self._obj
