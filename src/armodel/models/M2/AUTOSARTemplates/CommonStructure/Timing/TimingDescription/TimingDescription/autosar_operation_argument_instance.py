"""AutosarOperationArgumentInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class AutosarOperationArgumentInstance(Identifiable):
    """AUTOSAR AutosarOperationArgumentInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operation", None, False, False, DataPrototype),  # operation
    ]

    def __init__(self) -> None:
        """Initialize AutosarOperationArgumentInstance."""
        super().__init__()
        self.operation: Optional[DataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AutosarOperationArgumentInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarOperationArgumentInstance":
        """Create AutosarOperationArgumentInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AutosarOperationArgumentInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AutosarOperationArgumentInstance since parent returns ARObject
        return cast("AutosarOperationArgumentInstance", obj)


class AutosarOperationArgumentInstanceBuilder:
    """Builder for AutosarOperationArgumentInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarOperationArgumentInstance = AutosarOperationArgumentInstance()

    def build(self) -> AutosarOperationArgumentInstance:
        """Build and return AutosarOperationArgumentInstance object.

        Returns:
            AutosarOperationArgumentInstance instance
        """
        # TODO: Add validation
        return self._obj
