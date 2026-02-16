"""Code AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class Code(Identifiable):
    """AUTOSAR Code."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("artifacts", None, False, True, AutosarEngineeringObject),  # artifacts
        ("callback_headers", None, False, True, ServiceNeeds),  # callbackHeaders
    ]

    def __init__(self) -> None:
        """Initialize Code."""
        super().__init__()
        self.artifacts: list[AutosarEngineeringObject] = []
        self.callback_headers: list[ServiceNeeds] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Code to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Code":
        """Create Code from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Code instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Code since parent returns ARObject
        return cast("Code", obj)


class CodeBuilder:
    """Builder for Code."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Code = Code()

    def build(self) -> Code:
        """Build and return Code object.

        Returns:
            Code instance
        """
        # TODO: Add validation
        return self._obj
