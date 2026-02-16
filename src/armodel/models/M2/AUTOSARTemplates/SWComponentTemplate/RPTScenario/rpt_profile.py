"""RptProfile AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    PositiveInteger,
)


class RptProfile(Identifiable):
    """AUTOSAR RptProfile."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_service", None, True, False, None),  # maxService
        ("min_service_point", None, True, False, None),  # minServicePoint
        ("service_point", None, True, False, None),  # servicePoint
        ("stim_enabler", None, False, False, RptEnablerImplTypeEnum),  # stimEnabler
    ]

    def __init__(self) -> None:
        """Initialize RptProfile."""
        super().__init__()
        self.max_service: Optional[PositiveInteger] = None
        self.min_service_point: Optional[PositiveInteger] = None
        self.service_point: Optional[CIdentifier] = None
        self.stim_enabler: Optional[RptEnablerImplTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RptProfile to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptProfile":
        """Create RptProfile from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RptProfile instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RptProfile since parent returns ARObject
        return cast("RptProfile", obj)


class RptProfileBuilder:
    """Builder for RptProfile."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptProfile = RptProfile()

    def build(self) -> RptProfile:
        """Build and return RptProfile object.

        Returns:
            RptProfile instance
        """
        # TODO: Add validation
        return self._obj
