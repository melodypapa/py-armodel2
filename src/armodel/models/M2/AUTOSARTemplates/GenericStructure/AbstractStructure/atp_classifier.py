"""AtpClassifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)


class AtpClassifier(Identifiable):
    """AUTOSAR AtpClassifier."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("atp_features", None, False, True, AtpFeature),  # atpFeatures
    ]

    def __init__(self) -> None:
        """Initialize AtpClassifier."""
        super().__init__()
        self.atp_features: list[AtpFeature] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AtpClassifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpClassifier":
        """Create AtpClassifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AtpClassifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AtpClassifier since parent returns ARObject
        return cast("AtpClassifier", obj)


class AtpClassifierBuilder:
    """Builder for AtpClassifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpClassifier = AtpClassifier()

    def build(self) -> AtpClassifier:
        """Build and return AtpClassifier object.

        Returns:
            AtpClassifier instance
        """
        # TODO: Add validation
        return self._obj
