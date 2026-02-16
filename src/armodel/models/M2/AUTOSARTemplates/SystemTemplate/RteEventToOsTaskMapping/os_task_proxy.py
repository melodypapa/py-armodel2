"""OsTaskProxy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class OsTaskProxy(ARElement):
    """AUTOSAR OsTaskProxy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("period", None, True, False, None),  # period
        ("preemptability", None, False, False, OsTaskPreemptabilityEnum),  # preemptability
        ("priority", None, True, False, None),  # priority
    ]

    def __init__(self) -> None:
        """Initialize OsTaskProxy."""
        super().__init__()
        self.period: Optional[TimeValue] = None
        self.preemptability: Optional[OsTaskPreemptabilityEnum] = None
        self.priority: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert OsTaskProxy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OsTaskProxy":
        """Create OsTaskProxy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            OsTaskProxy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to OsTaskProxy since parent returns ARObject
        return cast("OsTaskProxy", obj)


class OsTaskProxyBuilder:
    """Builder for OsTaskProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OsTaskProxy = OsTaskProxy()

    def build(self) -> OsTaskProxy:
        """Build and return OsTaskProxy object.

        Returns:
            OsTaskProxy instance
        """
        # TODO: Add validation
        return self._obj
