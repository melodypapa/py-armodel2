"""FMFormulaByFeaturesAndAttributes AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFormulaByFeaturesAndAttributes(ARObject):
    """AUTOSAR FMFormulaByFeaturesAndAttributes."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("attribute", None, False, False, FMAttributeDef),  # attribute
        ("feature", None, False, False, FMFeature),  # feature
    ]

    def __init__(self) -> None:
        """Initialize FMFormulaByFeaturesAndAttributes."""
        super().__init__()
        self.attribute: Optional[FMAttributeDef] = None
        self.feature: Optional[FMFeature] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFormulaByFeaturesAndAttributes to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFormulaByFeaturesAndAttributes":
        """Create FMFormulaByFeaturesAndAttributes from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFormulaByFeaturesAndAttributes instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFormulaByFeaturesAndAttributes since parent returns ARObject
        return cast("FMFormulaByFeaturesAndAttributes", obj)


class FMFormulaByFeaturesAndAttributesBuilder:
    """Builder for FMFormulaByFeaturesAndAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFormulaByFeaturesAndAttributes = FMFormulaByFeaturesAndAttributes()

    def build(self) -> FMFormulaByFeaturesAndAttributes:
        """Build and return FMFormulaByFeaturesAndAttributes object.

        Returns:
            FMFormulaByFeaturesAndAttributes instance
        """
        # TODO: Add validation
        return self._obj
