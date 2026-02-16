"""EcucDefinitionCollection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)


class EcucDefinitionCollection(ARElement):
    """AUTOSAR EcucDefinitionCollection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("modules", None, False, True, EcucModuleDef),  # modules
    ]

    def __init__(self) -> None:
        """Initialize EcucDefinitionCollection."""
        super().__init__()
        self.modules: list[EcucModuleDef] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucDefinitionCollection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDefinitionCollection":
        """Create EcucDefinitionCollection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucDefinitionCollection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucDefinitionCollection since parent returns ARObject
        return cast("EcucDefinitionCollection", obj)


class EcucDefinitionCollectionBuilder:
    """Builder for EcucDefinitionCollection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDefinitionCollection = EcucDefinitionCollection()

    def build(self) -> EcucDefinitionCollection:
        """Build and return EcucDefinitionCollection object.

        Returns:
            EcucDefinitionCollection instance
        """
        # TODO: Add validation
        return self._obj
