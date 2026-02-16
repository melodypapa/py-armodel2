"""AtpInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_classifier import (
    AtpClassifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_prototype import (
    AtpPrototype,
)


class AtpInstanceRef(ARObject):
    """AUTOSAR AtpInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("atp_base", None, False, False, AtpClassifier),  # atpBase
        ("atp_contexts", None, False, True, AtpPrototype),  # atpContexts
        ("atp_target", None, False, False, AtpFeature),  # atpTarget
    ]

    def __init__(self) -> None:
        """Initialize AtpInstanceRef."""
        super().__init__()
        self.atp_base: AtpClassifier = None
        self.atp_contexts: list[AtpPrototype] = []
        self.atp_target: AtpFeature = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AtpInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpInstanceRef":
        """Create AtpInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AtpInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AtpInstanceRef since parent returns ARObject
        return cast("AtpInstanceRef", obj)


class AtpInstanceRefBuilder:
    """Builder for AtpInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpInstanceRef = AtpInstanceRef()

    def build(self) -> AtpInstanceRef:
        """Build and return AtpInstanceRef object.

        Returns:
            AtpInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
