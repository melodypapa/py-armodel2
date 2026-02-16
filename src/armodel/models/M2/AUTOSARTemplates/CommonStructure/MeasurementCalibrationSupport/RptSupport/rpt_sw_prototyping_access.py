"""RptSwPrototypingAccess AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class RptSwPrototypingAccess(ARObject):
    """AUTOSAR RptSwPrototypingAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("rpt_hook_access", None, False, False, RptAccessEnum),  # rptHookAccess
        ("rpt_read_access", None, False, False, RptAccessEnum),  # rptReadAccess
        ("rpt_write_access", None, False, False, RptAccessEnum),  # rptWriteAccess
    ]

    def __init__(self) -> None:
        """Initialize RptSwPrototypingAccess."""
        super().__init__()
        self.rpt_hook_access: Optional[RptAccessEnum] = None
        self.rpt_read_access: Optional[RptAccessEnum] = None
        self.rpt_write_access: Optional[RptAccessEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RptSwPrototypingAccess to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptSwPrototypingAccess":
        """Create RptSwPrototypingAccess from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RptSwPrototypingAccess instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RptSwPrototypingAccess since parent returns ARObject
        return cast("RptSwPrototypingAccess", obj)


class RptSwPrototypingAccessBuilder:
    """Builder for RptSwPrototypingAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptSwPrototypingAccess = RptSwPrototypingAccess()

    def build(self) -> RptSwPrototypingAccess:
        """Build and return RptSwPrototypingAccess object.

        Returns:
            RptSwPrototypingAccess instance
        """
        # TODO: Add validation
        return self._obj
