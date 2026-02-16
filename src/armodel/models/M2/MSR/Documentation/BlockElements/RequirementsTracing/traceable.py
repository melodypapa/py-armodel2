"""Traceable AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)


class Traceable(MultilanguageReferrable):
    """AUTOSAR Traceable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("traces", None, False, True, Traceable),  # traces
    ]

    def __init__(self) -> None:
        """Initialize Traceable."""
        super().__init__()
        self.traces: list[Traceable] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Traceable to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Traceable":
        """Create Traceable from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Traceable instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Traceable since parent returns ARObject
        return cast("Traceable", obj)


class TraceableBuilder:
    """Builder for Traceable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Traceable = Traceable()

    def build(self) -> Traceable:
        """Build and return Traceable object.

        Returns:
            Traceable instance
        """
        # TODO: Add validation
        return self._obj
