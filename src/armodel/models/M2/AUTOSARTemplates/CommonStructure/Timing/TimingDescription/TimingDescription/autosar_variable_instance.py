"""AutosarVariableInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class AutosarVariableInstance(Identifiable):
    """AUTOSAR AutosarVariableInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("variable_instance_instance_ref", None, False, False, DataPrototype),  # variableInstanceInstanceRef
    ]

    def __init__(self) -> None:
        """Initialize AutosarVariableInstance."""
        super().__init__()
        self.variable_instance_instance_ref: Optional[DataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AutosarVariableInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarVariableInstance":
        """Create AutosarVariableInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AutosarVariableInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AutosarVariableInstance since parent returns ARObject
        return cast("AutosarVariableInstance", obj)


class AutosarVariableInstanceBuilder:
    """Builder for AutosarVariableInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarVariableInstance = AutosarVariableInstance()

    def build(self) -> AutosarVariableInstance:
        """Build and return AutosarVariableInstance object.

        Returns:
            AutosarVariableInstance instance
        """
        # TODO: Add validation
        return self._obj
