"""EcucContainerValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)


class EcucContainerValue(Identifiable):
    """AUTOSAR EcucContainerValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("definition", None, False, False, EcucContainerDef),  # definition
        ("parameter_values", None, False, True, EcucParameterValue),  # parameterValues
        ("reference_values", None, False, True, any (EcucAbstractReference)),  # referenceValues
        ("sub_containers", None, False, True, EcucContainerValue),  # subContainers
    ]

    def __init__(self) -> None:
        """Initialize EcucContainerValue."""
        super().__init__()
        self.definition: Optional[EcucContainerDef] = None
        self.parameter_values: list[EcucParameterValue] = []
        self.reference_values: list[Any] = []
        self.sub_containers: list[EcucContainerValue] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucContainerValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucContainerValue":
        """Create EcucContainerValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucContainerValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucContainerValue since parent returns ARObject
        return cast("EcucContainerValue", obj)


class EcucContainerValueBuilder:
    """Builder for EcucContainerValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucContainerValue = EcucContainerValue()

    def build(self) -> EcucContainerValue:
        """Build and return EcucContainerValue object.

        Returns:
            EcucContainerValue instance
        """
        # TODO: Add validation
        return self._obj
