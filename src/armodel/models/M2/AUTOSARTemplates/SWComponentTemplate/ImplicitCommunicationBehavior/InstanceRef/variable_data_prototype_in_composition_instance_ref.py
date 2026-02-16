"""VariableDataPrototypeInCompositionInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class VariableDataPrototypeInCompositionInstanceRef(ARObject):
    """AUTOSAR VariableDataPrototypeInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, CompositionSwComponentType),  # base
        ("context_port", None, False, False, PortPrototype),  # contextPort
        ("context_sws", None, False, True, any (SwComponent)),  # contextSws
        ("target_variable", None, False, False, VariableDataPrototype),  # targetVariable
    ]

    def __init__(self) -> None:
        """Initialize VariableDataPrototypeInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_port: Optional[PortPrototype] = None
        self.context_sws: list[Any] = []
        self.target_variable: Optional[VariableDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert VariableDataPrototypeInCompositionInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableDataPrototypeInCompositionInstanceRef":
        """Create VariableDataPrototypeInCompositionInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            VariableDataPrototypeInCompositionInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to VariableDataPrototypeInCompositionInstanceRef since parent returns ARObject
        return cast("VariableDataPrototypeInCompositionInstanceRef", obj)


class VariableDataPrototypeInCompositionInstanceRefBuilder:
    """Builder for VariableDataPrototypeInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableDataPrototypeInCompositionInstanceRef = VariableDataPrototypeInCompositionInstanceRef()

    def build(self) -> VariableDataPrototypeInCompositionInstanceRef:
        """Build and return VariableDataPrototypeInCompositionInstanceRef object.

        Returns:
            VariableDataPrototypeInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
