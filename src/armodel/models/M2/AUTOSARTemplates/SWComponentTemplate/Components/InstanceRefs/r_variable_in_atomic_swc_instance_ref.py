"""RVariableInAtomicSwcInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.variable_in_atomic_swc_instance_ref import (
    VariableInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    """AUTOSAR RVariableInAtomicSwcInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_r_port_prototype", None, False, False, AbstractRequiredPortPrototype),  # contextRPortPrototype
        ("target_data_element", None, False, False, VariableDataPrototype),  # targetDataElement
    ]

    def __init__(self) -> None:
        """Initialize RVariableInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_data_element: Optional[VariableDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RVariableInAtomicSwcInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RVariableInAtomicSwcInstanceRef":
        """Create RVariableInAtomicSwcInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RVariableInAtomicSwcInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RVariableInAtomicSwcInstanceRef since parent returns ARObject
        return cast("RVariableInAtomicSwcInstanceRef", obj)


class RVariableInAtomicSwcInstanceRefBuilder:
    """Builder for RVariableInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RVariableInAtomicSwcInstanceRef = RVariableInAtomicSwcInstanceRef()

    def build(self) -> RVariableInAtomicSwcInstanceRef:
        """Build and return RVariableInAtomicSwcInstanceRef object.

        Returns:
            RVariableInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
