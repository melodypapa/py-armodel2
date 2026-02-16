"""DiagnosticAuthRoleProxy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
    DiagnosticAuthRole,
)


class DiagnosticAuthRoleProxy(ARObject):
    """AUTOSAR DiagnosticAuthRoleProxy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("authentications", None, False, True, DiagnosticAuthRole),  # authentications
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAuthRoleProxy."""
        super().__init__()
        self.authentications: list[DiagnosticAuthRole] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAuthRoleProxy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthRoleProxy":
        """Create DiagnosticAuthRoleProxy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAuthRoleProxy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAuthRoleProxy since parent returns ARObject
        return cast("DiagnosticAuthRoleProxy", obj)


class DiagnosticAuthRoleProxyBuilder:
    """Builder for DiagnosticAuthRoleProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthRoleProxy = DiagnosticAuthRoleProxy()

    def build(self) -> DiagnosticAuthRoleProxy:
        """Build and return DiagnosticAuthRoleProxy object.

        Returns:
            DiagnosticAuthRoleProxy instance
        """
        # TODO: Add validation
        return self._obj
