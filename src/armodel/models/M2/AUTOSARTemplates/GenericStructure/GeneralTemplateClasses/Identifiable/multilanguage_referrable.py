"""MultilanguageReferrable AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class MultilanguageReferrable(Referrable):
    """AUTOSAR MultilanguageReferrable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("long_name", None, False, False, MultilanguageLongName),  # longName
    ]

    def __init__(self) -> None:
        """Initialize MultilanguageReferrable."""
        super().__init__()
        self.long_name: Optional[MultilanguageLongName] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MultilanguageReferrable to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultilanguageReferrable":
        """Create MultilanguageReferrable from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MultilanguageReferrable instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MultilanguageReferrable since parent returns ARObject
        return cast("MultilanguageReferrable", obj)


class MultilanguageReferrableBuilder:
    """Builder for MultilanguageReferrable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultilanguageReferrable = MultilanguageReferrable()

    def build(self) -> MultilanguageReferrable:
        """Build and return MultilanguageReferrable object.

        Returns:
            MultilanguageReferrable instance
        """
        # TODO: Add validation
        return self._obj
