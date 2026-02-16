"""VariableAccess AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)


class VariableAccess(AbstractAccessPoint):
    """AUTOSAR VariableAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("accessed_variable", None, False, False, AutosarVariableRef),  # accessedVariable
        ("scope", None, False, False, VariableAccessScopeEnum),  # scope
    ]

    def __init__(self) -> None:
        """Initialize VariableAccess."""
        super().__init__()
        self.accessed_variable: Optional[AutosarVariableRef] = None
        self.scope: Optional[VariableAccessScopeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert VariableAccess to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableAccess":
        """Create VariableAccess from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            VariableAccess instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to VariableAccess since parent returns ARObject
        return cast("VariableAccess", obj)


class VariableAccessBuilder:
    """Builder for VariableAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableAccess = VariableAccess()

    def build(self) -> VariableAccess:
        """Build and return VariableAccess object.

        Returns:
            VariableAccess instance
        """
        # TODO: Add validation
        return self._obj
